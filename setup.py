from setuptools import setup

setup(
    name='kraken_helper',
    version='1.0',
    description='kraken helper module',
    author='Tactik8',
    author_email='admin@tactik8.com',
    packages=['kraken_helper'],  #same as name
    install_requires=['requests'], #external packages as dependencies
)
