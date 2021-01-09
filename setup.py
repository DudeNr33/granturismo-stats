"""
Setup script for gtsport-stats.
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
        "matplotlib",
        "cached-property",
    ],
    extras_require={
        "tests": [
            "pytest",
            "requests-mock",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.5'
)
