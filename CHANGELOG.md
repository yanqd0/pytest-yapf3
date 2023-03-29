# Change Log

## Release 0.7.0

- Set pytest limit to `>=7`.
- Fix a pytest warning with `from_parent`.

## Release 0.6.2

- Set pytest limit to `>=5.4,<8`.
- Upgrade dependencies in Pipfile and its lock.
- Enable GitHub actions.
- Delete `.travis.yml` and `.appveyor.yml`

## Release 0.6.1

- Fix cache missing.

## Release 0.6.0

- Upgrade pytest to 5.4+, fix a warning.
- Support python 3.6+ only, abandon 3.5
- Use Pipfile with `pipenv`

## Release 0.5.1

- Fix coverage missing lines.
- 100% test coverage.
- Fix a crash when yapf crash.
- Change development status to stable.

## Release 0.5.0

- Skip running if a file is not changed.
- Add more usage description in README.

## Release 0.4.0

- Add `yapf` as a pytest marker to enable `pytest -m yapf`
- Support `yapf-ignore` to ignore specified files
- Fix a probabilistic issue caused by `\r`

## Release 0.3.0

- Display `YAPF-check` as the error session name
- Display `::YAPF` in `pytest --verbose`

## Release 0.2.0

Since forked from [pytest-yapf](https://pypi.org/project/pytest-yapf/) `0.1.1`, there are some improvements:

- Restructure the project and rewrite documents
- Support Python 3.4+ only
- Add linters to pytest, and fix their errors
- Fix the line count error
- Change build configurations in [Travis] and [AppVeyor]
- Support coverage and displayed in [codecov]

[Travis]:https://travis-ci.org
[AppVeyor]:https://appveyor.com
[codecov]:https://codecov.io
