"""
Setup script for granturismo-stats.
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION.txt", "r") as fh:
    version = fh.read().strip()

with open("CHANGELOG.md", "r") as fh:
    changelog = fh.read()


setuptools.setup(
    name="granturismo-stats",
    version=version,
    author="Andreas Finkler",
    author_email="andi.finkler@gmail.com",
    description="Retrieve statistics for Gran Turismo Sport",
    long_description=long_description + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    url="https://github.com/DudeNr33/granturismo-stats",
    packages=setuptools.find_packages(where="src"),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "requests",
        "numpy",
        "dataclasses; python_version<'3.7'",
    ],
    extras_require={
        "dev": [
            "tox",
            "setuptools",
            "wheel",
            "twine",
            "check-manifest",
        ],
        "tests": [
            "coverage",
            "pylint",
            "pytest",
            "pytest-cov",
            "pytest-pylint",
            "requests-mock",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Simulation",
    ],
    python_requires='>=3.5'
)
