import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HTML-table-scraper-SheehabX",
    version="0.0.1",
    author="Muhammad Sheehab",
    author_email="SheehabX@gmail.com",
    description="A python package that can extract data from HTML tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SheehabX/HTML-Table-Scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)