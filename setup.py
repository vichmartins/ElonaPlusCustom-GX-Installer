from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="elonadl",
    version="0.1.9",
    author="vichmartins",
    packages=["elonadl"],
    description="ElonaPlusCGXDownload",
    long_description="Installs the latest version of Elona+CGX (Windows Only Currently)",
    python_requires='>=3.10',
    install_requires=['pywin32', 'requests', 'winshell']
)
