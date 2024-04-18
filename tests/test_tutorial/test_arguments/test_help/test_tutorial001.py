import subprocess
import sys

import types
import types.core
from types.testing import CliRunner

from docs_src.arguments.help import tutorial001 as mod

runner = CliRunner()

app = types.Types()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "[OPTIONS] NAME" in result.output
    assert "Arguments" in result.output
    assert "NAME" in result.output
    assert "The name of the user to greet" in result.output
    assert "[required]" in result.output


def test_help_no_rich():
    rich = types.core.rich
    types.core.rich = None
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "[OPTIONS] NAME" in result.output
    assert "Arguments" in result.output
    assert "NAME" in result.output
    assert "The name of the user to greet" in result.output
    assert "[required]" in result.output
    types.core.rich = rich


def test_call_arg():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
