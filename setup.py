"""
Demo of how types in python and classes are only loosely coupled.

This package contains extremely weird dangerous nonsence.
Do not teach this to you programmers.
"""
from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='crea-meta',
    # extract version from module.
    version=__version__,
    description="Some creative examples of metaclasses in python",
    long_description=__doc__,
    classifiers=[],
    keywords='useless nonesence metaclass wizzardy pythonista',
    author='Lars van de Kerkhof',
    author_email='lars@permanentmarkers.nl',
    url='',
    license='GPL',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # for avoiding conflict have one namespace for all apc related eggs.
    namespace_packages=[],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
    ],
    # mark test target to require extras.
    extras_require = {
        'test':  ["mock"]
    },
    # generate scripts
    entry_points={
        'console_scripts':[
            'crea-meta = creameta.crea:main',
        ]
    },
)
