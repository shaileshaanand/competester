import unittest
import pathlib
import subprocess
import sys
import os
from competest import parsers

if sys.platform == "linux":
    import competest.linux as platform
else:
    import competest.windows as platform

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class DummyFile():
    def __init__(self, data, name=None):
        self.contents = data
        self.name = name

    def read(self):
        return self.contents


class TestPython(unittest.TestCase):
    def test_single(self):
        python_file_path = pathlib.Path(os.path.join(
            THIS_DIR, "test_programs", "test_python_sample.py")).resolve()
        process = platform.python(
            python_file_path, "Hello World".strip().encode())
        self.assertEqual(
            process.stdout.decode().strip().replace('\r', ''), "Hello World")


class TestJava(unittest.TestCase):
    def test_single(self):
        java_file_path = pathlib.Path(os.path.join(
            THIS_DIR, "test_programs", "test_java_sample.java")).resolve()
        process = platform.java(
            java_file_path, "Hello World".strip().encode())
        self.assertEqual(
            process.stdout.decode().strip().replace('\r', ''), "Hello World")


class TestExe(unittest.TestCase):
    def test_single(self):
        exe_source_path = os.path.join(
            THIS_DIR, "test_programs", "test_exe_sample.c")
        exe_output_path = os.path.join(
            THIS_DIR, "test_programs", "test_exe_sample.exe")
        subprocess.run(["gcc", "-o", exe_output_path, exe_source_path])
        process = platform.exe(
            pathlib.Path(exe_output_path).resolve(), "HelloWorld".strip().encode())
        self.assertEqual(
            process.stdout.decode().strip().replace('\r', ''), "HelloWorld")


class TestParsers(unittest.TestCase):

    def test_parse_cases_json(self):
        self.assertEqual(parsers.parse_cases_json(DummyFile(
            '[{"input":["1","2"],"output":["5","3"]}]')), [{'input': ['1', '2'], 'output': ['5', '3']}])
        self.assertEqual(parsers.parse_cases_json(DummyFile(
            '[{"input":["1","2"],"output":["5","3"]},{"input":["ab"],"output":["aa"]}]')), [{'input': ['1', '2'], 'output': ['5', '3']}, {'input': ['ab'], 'output':['aa']}])

    def test_parse_cases_txt(self):
        self.assertEqual(parsers.parse_cases_txt(DummyFile(
            """
1
2

5
3
            """.strip()
        )), [{'input': ['1', '2'], 'output': ['5', '3']}])

        self.assertEqual(parsers.parse_cases_txt(DummyFile(
            """
1
2

5
3

ab

aa
            """.strip()
        )), [{'input': ['1', '2'], 'output': ['5', '3']}, {'input': ['ab'], "output": ['aa']}])


if __name__ == "__main__":
    unittest.main()
