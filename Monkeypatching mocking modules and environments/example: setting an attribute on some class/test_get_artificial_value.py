def test_some_interaction(monkeypatch):
    import os
    monkeypatch.setattr(os, "getcwd", lambda: "/")