"""Test badges utilities"""
from chromatictools import badges, unittestmixins
import unittest
import json
import os


class TestCoverage(unittestmixins.AssertPrintsMixin, unittest.TestCase):
  """Tests for coverage badge"""
  filename = "_coverage.json"

  @classmethod
  def setUpClass(cls):
    """Create fake report file"""
    with open(cls.filename, "w") as f:
      json.dump(dict(totals=dict(percent_covered=100.0)), f)

  def test_na(self):
    """Test N/A when file is not found"""
    with self.assert_prints(
      "https://img.shields.io/badge/coverage-N/A-d80000\n"
    ):
      badges.main("coverage", "-c", "_v_i__fq_ph")

  def test_100(self):
    """Test 100% coverage"""
    with self.assert_prints(
      "https://img.shields.io/badge/coverage-100%25-00d824\n"
    ):
      badges.main("coverage", "-c", self.filename)

  @classmethod
  def tearDownClass(cls):
    """Delete fake report file"""
    os.remove(cls.filename)


class TestPylint(unittestmixins.AssertPrintsMixin, unittest.TestCase):
  """Tests for pylint badge"""
  filename = "_pylint.txt"

  @classmethod
  def setUpClass(cls):
    """Create fake report file"""
    with open(cls.filename, "w") as f:
      f.write("Your code has been rated at 10.00/10")

  def test_na(self):
    """Test N/A when file is not found"""
    with self.assert_prints(
      "https://img.shields.io/badge/pylint-N/A-d80000\n"
    ):
      badges.main("pylint", "-l", "_v_i__fq_ph")

  def test_100(self):
    """Test 100% coverage"""
    with self.assert_prints(
      "https://img.shields.io/badge/pylint-10.00%2F10-00d824\n"
    ):
      badges.main("pylint", "-l", self.filename)

  @classmethod
  def tearDownClass(cls):
    """Delete fake report file"""
    os.remove(cls.filename)
