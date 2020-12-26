from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements_dev.txt", "r") as requirement_file:
    requirements = requirement_file.read()

setup(
    name="pyCalc",
    version="0.0.1",
    author="Amedeo Fortino",
    author_email="amedeo.fortino@gmail.com",
    description="A test package that implements a full-optional calculator",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Kale-gz/pyCalc/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9.1",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)