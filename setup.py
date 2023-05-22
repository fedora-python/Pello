
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pello",
    version="1.0.4",
    author="Tomáš Hrnčiar",
    author_email="tomas.hrnciar@me.com",
    description="An example Python Hello World package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fedora-python/Pello",
    license="MIT-0",
    license_files=["LICENSE.txt"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT No Attribution License (MIT-0)",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pello_greeting = pello.pello_greeting:greeting'
        ]
    },
    extras_require   = {
        'color': ['blessings'],
    },
) 
