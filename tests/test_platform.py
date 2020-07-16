import unittest
import pathlib
import sys
sys.path.append("../competest")
import os
from competest import parsers, competest
from click.testing import CliRunner


if sys.platform == "linux":
    import competest.linux as platform
else:
    import competest.windows as platform

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

java_file_path = pathlib.Path(os.path.join(
    THIS_DIR, "test_programs", "test_java_sample.java")).resolve()
python_file_path = pathlib.Path(os.path.join(
    THIS_DIR, "test_programs", "test_python_sample.py")).resolve()
c_source_path = os.path.join(
    THIS_DIR, "test_programs", "test_exe_sample.c")
cpp_source_path = os.path.join(
    THIS_DIR, "test_programs", "test_cpp_sample.cpp")
test_case_file_path = os.path.join(
    THIS_DIR, "test_programs", "test_cases.json")


class DummyFile():
    def __init__(self, data, name=None):
        self.contents = data
        self.name = name

    def read(self):
        return self.contents


class TestParsers(unittest.TestCase):

    def test_parse_cases_json(self):
        self.assertEqual(
            parsers.parse_cases_json(DummyFile(
                '[{"input":["1","2"],"output":["5","3"]}]'
            )),
            [{'input': ['1', '2'], 'output': ['5', '3']}]
        )
        self.assertEqual(
            parsers.parse_cases_json(DummyFile(
                '''[{"input":["1","2"],"output":["5","3"]},
                {"input":["ab"],"output":["aa"]}]'''
            )),
            [{'input': ['1', '2'], 'output': ['5', '3']},
                {'input': ['ab'], 'output': ['aa']}]
        )

    def test_parse_cases_txt(self):
        self.assertEqual(
            parsers.parse_cases_txt(DummyFile(
                "1\n2\n\n5\n3".strip())
            ),
            [{'input': ['1', '2'], 'output': ['5', '3']}]
        )
        self.assertEqual(
            parsers.parse_cases_txt(DummyFile(
                "1\n2\n\n5\n3\n\nab\n\naa".strip())),
            [{'input': ['1', '2'], 'output': ['5', '3']},
                {'input': ['ab'], "output": ['aa']}]
        )


class TestMainUtils(unittest.TestCase):
    def get_test_cases_test(self):
        self.assertEqual(competest.get_test_cases(DummyFile(
            '[{"input":["1","2"],"output":["5","3"]}]', "cases.json")),
            [{'input': ['1', '2'], 'output': ['5', '3']}])
        self.assertEqual(competest.get_test_cases(DummyFile(
            '''[{"input":["1","2"],"output":["5","3"]},
            {"input":["ab"],"output":["aa"]}]''',
            "cases.json")),
            [{'input': ['1', '2'], 'output': ['5', '3']},
                {'input': ['ab'], 'output': ['aa']}]
        )

    def test_compile_if_needed(self):
        competest.compile_if_needed(java_file_path, "java")


class TestMainPython(unittest.TestCase):
    def test_main_python(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["python", str(python_file_path), "-t", test_case_file_path]
        )
        self.assertTrue("All tests passed successfully." in result.output)


class TestMainJava(unittest.TestCase):
    def test_main_java(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["java", str(java_file_path), "-t", test_case_file_path]
        )
        self.assertTrue("All tests passed successfully." in result.output)


class TestMainC(unittest.TestCase):
    def test_main_c(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["c", str(c_source_path), "-t", test_case_file_path]
        )
        self.assertTrue("All tests passed successfully." in result.output)


class TestMainCpp(unittest.TestCase):
    def test_main_cpp(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["cpp", str(cpp_source_path), "-t", test_case_file_path]
        )
        self.assertTrue("All tests passed successfully." in result.output)


if __name__ == "__main__":
    unittest.main()
