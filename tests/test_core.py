import pytest
from agent.core import Agent

def test_repl_exit(monkeypatch, capsys):
    inputs = ['exit']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    agent = Agent()
    with pytest.raises(SystemExit):
        agent.repl()
