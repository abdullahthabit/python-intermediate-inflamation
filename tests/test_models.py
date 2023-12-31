"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_min_negatives():
    """Test that max function works for an array of negative integers."""
    from inflammation.models import daily_min

    test_input = np.array([[-1, -2],
                           [-3, -4],
                           [-5, -6]])

    test_result = np.array([-5, -6])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """Test for type error when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'There'], ['General', 'Kenobi']])

@pytest.mark.parametrize("test, expected",
                         [
                             ([[0, 0], [0, 0], [0, 0]], [0, 0]),
                             ([[1, 2], [3, 4], [5, 6]], [3, 4])
                         ])
def test_daily_mean(test, expected):
    """Test mean functions works for array of zeros and positive integers"""

    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize("test, expected",
                         [
                             ([[-1, -2], [-3, -4], [-5, -6]], [-1, -2]),
                             ([[1, 2], [3, 4], [5, 6]], [5, 6])
                         ])
def test_daily_max(test, expected):
    "Test max function for arrays of negative and positive values"

    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize("test, expected",
                         [
                             ([[0, 0], [0, 0], [0, 0]], [0, 0]),
                             ([[-1, -1], [-1, -1], [-1, -1]], [0, 0])
                         ])
def test_daily_std(test, expected):
    "Test max function for arrays of negative and positive values"

    from inflammation.models import daily_std
    npt.assert_array_equal(daily_std(np.array(test)), np.array(expected))
