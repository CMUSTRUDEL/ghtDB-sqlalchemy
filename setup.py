import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package = 'ghtdb_sqlalchemy_cmustrudel'

setuptools.setup(
    name="strudel.ghtdb",
    version="0.0.1",
    author="Bogdan Vasilescu",
    author_email="vasilescu@gmail.com",
    description="GHTorrent SQLAlchemy mappings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CMUSTRUDEL/ghtDB-sqlalchemy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)