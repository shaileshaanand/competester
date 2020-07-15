import json


def parse_cases_json(test_case_file):
    test_cases = json.loads(test_case_file.read())
    return test_cases


def parse_cases_txt(test_case_file):
    test_cases = []
    cases = [x.strip() for x in test_case_file.read().split("\n\n")]
    for i in range(0, len(cases), 2):
        test_cases.append(
            {"input": cases[i].split("\n"), "output": cases[i+1].split("\n")})
    return test_cases
