import sys

from setuptools import setup

import mutpy

if sys.version_info < (3,8):
    print('MutPy-Pynguin requires Python 3.8 or newer!')
    sys.exit()

with open('requirements/production.txt') as f:
    requirements = f.read().splitlines()

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='MutPy-Pynguin',
    version=mutpy.__version__,
    python_requires='>=3.8',
    description='Mutation testing tool for Python 3.x source code.',
    long_description=long_description,
    author='Konrad Hałas',
    author_email='halas.konrad@gmail.com',
    maintainer='Stephan Lukasczyk',
    maintainer_email='stephan.lukasczyk@uni-passau.de',
    url='https://github.com/se2p/mutpy-pynguin',
    download_url='https://github.com/se2p/mutpy-pynguin',
    packages=['mutpy', 'mutpy.operators', 'mutpy.test_runners'],
    package_data={'mutpy': ['templates/*.html']},
    scripts=['bin/mut.py'],
    install_requires=requirements,
    extras_require={
        'pytest': ["pytest>=3.0"]
    },
    test_suite='mutpy.test',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
    ],
)
