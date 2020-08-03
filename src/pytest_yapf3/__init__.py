"""Validate your Python file format with yapf."""

import re

import pytest
from yapf.yapflib import file_resources
from yapf.yapflib.yapf_api import FormatFile

HISTKEY = 'yapf/mtimes'


def pytest_addoption(parser):
    """Parse optional arguments from CLI or configured as `addopts`."""
    group = parser.getgroup('yapf')
    group.addoption(
        '--yapf',
        action='store_true',
        help='run yapf on *.py files.',
    )
    group.addoption(
        '--yapfdiff',
        action='store_true',
        help='show diff of yapf output.',
    )
    group.addoption(
        '--yapfstyle',
        action='store',
        dest='yapfstyle',
        default=None,
        help='style to be used by yapf.',
    )
    parser.addini(
        'yapf-ignore',
        type='linelist',
        help='each line specifies a glob pattern of files,'
        'which will not check YAPF',
    )


def pytest_configure(config):
    """
    Load arguments from CLI, set more values to config.

    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.
    """
    config.addinivalue_line('markers', 'yapf: Tests which run yapf.')
    if config.option.yapf:
        config.yapf_ignore = config.getini('yapf-ignore')
    if hasattr(config, 'cache'):
        config.yapf_mtimes = config.cache.get(HISTKEY, {})
    else:
        config.yapf_mtimes = {}


def pytest_unconfigure(config):
    """
    Flush the cache in the end.

    This hook is called before test process is exited.
    """
    if hasattr(config, "cache"):
        config.cache.set(HISTKEY, config.yapf_mtimes)


def _should_ignore(path, ignore_globs):
    return any(path.fnmatch(glob) for glob in ignore_globs)


def pytest_collect_file(path, parent):
    """
    Return collection Node or None for the given path.

    Any new node needs to have the specified parent as a parent.
    """
    config = parent.config
    if (
            config.option.yapf and
            path.ext == '.py' and
            not _should_ignore(path, config.yapf_ignore)
    ):  # yapf: disable
        return YapfFile.from_parent(parent=parent, fspath=path)
    return None


class YapfError(Exception):
    """Raise this with message when any yapf error occurs."""


class YapfFile(pytest.File):  # pylint: disable=abstract-method
    """The files to be collected."""
    def collect(self):
        yield YapfItem.from_parent(
            parent=self,
            name='YAPF',
        )


class YapfItem(pytest.Item):  # pylint: disable=abstract-method
    """Run yapf for every file."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_diff = self.parent.config.option.yapfdiff is True
        self.add_marker('yapf')
        self.__mtime = self.fspath.mtime()
        self.__style = (
            self.parent.config.getoption('yapfstyle') or
            file_resources.GetDefaultStyleForDir(str(self.fspath))
        )  # yapf: disable

    def setup(self):
        """Skip if the file is not changed since last success."""
        if self.__mtime == self.config.yapf_mtimes.get(self.nodeid, 0):
            pytest.skip("file(s) previously passed yapf checks")

    def runtest(self):
        """
        Run yapf with each file.

        Raise YapfError with messages if failed,
        or save the file mtime.
        """
        diff, _, changed = FormatFile(
            str(self.fspath),
            style_config=self.__style,
            print_diff=True,
        )
        if not changed:
            self.config.yapf_mtimes[self.nodeid] = self.__mtime
            return

        if self.show_diff:
            message = diff
        else:
            diff = diff.replace('\r', '\n')
            add = sum(1 for i in re.finditer(r'^\+', diff, re.MULTILINE)) - 1
            remove = sum(1 for i in re.finditer(r'^-', diff, re.MULTILINE)) - 1
            message = f'ERROR: {self.fspath} YAPF diff: +{add}/-{remove} lines'
        raise YapfError(message)

    def repr_failure(self, excinfo, _=None):
        """Repair the failure YapfError."""
        if excinfo.errisinstance(YapfError):
            return excinfo.value.args[0]
        return super().repr_failure(excinfo, 'native')

    def reportinfo(self):
        """
        Define the report title.

        This is used for representing the test location
        and is also consulted when reporting in verbose mode.
        """
        return self.fspath, -1, 'YAPF-check'
