# Task 1
## python -m doctest -v -o NORMALIZE_WHITESPACE main.py:
```Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode ('MSU')
Expecting:
     '-- ... ..-'
ok
Trying:
    encode ('MIT IS BETTER THAN HSE') # doctest: +ELLIPSIS
Expecting:
    '-- .. - ... .... ... .'
ok
Trying:
    encode('help')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'h'
ok
2 items had no tests:
    main
    main.decode
1 items passed all tests:
   4 tests in main.encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
```
## python -m doctest -v main.py

```Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode ('MSU')
Expecting:
     '-- ... ..-'
**********************************************************************
File "C:\Users\alexa\PycharmProjects\HW_Tests\main.py", line 35, in main.encode
Failed example:
    encode ('MSU')
Expected:
     '-- ... ..-'
Got:
    '-- ... ..-'
Trying:
    encode ('MIT IS BETTER THAN HSE') # doctest: +ELLIPSIS
Expecting:
    '-- .. - ... .... ... .'
ok
Trying:
    encode('help')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'h'
ok
2 items had no tests:
    main
    main.decode
**********************************************************************
1 items had failures:
   1 of   4 in main.encode
4 tests in 3 items.
3 passed and 1 failed.
***Test Failed*** 1 failures.
```
# Task 2
## python -m pytest main.py

```collected 3 items                                                                                                                                                                       

main.py ..F                                                                                                                                                                       [100%]

======================================================================================= FAILURES =======================================================================================
__________________________________________________________ test_decode[.-.. --- -. --.   . ...- . -. .. -. --.-LONG EVENING] ___________________________________________________________

code = '.-.. --- -. --.   . ...- . -. .. -. --.', message = 'LONG EVENING'

    @pytest.mark.parametrize('code,message', [
        ('... --- ...', 'SOS'),
        ('.- -... -.-.', 'ABC'),
        ('.-.. --- -. --.   . ...- . -. .. -. --.', 'LONG EVENING')
    ])
    def test_decode(code, message):
>       assert decode(code) == message, f'expected {message}, got {decode(code)}'
E       AssertionError: expected LONG EVENING, got LONGEVENING
E       assert 'LONGEVENING' == 'LONG EVENING'
E         - LONG EVENING
E         ?     -
E         + LONGEVENING

main.py:68: AssertionError
=============================================================================== short test summary info ================================================================================
FAILED main.py::test_decode[.-.. --- -. --.   . ...- . -. .. -. --.-LONG EVENING] - AssertionError: expected LONG EVENING, got LONGEVENING
============================================================================= 1 failed, 2 passed in 0.05s ==============================================================================
PS C:\Users\alexa\PycharmProjects\HW_Tests>
```

# Task 3
## python -m unittest -v fit.py
```
PS C:\Users\alexa\PycharmProjects\HW_testing>  python -m unittest -v fit.py
test_argless (fit.Test_fit) ... ok
test_empty (fit.Test_fit) ... ok
test_encoding (fit.Test_fit) ... ok
test_single (fit.Test_fit) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
# Task 4
## python -m pytest -v py_fit.py
```
================================================================================= test session starts ==================================================================================
platform win32 -- Python 3.9.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- C:\Users\alexa\PycharmProjects\HW_fit\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\alexa\PycharmProjects\HW_fit
collected 5 items                                                                                                                                                                       

py_fit.py::test_fit_transform[vector0-expected0] PASSED                                                                                                                           [ 20%]
py_fit.py::test_fit_transform[vector1-expected1] PASSED                                                                                                                           [ 40%]
py_fit.py::test_argless PASSED                                                                                                                                                    [ 60%]
py_fit.py::test_single PASSED                                                                                                                                                     [ 80%]
py_fit.py::test_empty PASSED                                                                                                                                                      [100%]

================================================================================== 5 passed in 0.02s ===================================================================================
```
# Task 5
## coverage run -m pytest -v Tic-Tac.py
```
================================================================================= test session starts ==================================================================================
platform win32 -- Python 3.9.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- c:\users\alexa\pycharmprojects\tic-tac\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\alexa\PycharmProjects\Tic-Tac
collected 2 items                                                                                                                                                                       

Tic-Tac.py::test_raise_exception PASSED                                                                                                                                           [ 50%]
Tic-Tac.py::test_year PASSED                                                                                                                                                      [100%]

================================================================================== 2 passed in 0.09s ===================================================================================

```
