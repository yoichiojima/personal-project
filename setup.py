from setuptools import setup
from setuptools import find_packages

setup(
    name="personal-project-libs",
    version="0.1.0",
    description="Personal project libs",
    author="Yoichi Ojima",
    packages=find_packages("libs"),
    package_dir={"": "libs"},
)
