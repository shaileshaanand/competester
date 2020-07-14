import subprocess
from click import BadParameter


def python(program_file, input_data):
    return subprocess.run(["python3", program_file],
                          input=input_data,
                          capture_output=True)


def pypy(program_file, input_data):
    return subprocess.run(["pypy3", program_file],
                          input=input_data,
                          capture_output=True)


def java(program_file, input_data):
    if program_file.suffix != ".java":
        raise BadParameter(
            f"for java PROGRAM_FILE extention should be .java not {program_file.suffix}")
    classname = program_file.stem
    program_path = program_file.parent
    subprocess.run(["javac", program_file])
    return subprocess.run(["java", "-classpath", program_path, classname],
                          input=input_data,
                          capture_output=True)


def exe(program_file, input_data):
    return subprocess.run([program_file],
                          input=input_data,
                          capture_output=True)
