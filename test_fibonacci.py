# FIBONACCI ASSIGNMENT

from fibonacci import fibo

# my 6 list of fibonacci numbers to use  0,1,1,2,3,5

# The first fibo number can be a 0, but we ignored it
# def test_fibonacci_0():
#     assert fibo(0) == []
 
def test_fibonacci_1():
    assert fibo(1) == [0]
# THis test FAILED, no fibo function to use
#  To PASS the test we created a fibo function to use in assert, and imported

# Second Test
def test_fibonacci_2():
    assert fibo(2) == 1

# Third Test
def test_fibonacci_3():
    assert fibo(3) == 1