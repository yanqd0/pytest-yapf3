def test_yapf_success(testdir):
    testdir.makepyfile('''
        SOME_VALUE = 8
    ''')

    result = testdir.runpytest('--yapf', '-v')
    print(result)

    assert result.ret == 0


def test_yapf_failure(testdir):
    testdir.makepyfile('''
        AAA =8
    ''')

    result = testdir.runpytest('--yapf', '-v')

    result.stdout.fnmatch_lines([
        '*YAPF-check*',
        '*diff: +1/-1 lines',
    ])
    assert result.ret != 0


def test_yapf_failure_diff(testdir):
    testdir.makepyfile('''
        AAA =8
    ''')

    result = testdir.runpytest('--yapf', '--yapfdiff', '-v')

    result.stdout.fnmatch_lines([
        '*YAPF-check*',
        '*-AAA =8*',
        '*+AAA = 8*',
    ])
    assert result.ret != 0


def test_yapf_error(testdir):
    testdir.makepyfile('''
        AAA
    ''')

    result = testdir.runpytest('--yapf', '-v')

    result.stdout.fnmatch_lines([
        'E   NameError: name \'AAA\' is not defined',
    ])
    assert result.ret != 0
