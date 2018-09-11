import pytest
from calculadora import soma


def test_soma ():
	assert soma (1, 1) == 2
	assert soma (3, 2) == 5
	assert soma ('-2', '-3') == -5
	assert soma (5, 5) == 10
	assert soma ('n', 'o') == None 
	assert soma ('-1', 'y') == None
	assert soma ('cinco', 'um') == None
