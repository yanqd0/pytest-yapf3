"""
Validate your Python file format with yapf.
"""
import pytest
from yapf.yapflib import file_resources
from yapf.yapflib.yapf_api import FormatFile


def pytest_addoption(parser):
    """
    Parse optional arguments configured as `addopts` in pytest.ini,
    or trasferred from CLI.
    """
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


def pytest_collect_file(path, parent):
    """
    Return collection Node or None for the given path.
    Any new node needs to have the specified parent as a parent.
    """
    config = parent.config
    if config.option.yapf and path.ext == '.py':
        return YapfItem(path, parent)
    return None


class YapfError(Exception):
    """
    Raise this with message when any yapf error occurs.
    """


class YapfItem(pytest.Item, pytest.File):
    """
    Run yapf for every file.
    """
    def __init__(self, path, parent):
        super(YapfItem, self).__init__(path, parent)
        self.path = str(path)
        self.show_diff = self.parent.config.option.yapfdiff is True
        self.style = (
            self.parent.config.getoption('yapfstyle') or
            file_resources.GetDefaultStyleForDir(self.path)
        )  # yapf: disable

    def runtest(self):
        """
        Run yapf with each file, raise YapfError with messages if failed.
        """
        diff, _, changed = FormatFile(
            self.path,
            style_config=self.style,
            print_diff=True,
        )
        if not changed:
            return

        if self.show_diff:
            message = diff
        else:
            lines = diff.split('\n')
            added = len([x for x in lines if x.startswith('+')])
            removed = len([x for x in lines if x.startswith('-')])
            message = 'ERROR: {} YAPF diff: +{}/-{} lines'.format(
                self.path,
                added,
                removed,
            )
        raise YapfError(message)

    def repr_failure(self, excinfo, style=None):
        """
        Repare the failure YapfError.
        """
        if excinfo.errisinstance(YapfError):
            return excinfo.value.args[0]
        return super().repr_failure(excinfo)
