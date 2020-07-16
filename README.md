# competester

## A python cli tool to test competitive programming solutions(code) against multiple test cases and measure execution time.

This tool comes handy when the programmer is dealing with a problem having
larger amount of test cases.

<img src="https://raw.githubusercontent.com/shaileshaanand/competester/master/docs/images/first.svg"/>

-   [INSTALLATION](#installation)
-   [DESCRIPTION & USAGE](#description-&-usage)
-   [TEST CASES FORMAT](#test-cases-format)
-   [OPTIONS](#options)
-   [COMPILATION](#compilation)
-   [BUILD INSTRUCTIONS](#build-instructions)
-   [TODO](#todo)

# INSTALLATION

To install it using [pip](https://pip.pypa.io/) (for Linux, MacOS and Windows users)

`sudo pip3 install --upgrade competest`

Alternatively, Windows users can download the latest competest.exe file from
[releases](https://github.com/shaileshaanand/competester/releases/tag/v0.0.4).

# DESCRIPTION & USAGE

competest is a command line program to test competitive coding problems for test cases. It requires python 3.6+ to be installed. It is licensed under GPL-v3 License.

As of now, supported Languages are:

-   C
-   C++
-   java
-   python
-   pypy
-   exe(i.e. compiled executables)

Usage:

```
competest [OPTIONS] [python|java|pypy|exe] PROGRAM_FILE

Example:
competest python program.py -t test_cases.json
```

# TEST CASES FORMAT

The test case file should contain all the test cases that you want to test your
code against.

Note: The test case format is decided based on the file extension so the file
extension must be `.txt` or `.json`.

## Test Cases can be written in 2 formats:

## 1. Test cases can be in .txt format like this

### Single Test Case:

```
5
3 2 4 5 6

2
12
```

Note: input is followed by output and separated by a blank line.

### Multiple Test Cases:

```
5
3 2 4 5 6

2
12

7
3 2 4 5 6 10 16

10
```

## Note: Each test case is also separated by a blank line.

## 2. Test cases can be in json format like this:

```
[
    {
        "input":[
            "5",
            "3 2 4 5 6"
        ],
        "output":[
            "2",
            "1 2"
        ]
    }
]
```

Note: `input` and `output` are arrays of strings where each string is a line of input/output

## For multiple test cases:

```
[
    {
        "input":[
            "5",
            "3 2 4 5 6"
        ],
        "output":[
            "2",
            "1 2"
        ]
    },
    {
        "input":[
            "7",
            "3 2 4 5 6 10 16"
        ],
        "output":["10"]
    }
]
```

[Find more about JSON](https://www.json.org)

# OPTIONS

```
 -t, --test-cases FILENAME          File containing test cases.  [required]

 -a, --compiler-args ARGUMENTS      command line arguments to be passed to
                                    compiler(for compiled languages only)

 -h, --help                         Show this message and exit.
```

# COMPILATION

You can pass extra arguments and flags to the compiler using `-a` option.
Don't pass `-o` flag to C/C++ compiler as it is not required and handled
by the tool itself.

### The default compilation commands are:

Java

```
javac classname.java
```

C

```
gcc -O2 -lm filename.c
```

C++

```
g++ -O2 -lm filename.cpp
```

# BUILD INSTRUCTIONS

To run competest directly use

```
python3 run.py
```

---

To run the tests use

```
python3 tests/test_platform.py
```

---

To build competest binary (install [pyinstaller](https://pypi.org/project/PyInstaller/) first)

```
pyinstaller -F run.py
```

# TODO

-   [x] ~~Add a simpler test case format~~
-   [ ] Improve Documentation
-   [x] ~~Add more metadata to setup.py~~
-   [ ] Add more language support

Made with ♥️ by [**Shailesh Aanand**](https://github.com/shaileshaanand/)
