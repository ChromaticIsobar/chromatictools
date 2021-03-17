"""Tests for the CLI decorator"""
import unittest
from unittest import mock
from chromatictools import cli


def foo():
  """Dummy function. Return value is checked as call argument
  to :func:`sys.exit` in the test"""
  return 0


class TestCli(unittest.TestCase):
  """Test the CLI decorator"""
  def test_main(self):
    """Test execution as main function"""
    with mock.patch.object(cli.sys, "exit") as mock_exit:
      cli.main("__main__")(foo)
      self.assertEqual(mock_exit.call_args[0][0], 0)

  def test_not_main(self):
    """Test execution not as main function"""
    self.assertEqual(cli.main("name")(foo), foo)
