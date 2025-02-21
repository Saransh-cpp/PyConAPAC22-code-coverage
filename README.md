# Code coverage through unit tests running in sub-processes/threads: Locally and automated on GitHub

[![Talk](https://img.shields.io/badge/PyConAPAC22-talk-blue?logo=github&logoColor=white&color=blue)](https://tw.pycon.org/2022/en-us/conference/talk/243/)
[![PyConAPAC 2022](https://github.com/Saransh-cpp/PyConAPAC22/actions/workflows/python-app.yml/badge.svg)](https://github.com/Saransh-cpp/PyConAPAC22/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/Saransh-cpp/PyConAPAC22/branch/main/graph/badge.svg?token=D8N0hyyKHx)](https://codecov.io/gh/Saransh-cpp/PyConAPAC22)

## Abstract

Unit testing and code coverage are two essential aspects of an open-source codebase. These unit tests often run in spawned sub-processes or threads as sub-processes or multi-threading allow them to run parallelly. They also make it easier to stop the tests midway if the process is taking too much time (probabilistic tests).

However, running unit tests in a sub-process creates a problem in the local repository as well as in the remote repository. As the documentation of coverage.py says — “Measuring coverage in those sub-processes can be tricky because you have to modify the code spawning the process to invoke coverage.py.”

## Description

The “Code coverage” value of a codebase depicts how much of the production/development code is covered by the running unit tests. In the world of open-source, all the maintainers try their best to keep this percentage high, and this process is often automated through tools like GitHub Actions and Codecov. Hence, code coverage becomes a good metric (not always) to check if a particular codebase is well tested and reliable.

Open source maintainers often prefer to run these unit tests in sub-processes or threads as it allows them to run in parallel and reduce the CI (continuous integration) run time on pull requests. They also make it easier to stop the tests midway if they are taking too much time (probabilistic tests).

In this talk, we will first try to use coverage.py in the default mode on the unit tests running in a sub-process or a thread. After going through the results, we will build a solution to cover the “un-covered” code in the local repository. As a final step, we will also configure a CI (continuous integration) pipeline using GitHub Actions and Codecov to automate this process in our remote repository
