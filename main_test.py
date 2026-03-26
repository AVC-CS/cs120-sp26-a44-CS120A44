import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # input=1: output must show menu 1 selected
    content = open('result1.txt').read()
    print(content)
    regex_test([r'[Mm]enu\s+1\s+selected'], content)

@pytest.mark.T2
def test_main_2():
    # input=2: output must show menu 2 selected
    content = open('result2.txt').read()
    print(content)
    regex_test([r'[Mm]enu\s+2\s+selected'], content)

@pytest.mark.T3
def test_main_3():
    # input=3: output must show menu 3 selected
    content = open('result3.txt').read()
    print(content)
    regex_test([r'[Mm]enu\s+3\s+selected'], content)

@pytest.mark.T4
def test_main_4():
    # input=4: output must show menu 4 selected
    content = open('result4.txt').read()
    print(content)
    regex_test([r'[Mm]enu\s+4\s+selected'], content)
