"""Mixin classes for unittests"""
import contextlib
import io


class AssertPrintsMixin:
  """Mixin class for print assertion"""
  @contextlib.contextmanager
  def assert_prints(self, target: str):
    """Assert that contextual code prints the target string.
    Use as context manager

    Args:
      target (str): Print expectation"""
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
      yield
      printed = buf.getvalue()
    self.assertEqual(printed, target)


class AssertDoesntRaiseMixin:
  """Mixin class for "doesn't-raise" assertion"""
  @contextlib.contextmanager
  def assert_doesnt_raise(self):
    """Assert that contextual code doesn't raise any exception
    Use as context manager"""
    try:
      yield
    except Exception as e:
      raise AssertionError from e
