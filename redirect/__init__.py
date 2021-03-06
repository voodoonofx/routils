import sys

import roplus

def stdout(path_to_stdout, force=False):
    if force or getattr(sys.stdout, 'name', 'nope') != path_to_stdout:
        roplus.log('Redirecting STDOUT to {0}'.format(path_to_stdout))
        sys.stdout = open(path_to_stdout, 'wb')

def stderr(path_to_stderr, force=False):
    if force or getattr(sys.stderr, 'name', 'nope') != path_to_stderr:
        roplus.log('Redirecting STDERR to {0}'.format(path_to_stderr))
        sys.stderr = open(path_to_stderr, 'wb')
