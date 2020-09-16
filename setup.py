from setuptools import setup

setup(
    name='krakenhelper',
    version='1.0.3',
    description='kraken helper module',
    author='Tactik8',
    author_email='admin@tactik8.com',
    packages=['krakenhelper'],  #same as name
    install_requires=['requests', 'validators', 'pytz', 'flask'], #external packages as dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
