"""Test import utilities"""
from chromatictools import imports
import types
import unittest


class TestImports(unittest.TestCase):
  """Test import utilities"""
  def test_import_success(self):
    """Test module imports correctly"""
    self.assertTrue(isinstance(
      imports.import_if_installed("math"),
      types.ModuleType
    ))

  def test_import_fail(self):
    """Test that a :class:`ModuleNotFoundError` is returned"""
    self.assertTrue(isinstance(
      imports.import_if_installed("sjèò+jljks"),
      ModuleNotFoundError
    ))
