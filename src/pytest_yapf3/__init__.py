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
        return YapfItem(path, parent)
    return None


class YapfError(Exception):
    """Raise this with message when any yapf error occurs."""


class YapfItem(pytest.Item, pytest.File):
    """Run yapf for every file."""
    def __init__(self, path, parent):
        """Set item options from global config."""
        super(YapfItem, self).__init__(path, parent)
        self._nodeid += '::YAPF'
        self.path = str(path)
        self.show_diff = self.parent.config.option.yapfdiff is True
        self.style = (
            self.parent.config.getoption('yapfstyle') or
            file_resources.GetDefaultStyleForDir(self.path)
        )  # yapf: disable
        self.add_marker('yapf')
        self.__mtime = self.fspath.mtime()

    def setup(self):
        """Skip if the file is not changed since last success."""
        if self.__mtime == self.config.yapf_mtimes.get(self.name, 0):
            pytest.skip("file(s) previously passed yapf checks")

    def runtest(self):
        """
        Run yapf with each file.

        Raise YapfError with messages if failed,
        or save the file mtime.
        """
        diff, _, changed = FormatFile(
            self.path,
            style_config=self.style,
            print_diff=True,
        )
        if not changed:
            self.config.yapf_mtimes[self.name] = self.__mtime
            return

        if self.show_diff:
            message = diff
        else:
            diff = diff.replace('\r', '\n')
            added = sum(1 for i in re.finditer(r'^\+', diff, re.MULTILINE))
            removed = sum(1 for i in re.finditer(r'^-', diff, re.MULTILINE))
            message = 'ERROR: {} YAPF diff: +{}/-{} lines'.format(
                self.path,
                added - 1,
                removed - 1,
            )
        raise YapfError(message)

    def repr_failure(self, excinfo, _=None):
        """Repair the failure YapfError."""
        if excinfo.errisinstance(YapfError):
            return excinfo.value.args[0]
        return super().repr_failure(excinfo)

    def reportinfo(self):
        """
        Define the report title.

        This is used for representing the test location
        and is also consulted when reporting in verbose mode.
        """
        return self.fspath, -1, 'YAPF-check'
