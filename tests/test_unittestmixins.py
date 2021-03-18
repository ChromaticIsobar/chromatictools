"""Tests for unittest mixins"""
import unittest
from chromatictools import unittestmixins


class TestAssertDoesntRaiseMixin(
  unittestmixins.AssertDoesntRaiseMixin,
  unittest.TestCase
):
  """Test the AssertDoesntRaiseMixin class"""
  def test_raise(self):
    """Test that the test fails if an exception is raised"""
    with self.assertRaises(AssertionError):
      with self.assert_doesnt_raise():
        raise Exception("Make the test fail!")

  def test_dont_raise(self):
    """Test that the test doesn't fail if an exception is not raised"""
    with self.assert_doesnt_raise():
      pass
