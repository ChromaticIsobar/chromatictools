"""Test purgithub CLI tool"""
import unittest
import contextlib
import io
from chromatictools import purgithub


class TestPurgithub(unittest.TestCase):
  """Test purgithub cli tool"""
  def test_purge_repo_home(self):
    """Test on repo home"""
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
      purgithub.main("https://github.com/ChromaticIsobar/chromatictools")
