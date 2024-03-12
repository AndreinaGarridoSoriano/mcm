"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from mcm import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='scipion-em-mcm',  # Required
    version=3,  # Required
    description='Scipion plugin MCM.',  # Required
    long_description=long_description,  # Optional
    url='https://github.com:AndreinaGarridoSoriano/mcm.git',  # Optional
    author='Andreina',  # Optional
    author_email='andreinagarrido11@gmail.com',  # Optional
    keywords='scipion cryoem imageprocessing scipion-3.0',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    install_requires=[requirements],
    project_urls={},
    entry_points={'pyworkflow.plugin': 'mcm = mcm'},
    package_data={  # Optional
       'mcm': ['icon.png', 'protocols.conf'],
    }
)
