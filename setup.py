import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dglogger",
    version="0.0.2",
    author="David G.",
    author_email="dgabbe@acm.org",
    description="Logging utility for development & production",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgabbe/dglogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development",
        "Topic :: System :: Logging",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
