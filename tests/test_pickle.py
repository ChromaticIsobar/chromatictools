"""Tests for :mod:`chromatictools.pickle`"""
from chromatictools import unitdoctest, pickle


class DocTestPickle(metaclass=unitdoctest.DocTestMeta):
  """Doctests for :mod:`chromatictools.pickle`"""
  _modules = (pickle,)
