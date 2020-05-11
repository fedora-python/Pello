
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pello",
    version="1.0.0",
    author="Tomáš Hrnčiar",
    author_email="tomas.hrnciar@me.com",
    description="An example Python Hello World package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrnciar/pello",
    license="CC0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pello_greeting = pello.pello_greeting:greeting'
        ]
    }
) 
