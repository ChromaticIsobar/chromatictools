import setuptools


with open("README.md", "r") as f:
  readme = f.read()
with open("chromatictools/__init__.py", "r") as f:
  version = f.read().split("__version__ = \"", 1)[-1].split("\"", 1)[0]


setuptools.setup(
  name="chromatictools",
  version=version,
  author="Marco Tiraboschi",
  author_email="marco.tiraboschi@unimi.it",
  maintainer="Marco Tiraboschi",
  maintainer_email="marco.tiraboschi@unimi.it",
  description="chromatictools",
  long_description=readme,
  long_description_content_type="text/markdown",
  url="https://github.com/ChromaticIsobar/chromatictools",
  packages=setuptools.find_packages(
    include=["chromatictools", "chromatictools.*"]
  ),
  include_package_data=True,
  setup_requires=[
    "wheel",
  ],
  install_requires=[
    "requests",
    "numpy",
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.6",
)
