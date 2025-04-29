"""
This file defines what tests are executed by the "poetry run nox" command
https://nox.thea.codes/en/stable/config.html
"""

import shutil

from nox import Session, parametrize, session


@session(python=False)
def black(session: Session) -> None:
    """
    Run black formatter for python.
    https://black.readthedocs.io/en/stable/
    """
    # Run black formatter in check mode
    session.run("black", "--check", "--diff", ".")


@session(python=False)
def ruff(session: Session) -> None:
    """
    Run black formatter for python.
    https://black.readthedocs.io/en/stable/
    """
    # Run black formatter in check mode
    session.run("ruff", "check", ".")


@session(python=False)
def cleanup(session: Session) -> None:
    """
    Erase test outputs.
    """
    # Clear output folder
    shutil.rmtree("tests/output", ignore_errors=True)


@session(python=False)
@parametrize("python", ["3.10", "3.11", "3.12"])
def sanity(session: Session, python) -> None:
    """
    Run all ansible sanity tests for the specified python version.
    """
    # Run sanity tests
    session.run(
        "ansible-test",
        "sanity",
        "--docker",
        "-v",
        "--python",
        python,
    )


@session(python=False)
@parametrize("python", ["3.10", "3.11", "3.12"])
def units(session: Session, python) -> None:
    """
    Run all ansible unit tests for the specified python version.
    """
    # Run unit tests
    session.run(
        "ansible-test", "units", "-v", "--docker", "--coverage", "--python", python
    )


@session(python=False)
def coverage(session: Session) -> None:
    """
    Print coverage report grouped by version.
    """
    # Print coverage
    session.run(
        "ansible-test",
        "coverage",
        "report",
        "--show-missing",
        "--include",
        "plugins/*/*",
        "--group-by",
        "version",
        "-v",
    )
    # Generate XML report
    session.run("poetry", "run", "ansible-test", "coverage", "xml")
    # Generate HTML report
    session.run("poetry", "run", "ansible-test", "coverage", "html")
