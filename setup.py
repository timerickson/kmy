from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'KMyMoney (.kmy) file parser'
LONG_DESCRIPTION = 'A simply library to read and provide typed access to KMyMoney data in .kmy files.' \
                   'It currently only supports readonly access.'

# Setting up
setup(
    # the name must match the folder name 'kmy'
    name="kmy",
    version=VERSION,
    author="Tim Erickson",
    author_email="<tim@timerickson.io>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'KMyMoney', 'kmy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Finance",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)