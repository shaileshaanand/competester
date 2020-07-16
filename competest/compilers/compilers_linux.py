from .compilers_common import (
    java_compile_common,
    c_compile_common,
    cpp_compile_common
)
import subprocess
import shlex


def java_compile(program_file, compiler_args):
    java_compile_common(program_file)
    if compiler_args:
        subprocess.run(["javac", *shlex.split(compiler_args), program_file])
    else:
        subprocess.run(["javac", program_file])


def c_compile(program_file, compiler_args):
    output_file = program_file.with_suffix("")
    c_compile_common(program_file, output_file, compiler_args)
    return output_file


def cpp_compile(program_file, compiler_args):
    output_file = program_file.with_suffix("")
    cpp_compile_common(program_file, output_file, compiler_args)
    return output_file
