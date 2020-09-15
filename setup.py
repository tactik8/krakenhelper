from setuptools import setup

setup(
    name='kraken_helper',
    version='1.0',
    description='krkane helper module',
    author='TActik8',
    author_email='admin@tactik8.com',
    packages=['kraken_helper'],  #same as name
    install_requires=['requests', 'json'], #external packages as dependencies
)
