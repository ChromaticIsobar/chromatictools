"""Generate coverage badge URL from coverage report"""
from chromatictools import colors
import argparse
import json
from typing import Union


class HuePercentBadge:
  """Badge URL generator class based on mapping percentage to hue"""
  def __init__(
    self,
    label: str,
    hue_0: float = 0,
    hue_100: float = 130,
    hue_gamma: float = 1,
    saturation: float = 1,
    value: float = 1,
    fmt: str = "https://img.shields.io/badge/{label}-{message}-{color}",
  ):
    self.label = label
    self.hue_0 = hue_0
    self.hue_100 = hue_100
    self.hue_gamma = hue_gamma
    self.saturation = saturation
    self.value = value
    self.fmt = fmt

  @property
  def percent(self) -> Union[str, float]:
    return "N/A"

  @property
  def message(self) -> str:
    p = self.percent
    if not isinstance(p, str):
      p = "{:.0f}%25".format(p)
    return p

  @property
  def hue(self) -> float:
    """Color hue for the badge"""
    p = self.percent
    if isinstance(p, str):
      return self.hue_0
    p = (p / 100) ** self.hue_gamma
    return p * self.hue_100 + (1 - p) * self.hue_0

  @property
  def color(self) -> str:
    """Hexadecimal color string for the badge"""
    return colors.rgb2hex(
      *colors.hsv2rgb(
        self.hue,
        self.saturation,
        self.value
      )
    )

  @property
  def url(self) -> str:
    """Badge URL string"""
    return self.fmt.format(
      label=self.label,
      message=self.message,
      color=self.color,
    )

  def __str__(self) -> str:
    return self.url


class CoverageBadge(HuePercentBadge):
  """Coverage badge utility class"""
  def __init__(
    self,
    filename: str,
    label: str = "coverage",
    hue_gamma: float = 6,
    **kwargs,
  ):
    super().__init__(
      label=label,
      hue_gamma=hue_gamma,
      **kwargs
    )
    self.filename = filename

  @property
  def report(self) -> dict:
    """Coverage report dictionary"""
    try:
      with open(self.filename, "r") as f:
        d = json.load(f)
    except FileNotFoundError:
      d = {}
    return d

  @property
  def percent(self) -> Union[str, float]:
    """Coverage percentage if found in file, else :data:`"N/A"`"""
    return self.report.get("totals", {}).get("percent_covered", "N/A")


class PylintBadge(HuePercentBadge):
  """Pylint badge utility class"""
  def __init__(
    self,
    filename: str,
    label: str = "pylint",
    hue_gamma: float = 1,
    **kwargs,
  ):
    super().__init__(
      label=label,
      hue_gamma=hue_gamma,
      **kwargs
    )
    self.filename = filename

  @property
  def report(self) -> str:
    """Pylint report text file"""
    try:
      with open(self.filename, "r") as f:
        s = f.read()
    except FileNotFoundError:
      s = ""
    return s

  @property
  def percent(self) -> Union[str, float]:
    """Coverage percentage if found in file, else :data:`"N/A"`"""
    s = self.report
    prefix = "Your code has been rated at "
    if prefix not in s:
      return "N/A"
    return float(s.split(prefix, 1)[-1].split("/", 1)[0]) * 10

  @property
  def message(self) -> str:
    p = self.percent
    if not isinstance(p, str):
      p = "{:.2f}%2F10".format(p / 10)
    return p


if __name__ == "__main__":
  cmds = {
    "coverage": lambda a: CoverageBadge(a.coverage).url,
    "pylint": lambda a: PylintBadge(a.pylint).url,
  }
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    "cmd",
    help="Command. Should be in {}".format(list(cmds.keys()))
  )
  parser.add_argument(
    "-c",
    metavar="filename",
    dest="coverage",
    default="coverage.json",
    required=False,
    help="JSON coverage report filepath",
  )
  parser.add_argument(
    "-l",
    metavar="filename",
    dest="pylint",
    default="pylint.txt",
    required=False,
    help="Pylint report filepath",
  )
  args = parser.parse_args()
  print(cmds[args.cmd](args))
