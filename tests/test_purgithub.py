"""Test purgithub CLI tool"""
import unittest
import contextlib
import io
from chromatictools import purgithub, unittestmixins


class TestPurgithub(
  unittestmixins.AssertPrintsMixin,
  unittest.TestCase
):
  """Test purgithub cli tool"""
  def test_purge_repo_home(self):
    """Test on repo home"""
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
      purgithub.main("https://github.com/ChromaticIsobar/chromatictools")

  def test_purge_repo_home_quiet_mode(self):
    """Test on repo home with quiet mode on"""
    with self.assert_prints(""):
      purgithub.main(
        "--quiet",
        "https://github.com/ChromaticIsobar/chromatictools"
      )
