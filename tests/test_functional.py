"""Tests for function utilities"""
import unittest
from chromatictools import functional
from typing import Type, Optional


def _foo(c: Optional[Type[Exception]] = None):
  """Dummy function"""
  if c is None:
    return True
  raise c()


class TestRecast(unittest.TestCase):
  """Tests for exception recasting"""
  def test_recast_exception(self):
    """Test recast of single exception type"""
    foo = functional.recast_exception(ValueError, RuntimeError)(_foo)
    with self.subTest(recast=True):
      with self.assertRaises(RuntimeError):
        foo(ValueError)
    with self.subTest(recast=False):
      with self.assertRaises(FileNotFoundError):
        foo(FileNotFoundError)
    with self.subTest(raise_=False):
      self.assertTrue(foo())

  def test_recast_exceptions(self):
    """Test recast of multiple exception types"""
    clss = (ValueError, OverflowError, ModuleNotFoundError)
    foo = functional.recast_exception(clss, RuntimeError)(_foo)
    for c in clss:
      with self.subTest(exc=c, recast=True):
        with self.assertRaises(RuntimeError):
          foo(c)
    with self.subTest(recast=False):
      with self.assertRaises(FileNotFoundError):
        foo(FileNotFoundError)
    with self.subTest(raise_=False):
      self.assertTrue(foo())
