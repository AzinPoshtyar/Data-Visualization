from codecs import open
from os import path

from setuptools import find_packages, setup


def get_long_description():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


def get_version():
    version_filepath = path.join(path.dirname(__file__), "chat2plot", "version.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.strip().split()[-1][1:-1]


def requirements_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="datavis",
    packages=find_packages(),
    version=get_version(),
    license="MIT",
    install_requires=requirements_from_file("requirements.txt"),
    ppppppppppppppppp
    description="Data table visualization with LLM",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="llm-based data visualization",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
