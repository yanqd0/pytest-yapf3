# pytest-yapf3

Validate your Python file format with yapf.

This is a [pytest] plugin, which make sure your python file is exactly formated by yapf,
or it will crash when running `pytest`.

[pytest]:https://pytest.org/

## Install

```sh
pip install pytest-yapf
```

## Usage

```ini
[tool:pytest]
addopts =
    --yapf
```

Add `--yapf` to [pytest] configuration `addopts`, or run with command.

```sh
pytest -m yapf
```
