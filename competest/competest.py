import click
import sys
import pathlib
from time import time
from click import BadParameter
from .parsers import parse_cases_json, parse_cases_txt
if sys.platform == "linux":
    from .compilers.compilers_linux import (
        java_compile,
        c_compile,
        cpp_compile
    )
    from .linux import (
        python,
        java,
        pypy,
        exe,
        c,
        cpp
    )
elif sys.platform == "win32":
    from .compilers.compilers_windows import (
        java_compile,
        c_compile,
        cpp_compile
    )
    from .windows import (
        python,
        java,
        pypy,
        exe,
        c,
        cpp
    )
else:
    raise Exception


@click.command("competest",
               context_settings={
                   "help_option_names": ['-h', '--help']
               })
@click.argument("language",
                type=click.Choice(
                    ["python", "java", "pypy", "c", "cpp", "exe"]),
                required=True)
@click.argument("program_file",
                type=click.Path(exists=True),
                required=True)
@click.option("--test-cases", "-t",
              type=click.File("r"),
              help="File containing test cases.",
              required=False)
@click.option("--compiler-args", "-a")
def competest(language, program_file, test_cases, compiler_args):
    """Run PROGRAM_FILE with test cases from the PROGRAM_FILE.txt or
    PROGRAMFILE.json file or from the file specified in --test-cases (or -t)
    option and check them against the correct output specified in the
    same file.

       Supported Languages: java, python, pypy and exe(i.e. compiled
       executables)"""
    main(language, program_file, test_cases, compiler_args)


def main(language, program_file, test_cases_in, compiler_args):
    program_file = pathlib.Path(program_file).resolve()

    if test_cases_in is None:
        if program_file.with_suffix(".txt").exists():
            test_cases_in = open(program_file.with_suffix(".txt"), 'r')
        elif program_file.with_suffix(".json").exists():
            test_cases_in = open(program_file.with_suffix(".json"), 'r')
        else:
            raise BadParameter("Test case file is missing. Please use -t")

    test_cases = get_test_cases(test_cases_in)
    test_cases_in.close()
    if test_cases == "error":
        raise BadParameter(
            "invalid testcase file extension, should be .json or .txt")
    file_to_run = compile_if_needed(program_file, language, compiler_args)
    total_cases = len(test_cases)
    failed_cases = 0
    languages = {
        "python": python,
        "java": java,
        "pypy": pypy,
        "exe": exe,
        "c": c,
        "cpp": cpp
    }

    for i, test_case in enumerate(test_cases, 1):
        input_data = "\n".join(test_case["input"]).encode()
        required_output = "\n".join(test_case["output"])
        start_time = time()
        process = languages[language](file_to_run, input_data)
        time_taken = time() - start_time
        actual_output = process.stdout.decode().strip().replace('\r', '')
        if process.returncode == 0 and required_output == actual_output:
            click.echo(
                f"Test Case {i} Passed and took {time_taken:.3f} seconds  ✅")
        else:
            failed_cases += 1
            click.echo(f"Test Case {i} Failed ❎")
            if process.returncode == 0:
                click.echo(
                    f"Required Output:\n{required_output}\n---------------")
                click.echo(
                    f"Actual Output:\n{actual_output}\n---------------\n(took {time_taken:.3f} seconds)\n")
            else:
                click.echo("---------------")
                click.echo(f"Runtime Error: (took {time_taken:.3f} seconds)")
                click.echo(process.stderr.decode().strip())
                click.echo("---------------\n")

    if failed_cases == 0:
        click.echo("All tests passed successfully. ✅")
    else:
        click.echo(f"{failed_cases}/{total_cases} Test Cases Failed ❎")


def get_test_cases(tests_file):
    if tests_file.name.endswith(".json"):
        test_cases = parse_cases_json(tests_file)
    elif tests_file.name.endswith(".txt"):
        test_cases = parse_cases_txt(tests_file)
    else:
        return "error"
    return test_cases


def compile_if_needed(program_file, language, compiler_args):
    file_to_run = program_file
    if language == "java":
        java_compile(program_file, compiler_args)
        file_to_run = program_file.with_suffix(".class")
    elif language == "c":
        file_to_run = c_compile(program_file, compiler_args)
    elif language == "cpp":
        file_to_run = cpp_compile(program_file, compiler_args)

    return file_to_run
