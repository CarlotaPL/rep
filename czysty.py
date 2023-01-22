from funkcje import *

def test_add():
    assert add(3,5) == 8
    assert add(120,43) == 163

def test_multiply():
    assert multiply(7,7) == 49

def test_fizzbuzz():
    assert fizzbuzz(1) ==1
    assert fizzbuzz(14)== 14
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(-7) == "Number out of range"
    assert fizzbuzz (4.62) == "Buzz"
    assert fizzbuzz("mama") == "Number out of range"