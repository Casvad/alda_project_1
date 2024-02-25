# About this repo

Project with 3 searching algorithms, linear, binary and ternary

## Linear sort

Time complexity: `O(n)`

## Binary sort

Time complexity: `O(log(n))`

## Ternary sort

Time complexity: `O(2 * log3(n))`

---

# Python version
Python 3.11.0

# Running locally and testing

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Check coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. 
Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```shell
Name                             Stmts   Miss  Cover
----------------------------------------------------
base/__init__.py                     0      0   100%
base/test/__init__.py                0      0   100%
binary/__init__.py                   0      0   100%
binary/algorithm.py                 11      0   100%
binary/test/__init__.py              0      0   100%
binary/test/test_algorithm.py       11      1    91%
linear/__init__.py                   0      0   100%
linear/algorithm.py                  5      0   100%
linear/test/__init__.py              0      0   100%
linear/test/test_algorithm.py       11      1    91%
ternary/__init__.py                  0      0   100%
ternary/algorithm.py                14      0   100%
ternary/test/__init__.py             0      0   100%
ternary/test/test_algorithm.py      11      1    91%
utils/__init__.py                    0      0   100%
utils/constants_test.py              2      0   100%
----------------------------------------------------
TOTAL                               65      3    95%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.

# Searching performance


