"""Tests for :mod:`chromatictools.pickle`"""
from chromatictools import unitdoctest, pickle
import unittest
import shutil
import os


class DocTestPickle(metaclass=unitdoctest.DocTestMeta):
  """Doctests for :mod:`chromatictools.pickle`"""
  _modules = (pickle,)


class TestPickle(unittest.TestCase):
  """Tests for :mod:`chromatictools.pickle`"""
  def test_makedirs(self):
    """Test that a new directory is created automatically when pickling"""
    cache_file = "pickled_example/saved"
    cache_dir = os.path.dirname(cache_file)
    with self.subTest(step="check directory doesn't exist"):
      self.assertFalse(os.path.exists(cache_dir))
    pickle.save_pickled({"data": 8}, cache_file)
    with self.subTest(step="check directory has been created"):
      self.assertTrue(os.path.exists(cache_dir))
    os.remove(cache_file)
    shutil.rmtree(cache_dir)

  def test_property_version(self):
    """Test pickle cache decorator with properties"""
    class Cached:
      def __init__(self, name, path="cached_name"):
        self.name = name
        self._path = path

      @property
      def path(self):
        return self._path

      @pickle.pickled_cache(path)
      def echo(self):
        return self.name

    with self.subTest(step="check echo is the same"):
      self.assertEqual(Cached("Alice").echo(), "Alice")
    with self.subTest(step="check echo is the previous"):
      self.assertEqual(Cached("Bob").echo(), "Alice")
    os.remove(Cached(None).path)

  def test_raise_not_implemented(self):
    """Test that NotImplementedError is raise for unsupported types"""
    ex = None
    try:
      @pickle.pickled_cache(None)
      def echo(s):
        return s
    except NotImplementedError as e:
      ex = e
      msg = str(e)
    else:
      msg = "No exceptions raised"
    self.assertTrue(isinstance(ex, NotImplementedError), msg=msg)
