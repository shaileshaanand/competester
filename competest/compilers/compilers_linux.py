from .compilers_common import (
    java_compile_common,
    c_compile_common,
    cpp_compile_common
)
import subprocess


def java_compile(program_file):
    java_compile_common(program_file)
    subprocess.run(["javac", program_file])


def c_compile(program_file):
    output_file = program_file.with_suffix("")
    c_compile_common(program_file, output_file)
    return output_file


def cpp_compile(program_file):
    output_file = program_file.with_suffix("")
    cpp_compile_common(program_file, output_file)
    return output_file
