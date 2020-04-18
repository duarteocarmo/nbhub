import pathlib
import pytest
import nbhub
from click.testing import CliRunner
import click


def test_nbhub_normal():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "test_notebook.ipynb"
    result = runner.invoke(
        nbhub.main, [str(notebook)], input="\n".join(["y", "n"])
    )
    assert result.exit_code == 0
    assert "Published" in result.output


def test_nbhub_nothing():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "test_notebook.ipynb"
    result = runner.invoke(nbhub.main)
    assert result.exit_code == 0
    assert "No notebook provided, nothing to do" in result.output


def test_nbhub_with_password():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "test_notebook.ipynb"
    print("hey")
    result = runner.invoke(
        nbhub.main, [str(notebook)], input="\n".join(["y", "y"])
    )
    assert result.exit_code == 0
    assert "not available yet" in result.output


def test_bad_file():
    runner = CliRunner()
    notebook = pathlib.Path.cwd() / "tests" / "data" / "bad.txt"
    result = runner.invoke(
        nbhub.main, [str(notebook)], input="\n".join(["y", "n"])
    )
    assert result.exit_code == 0
    assert "wrong" in result.output


def test_check_notebook():
    notebook = pathlib.Path.cwd() / "tests" / "data" / "test_notebook.ipynb"
    assert nbhub.check_notebook(notebook) == None


def test_check_status_good():
    assert nbhub.status_ok("https://google.com") == True


def test_check_status_bad():
    with pytest.raises(click.exceptions.Exit) as f:
        with pytest.raises(ConnectionError) as e:
            assert nbhub.status_ok("https://google.aafeaf") == False
