import os
import numpy as np
import pytest
from agent.memory.faiss_memory import FaissMemory

@pytest.fixture(autouse=True)
def cleanup(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    yield

def test_add_and_query():
    mem = FaissMemory()
    mem.add("hello", "world")
    results = mem.query("hello")
    assert any("hello: world" in r for r in results)
