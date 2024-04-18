import subprocess
import sys

import types
import types.core
from types.testing import CliRunner

from docs_src.parameter_types.bool import tutorial002_an as mod

runner = CliRunner()

app = types.Types()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--accept" in result.output
    assert "--reject" in result.output
    assert "--no-accept" not in result.output


def test_help_no_rich():
    rich = types.core.rich
    types.core.rich = None
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--accept" in result.output
    assert "--reject" in result.output
    assert "--no-accept" not in result.output
    types.core.rich = rich


def test_main():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "I don't know what you want yet" in result.output


def test_accept():
    result = runner.invoke(app, ["--accept"])
    assert result.exit_code == 0
    assert "Accepting!" in result.output


def test_reject():
    result = runner.invoke(app, ["--reject"])
    assert result.exit_code == 0
    assert "Rejecting!" in result.output


def test_invalid_no_accept():
    result = runner.invoke(app, ["--no-accept"])
    assert result.exit_code != 0
    assert "No such option: --no-accept" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
