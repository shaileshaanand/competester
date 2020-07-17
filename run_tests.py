from click.testing import CliRunner
import unittest
from competest import competest


class TestPython(unittest.TestCase):
    def test_python_passing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["python", "python_test.py", "-t", "cases_passing.json"]
        )
        self.assertTrue("All tests passed successfully." in result.output)

    def test_python_failing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["python", "python_test.py", "-t", "cases_failing.json"]

        )
        self.assertTrue("1/2 Test Cases Failed" in result.output)


class TestJava(unittest.TestCase):
    def test_java_passing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["java", "java_test.java", "-t", "cases_passing.json"]
        )
        self.assertTrue("All tests passed successfully." in result.output)

    def test_java_failing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["java", "java_test.java", "-t", "cases_failing.json"],

        )
        self.assertTrue("1/2 Test Cases Failed" in result.output)


class TestCpp(unittest.TestCase):
    def test_cpp_passing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["cpp", "cpp_test.cpp", "-t", "cases_passing.json"]
        )
        self.assertTrue("All tests passed successfully." in result.output)

    def test_cpp_failing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["cpp", "cpp_test.cpp", "-t", "cases_failing.json"]

        )
        self.assertTrue("1/2 Test Cases Failed" in result.output)


class TestC(unittest.TestCase):
    def test_c_passing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["c", "c_test.c", "-t", "cases_passing.json"]
        )
        self.assertTrue("All tests passed successfully." in result.output)

    def test_c_failing(self):
        runner = CliRunner()
        result = runner.invoke(
            competest.competest,
            ["c", "c_test.c", "-t", "cases_failing.json"]

        )
        self.assertTrue("1/2 Test Cases Failed" in result.output)


runner = CliRunner()
with runner.isolated_filesystem():
    with open("cases_passing.json", "w") as f:
        f.write(
            """
[
    {
        "input": ["HelloWorld"],
        "output": ["HelloWorld"]
    },
    {
        "input": ["123"],
        "output": ["123"]
    }
]
            """.strip()
        )
    with open("cases_passing.txt", "w") as f:
        f.write(
            """
HelloWorld

HelloWorld

123

123
            """.strip()
        )
    with open("cases_failing.json", "w") as f:
        f.write(
            """
[
    {
        "input": ["Something"],
        "output": ["SomethingElse"]
    },
    {
        "input": ["123"],
        "output": ["123"]
    }
]
            """.strip()
        )
    with open("cases_failing.txt", "w") as f:
        f.write(
            """
Something

SomethingElse

123

123
            """.strip()
        )
    with open("python_test.py", "w") as f:
        f.write(
            """
print(input())
            """.strip()
        )
    with open("java_test.java", "w") as f:
        f.write(
            """
import java.io.*;

public class java_test{
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(
            new InputStreamReader(System.in));
        System.out.println(in.readLine());
    }
}
            """.strip()
        )
    with open("c_test.c", "w") as f:
        f.write(
            """
#include <stdio.h>
int main()
{
    char str[255];
    scanf("%s", str);
    printf("%s", str);
}
            """.strip()
        )
    with open("cpp_test.cpp", "w") as f:
        f.write(
            """
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
    getline(cin, str);
    cout << str;
    return 0;
}
            """.strip()
        )
    if __name__ == "__main__":
        unittest.main()
