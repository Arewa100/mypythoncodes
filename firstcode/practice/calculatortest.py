import calculatorfunctions
import pytest

def test_addition_function():
	assert calculatorfunctions.add(2, 2) == 4

def test_division_function():
	with pytest.raises(ZeroDivisionError) as excinfo:
		calculatorfunctions.divide(1, 0)
	assert str(excinfo.value) == "Division by zero is not allowed"