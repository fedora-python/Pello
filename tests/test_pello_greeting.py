import pytest
from pello import pello_greeting

def test_pello_greeting(capsys):
    pello_greeting.greeting()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
