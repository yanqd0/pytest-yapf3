# Change Log

## Release 0.4.0

- Add `yapf` as a pytest marker to enable `pytest -m yapf`
- Support `yapf-ignore` to ignore specified files

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
