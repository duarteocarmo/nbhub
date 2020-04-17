from click.testing import CliRunner
from nbhub import nbhub
import pathlib


def test_nbhub():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "test_notebook.ipynb"
    result = runner.invoke(nbhub, [str(notebook)], input="\n".join(["y", "n"]))
    assert result.exit_code == 0
    assert "Published" in result.output


def test_nbhub_with_password():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "test_notebook.ipynb"
    print("hey")
    result = runner.invoke(nbhub, [str(notebook)], input="\n".join(["y", "y"]))
    assert result.exit_code == 0
    assert "not available yet" in result.output


def test_bad_file():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "bad.txt"
    result = runner.invoke(nbhub, [str(notebook)], input="\n".join(["y", "n"]))
    assert result.exit_code == 0
    assert "wrong" in result.output
