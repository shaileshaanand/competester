import unittest
import sys
import os


if sys.platform == "linux":
    import competest.linux as platform
else:
    import competest.windows as platform

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestPython(unittest.TestCase):
    def test_single(self):
        python_file_path = os.path.join(
            THIS_DIR, "test_programs", "test_python_sample.py")
        process = platform.python(
            python_file_path, "Hello World".strip().encode())
        self.assertEqual(
            process.stdout.decode().strip().replace('\r', ''), "Hello World")


class TestJava(unittest.TestCase):
    def test_single(self):
        java_file_path = os.path.join(
            THIS_DIR, "test_programs", "test_java_sample.java")
        process = platform.java(
            java_file_path, "Hello World".strip().encode())
        self.assertEqual(
            process.stdout.decode().strip().replace('\r', ''), "Hello World")


if __name__ == "__main__":
    unittest.main()
