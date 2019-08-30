# pytest-yapf3

Validate your Python file format with yapf.

This is a [pytest] plugin, which make sure your python file is exactly formatted by yapf,
or it will crash when running `pytest`.

[pytest]:https://pytest.org/

## Install

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
- [ ] Display yapf as the session name.
- [ ] Display `YAPF` in `pytest --verbose`.
- [ ] Support `--yapf-ignore` to ignore specified files.
- [ ] Skip running if a file is not changed.

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

[![License](https://img.shields.io/github/license/yanqd0/pytest-yapf3.svg)](https://github.com/yanqd0/pytest-yapf3/blob/master/LICENSE)

> The MIT License (MIT)
>
> Copyright (c) 2019 Yan QiDong

This repository is forked from [pytest-yapf] in 2019, which is [not maintained] since 2017.
Besides extra features, the project structure is adjusted,
and the code is enhanced to pass linters like flake8, pylint and, of course, yapf.

[pytest-yapf]:https://github.com/django-stars/pytest-yapf
[not maintained]:https://github.com/django-stars/pytest-yapf/issues/1