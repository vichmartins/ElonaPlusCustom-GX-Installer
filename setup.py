from setuptools import setup

setup(
    name="elonadl",
    version="0.0.3",
    author="VH-Martins",
    packages=["elonadl"],
    description="ElonaPlusCGXDownload",
    long_description="Quick script to download and setup Elona+CGX",
    python_requires='>=3.10',
    install_requires=['py7zr', 'requests']
)
