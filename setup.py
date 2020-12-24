from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'KMyMoney (.kmy) file parser'
URL = 'https://github.com/timerickson/kmy'
LONG_DESCRIPTION = 'A simply library to read and provide typed access to KMyMoney data in .kmy files.' \
                   'It currently only supports readonly access.'

# Setting up
setup(
    name="kmy",
    version=VERSION,
    url=URL,
    author="Tim Erickson",
    author_email="<tim@timerickson.io>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'KMyMoney', 'kmy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)