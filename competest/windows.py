import subprocess
import pathlib
from click import BadParameter


def python(program_file, input_data):
    return subprocess.run(["python", str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def pypy(program_file, input_data):
    return subprocess.run(["pypy", str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def java(program_file, input_data):
    program_file = pathlib.Path(program_file).resolve()
    if program_file.suffix != ".java":
        raise BadParameter(
            f"for java PROGRAM_FILE extention should be .java not {program_file.suffix}")
    classname = program_file.stem
    program_path = program_file.parent
    subprocess.run(["javac", str(program_file)])
    return subprocess.run(["java", "-classpath", str(program_path), classname],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def exe(program_file, input_data):
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)
