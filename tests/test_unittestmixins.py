"""Tests for unittest mixins"""
import unittest
from chromatictools import unittestmixins
import numpy as np


class TestAssertDoesntRaiseMixin(
  unittestmixins.AssertDoesntRaiseMixin,
  unittest.TestCase
):
  """Test the :class:`AssertDoesntRaiseMixin` class"""
  def test_raise(self):
    """Test that the test fails if an exception is raised"""
    with self.assertRaises(AssertionError):
      with self.assert_doesnt_raise():
        raise Exception("Make the test fail!")

  def test_dont_raise(self):
    """Test that the test doesn't fail if an exception is not raised"""
    with self.assert_doesnt_raise():
      pass


class TestSingificantPlaces(
  unittestmixins.SignificantPlacesAssertMixin,
  unittest.TestCase
):
  """Test the :class:`SignificantPlacesAssertMixin` class"""
  def test_significant_places_ok(self):
    """Test the significant places assertion"""
    self.assert_almost_equal_significant(.000541, .000542, places=1)

  def test_significant_places_fail(self):
    """Test the significant places assertion when it fails"""
    with self.assertRaises(AssertionError):
      self.assert_almost_equal_significant(.000541, .000542, places=2)

  def test_significant_places_zeros(self):
    """Test the significant places assertion on zeros"""
    self.assert_almost_equal_significant(.0, -.000, places=7)


class TestRMSE(
  unittestmixins.RMSEAssertMixin,
  unittest.TestCase
):
  """Test the :class:`RMSEAssertMixin` class"""
  def test_rmse_almost(self):
    """Test RMSE "almost-equal" assertion"""
    x = np.linspace(0, 100, 1024)
    np.random.seed(42)
    y = x + np.random.randn(*x.shape) * 0.01
    self.assert_almost_equal_rmse(x, y, places=1)

  def test_rmse(self):
    """Test RMSE assertion"""
    x = np.linspace(0, 100, 1024)
    self.assert_equal_rmse(x, x)
