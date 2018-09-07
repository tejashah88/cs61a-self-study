import sys
from io import StringIO
from contextlib import contextmanager
from unittest import TestCase
from textwrap import dedent

@contextmanager
def output_recorder(command, *args, **kwargs):
    out, sys.stdout = sys.stdout, StringIO()
    try:
        command(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdout = out

def clean_string(s):
    return dedent(s).strip()

class EnhancedTestCase(TestCase):
    def assertPrinted(self, fn, args, expected):
        if type(args) not in [tuple, list]:
            args = [args]
        with output_recorder(fn, *args) as output:
            self.assertEqual(expected, output.strip())

