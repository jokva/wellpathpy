import pytest
import numpy as np

from ..low_tan import low_tan_method

# inputs are array-like
def test_md_throws():
    with pytest.raises(TypeError):
        _ = low_tan_method(md='lmkcde', inc=[1,2,3], azi=[1,2,3])

def test_inc_throws():
    with pytest.raises(TypeError):
        _ = low_tan_method(md=[1,2,3], inc='adsda', azi=[1,2,3])

def test_azi_throws():
    with pytest.raises(TypeError):
        _ = low_tan_method(md=[1,2,3], inc=[1,2,3], azi='kjnef')

# inputs are same length
def test_input_lengths_throws():
    with pytest.raises(ZeroDivisionError):
        _ = low_tan_method(md=[1,2,3], inc=[1,2,3], azi=[1,2])

# inputs dtype are int or float
def test_md_dtype_throws():
    with pytest.raises(TypeError):
        _ = low_tan_method(md=['1','2','3'], inc=[1,2,3], azi=[1,2,3])

def test_inc_dtype_throws():
    with pytest.raises(TypeError):
        _ = low_tan_method(md=[1,2,3], inc=['1','2','3'], azi=[1,2,3])

def test_azi_dtype_throws():
    with pytest.raises(TypeError):
        _ = low_tan_method(md=[1,2,3], inc=[1,2,3], azi=['1','2','3'])

# md array increases strictly at each step
def test_increasing_md_throws():
    with pytest.raises(ZeroDivisionError):
        _ = low_tan_method(md=[1,1,3], inc=[1,2,3], azi=[1,2,3])