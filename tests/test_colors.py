"""Test color utilities"""
from chromatictools import colors
import unittest


references = (
  ("black", (0, 0, 0), (0, 0, 0), "000000"),
  ("white", (0, 0, 1), (255, 255, 255), "ffffff"),
  ("red", (0, 1, 1), (255, 0, 0), "ff0000"),
  ("green", (120, 1, 1), (0, 255, 0), "00ff00"),
  ("blue", (240, 1, 1), (0, 0, 255), "0000ff"),
)


class TestColors(unittest.TestCase):
  """Test for colors module"""
  def test_hsv2rgb(self):
    """Test hsv2rgb conversion"""
    for k, hsv, rgb, _ in references:
      with self.subTest(color=k):
        self.assertEqual(colors.hsv2rgb(*hsv), rgb)

  def test_rgb2hex(self):
    """Test rgb2hex conversion"""
    for k, _, rgb, h in references:
      with self.subTest(color=k):
        self.assertEqual(colors.rgb2hex(*rgb), h)
