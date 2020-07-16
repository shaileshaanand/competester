from .compilers_common import (
    java_compile_common,
    c_compile_common,
    cpp_compile_common
)
import subprocess


def java_compile(program_file):
    java_compile_common(program_file)
    subprocess.run(["javac", str(program_file)])


def c_compile(program_file):
    output_file = program_file.with_suffix(".exe")
    c_compile_common(str(program_file), str(output_file))
    return output_file


def cpp_compile(program_file):
    output_file = program_file.with_suffix(".exe")
    cpp_compile_common(str(program_file), str(output_file))
    return output_file
