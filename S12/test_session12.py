import pytest
import os
import inspect
import re
import math

#os.chdir(r'C:\Users\bhaga\Documents\EPAI\S12')
import calculator
from calculator import derivatives

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_sin():
    assert math.sin(15) == calculator.sin(15)

def test_cos():
    assert math.cos(5) == calculator.cos(5)

def test_tan():
    assert math.tan(10) == calculator.tan(10)

def test_tanh():
    assert math.tanh(10) == calculator.tanh(10)

def test_softmax():
    assert calculator.softmax(5) == 1.0

def test_sigmoid():
    assert [0.8807970779778823, 0.11920292202211755] == list(calculator.softmax([5,3]))

def test_relu():
    assert max(0, -2) == calculator.relu(-2)

def test_log():
    assert math.log(10) == calculator.log(10)

def test_exp():
    assert math.exp(10) == calculator.exp(10)

def test_sin_diff():
    assert derivatives.sin_diff(15) == -0.7596879128588213

def test_cos_diff():
    assert derivatives.cos_diff(15) == -0.6502878401571168

def test_tan_diff():
    assert derivatives.tan_diff(15) == 0.2672752976010677

def test_tanh_diff():
    assert derivatives.tanh_diff(15) == 3.743672039036028e-13

def test_sigmoid_diff():
    assert derivatives.sigmoid_diff(15) == 3.0590213341738715e-07

def test_relu_diff():
    assert derivatives.relu_diff(15) == 1

def test_log_diff():
    assert derivatives.log_diff(15) == 0.06666666666666667

def test_exp_diff():
    assert derivatives.exp_diff(15) == 3269017.3724721107