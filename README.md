# pytest-yapf3

[![Travis](https://travis-ci.org/yanqd0/pytest-yapf3.svg?branch=master)](https://travis-ci.org/yanqd0/pytest-yapf3)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/umf6393qo2y7afog/branch/master?svg=true)](https://ci.appveyor.com/project/yanqd0/pytest-yapf3/branch/master)
[![codecov](https://codecov.io/gh/yanqd0/pytest-yapf3/branch/master/graph/badge.svg)](https://codecov.io/gh/yanqd0/pytest-yapf3)

Validate your Python file format with yapf.

This is a [pytest] plugin, which make sure your python file is exactly formatted by yapf,
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

## Usage

Modify `setup.cfg` (or `pytest.ini`):

```ini
[tool:pytest]
addopts =
    --yapf
    --yapfdiff
```

Add `--yapf` to [pytest] configuration `addopts`.
By default, only line summaries is displayed.
With `--yapfdiff`, a full text of `yapf -d` is displayed.

## Features and Todos

- [x] Basic support to validate `yapf`.
- [x] Fix the diff line count error and improve the performance.
- [x] Display `YAPF-check` as the error session name.
- [x] Display `YAPF` in `pytest --verbose`.
- [ ] Support `--yapf-ignore` to ignore specified files.
- [ ] Skip running if a file is not changed.
- [ ] 100% test coverage.

## Develop

Prepare the environment:

```sh
source your/virtual/env
pip install -e .[dev]
```

Run test:

```sh
pytest
```

## License

> The MIT License (MIT)
>
> Copyright (c) 2019 Yan QiDong

This repository is forked from [pytest-yapf] in 2019, which is [not maintained] since 2017.
Besides extra features, the project structure is adjusted,
and the code is enhanced to pass linters like flake8, pylint and, of course, yapf.

[pytest-yapf]:https://github.com/django-stars/pytest-yapf
[not maintained]:https://github.com/django-stars/pytest-yapf/issues/1
