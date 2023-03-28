# pytest-yapf3

<!-- [![Travis](https://travis-ci.org/yanqd0/pytest-yapf3.svg?branch=master)](https://travis-ci.org/yanqd0/pytest-yapf3) -->
<!-- [![AppVeyor](https://ci.appveyor.com/api/projects/status/umf6393qo2y7afog/branch/master?svg=true)](https://ci.appveyor.com/project/yanqd0/pytest-yapf3/branch/master) -->
<!-- [![codecov](https://codecov.io/gh/yanqd0/pytest-yapf3/branch/master/graph/badge.svg)](https://codecov.io/gh/yanqd0/pytest-yapf3) -->

[![Python PyTest](https://github.com/yanqd0/pytest-yapf3/actions/workflows/python-pytest.yml/badge.svg)](https://github.com/yanqd0/pytest-yapf3/actions/workflows/python-pytest.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3446/badge)](https://bestpractices.coreinfrastructure.org/projects/3446)
[![Code style: yapf](https://img.shields.io/badge/code%20style-yapf-blue)](https://github.com/google/yapf)

Validate your Python file format with yapf.

This is a [pytest] plugin,
which make sure your python file is exactly formatted by yapf,
or it will crash when running `pytest`.

[pytest]:https://pytest.org/

## Install

[![Version](https://img.shields.io/pypi/v/pytest-yapf3)](https://pypi.org/project/pytest-yapf3/)
[![Python](https://img.shields.io/pypi/pyversions/pytest-yapf3)](https://pypi.org/project/pytest-yapf3/)
[![Format](https://img.shields.io/pypi/format/pytest-yapf3)](https://pypi.org/project/pytest-yapf3/)
[![Status](https://img.shields.io/pypi/status/pytest-yapf3)](https://pypi.org/classifiers/)
[![Download](https://img.shields.io/pypi/dm/pytest-yapf3)](https://pypi.org/project/pytest-yapf3/)
[![MIT](https://img.shields.io/pypi/l/pytest-yapf3)](https://github.com/yanqd0/pytest-yapf3/blob/master/LICENSE)

```sh
pip install pytest-yapf3
```

Requires:

- Python 3.6 or above
- Pytest:
    - `pytest>=5.4,<8` when `pytest-yapf3<0.7`
    - `pytest>=7` when `pytest-yapf3>=0.7`

If someone use this with Python 3.5 or Pytest less than 5.4, set `'pytest-yapf3<0.6.0'`.

## Usage

Modify `setup.cfg` (or `pytest.ini`):

```ini
[tool:pytest]
addopts =
    --yapf
    --yapfdiff
yapf-ignore =
    setup.py
    src/package/auto_generated/**.py
```

Add `--yapf` to [pytest] configuration `addopts`.
If run with `pytest -m yapf`, only `yapf` is checked.

By default, only line summaries is displayed.
With an optional `--yapfdiff`, a full text of `yapf -d` is displayed.
If not configured here, `pytest --yapfdiff` will also work.

An optional `yapf-ignore` is supported.
Each line specifies a glob pattern of files which should not check `yapf`.

The `pytest` will cache success results of pytest-yapf3, and will not check again if files not changed.
Sometimes you may want to disable it.
There are 2 ways:

- `pytest -p no:cacheprovider`
    This may crash if any other pytest plugin not supports.
- `rm -rf .pytest_cache/v/yapf`
    This is ugly, but safe for any environment.

## Features and Todos

- [x] Basic support to validate `yapf`.
- [x] Fix the diff line count error and improve the performance.
- [x] Display `YAPF-check` as the error session name.
- [x] Display `YAPF` in `pytest --verbose`.
- [x] Add `yapf` as a marker to enable `pytest -m yapf`.
- [x] Support `yapf-ignore` to ignore specified files.
- [x] Skip running if a file is not changed.
- [x] 100% test coverage.

## Develop

Prepare the environment:

```sh
pipenv install --dev
pipenv shell
```

Run test:

```sh
pytest
```

## Badge

Like [black], if your project always pass yapf checking provided by this project,
you can use an unofficial badge to show off.

[black]:https://github.com/psf/black#show-your-style

### Markdown (README.md)

```markdown
[![Code style: yapf](https://img.shields.io/badge/code%20style-yapf-blue)](https://github.com/google/yapf)
```

### reStructuredText (README.rst)

```rst
.. image:: https://img.shields.io/badge/code%20style-yapf-blue
    :target: https://github.com/google/yapf
    :alt: Code style: yapf
```

## License

> The MIT License (MIT)
>
> Copyright (c) 2019~2022 Yan QiDong

This repository is forked from [pytest-yapf] in 2019, which is [not maintained] since 2017.
Besides extra features, the project structure is adjusted,
and the code is enhanced to pass linters like flake8, pylint and, of course, yapf.

The `3` in `pytest-yapf3` means this package supports Python 3 only.

[pytest-yapf]:https://github.com/django-stars/pytest-yapf
[not maintained]:https://github.com/django-stars/pytest-yapf/issues/1
