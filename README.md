
# Pello
Pello is an example package that will be used as a part of
Fedora Python Packaging Guidelines.
The only thing that this package does
is printing `Hello World!` on the command line.


## Installation

In a virtual environment, run:

```console
$ python -m pip install pello
```

If you want colorized output, install the `color` extra:

```console
$ python -m pip install pello[color]
```

## Running

You can run the `pello_greeting` command directly:

```console
$ pello_greeting
Hello World!
````

You can also run the `pello` Python package:

```console
$ python -m pello
Hello World!
```

Or you can use the Python API:

```console
>>> import pello
>>> pello.greeting()
Hello World!
```

## Tests

Run tests using [Tox](https://tox.readthedocs.io/en/latest/):

```console
$ tox
```

This tests several Python interpreters (if they're available).
It also checks for some “code quality” issues in a separate Tox environment,
`lint`.

## Contributing to Pello

Pull requests welcome, but keep in mind that this is an example package.
Please coordinate major changes on [Fedora's Python SIG mailing list](mailto:python-devel@lists.fedoraproject.org).

## Name & History

Beginner RPM packaging guides have traditionally featured simple example
programs `hello` (in Bash), `cello` (in C) and `pello` (in Python).

This project is not a simple script, but a full Python project with associated
metadata (in `pyproject.toml` and `setup.py`).
This metadata should be converted, as automatically as possible,
into RPM metadata.

Thanks to the capital P, `Pello` differs from the
[normalized name](https://www.python.org/dev/peps/pep-0503/#normalized-name)
`pello`, so we can show where each of them is needed.
