[![nbhub](https://github.com/duarteocarmo/nbhub/raw/master/assets/logo.png)](https://nbhub.duarteocarmo.com)

A command-line application for sharing jupyter notebooks to the web. Simple, minimal, hacky. 

[![Build Status](https://travis-ci.org/duarteocarmo/nbhub.svg?branch=master)](https://travis-ci.org/duarteocarmo/nbhub) [![Coverage Status](https://coveralls.io/repos/github/duarteocarmo/nbhub/badge.svg?branch=master&service=github)](https://coveralls.io/github/duarteocarmo/nbhub?branch=master) [![PyPI version shields.io](https://img.shields.io/pypi/v/nbhub.svg)](https://pypi.python.org/pypi/nbhub/) [![Supported Python versions](https://img.shields.io/pypi/pyversions/nbhub.svg)](https://pypi.org/project/nbhub/) [![PyPI downloads](https://img.shields.io/pypi/dm/nbhub.svg)](https://pypistats.org/packages/nbhub) [![GitHub license](https://img.shields.io/github/license/duarteocarmo/nbhub.svg)](https://github.com/duarteocarmo/nbhub/blob/master/LICENSE) [![made with: Vim](https://img.shields.io/badge/made%20with-Vim-019331)](https://github.com/vim/vim) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

NbHub, works by sending your jupyter notebooks to a web server and converting them to static `html` files. We are currently working on open sourcing the webserver as well!

**This is alpha! Check the [roadmap](#roadmap) and don't blow up my server.**

## Installation

NbHub requires pyhton 3.6 or newer. 

```bash
$ pip install nbhub
```

We actually recommend you using [pipx](https://github.com/pipxproject/pipx) for installing CLI tools. 

## Usage

Once installed, simply run `nbhub <path-to-the-notebook>`, and receive a link to share with anyone. [Here's an example link](https://nbhub.duarteocarmo.com/notebook/0d856c18).

And here's the CLI in action:

![nbhub](https://github.com/duarteocarmo/nbhub/raw/master/assets/usage.png)

## Contributing

Start by forking this repo.

Install the development dependencies (you probably want to do this in a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/)):

```bash
 $ pip install -r requirements-dev.txt
 ```

Make sure the tests run:

```bash
 $ pytest
 ```

Now go ahead and make some changes and submit a pull request :)

**Bugs and other issues** should be reported [right here](https://github.com/duarteocarmo/nbhub/issues). 

**More info?** Just submit an issue or [email me](mailto:me@duarteocarmo.com). 

## Roadmap

- [ ] Open source the web server.
- [ ] Date limit on notebooks to be destroyed.
- [ ] Ability to set password on link creation for private notebooks.
- [ ] Improvements to CLI like only accepting notebook format.
- [ ] Web server improvements (auto clean ups, encryption, etc.)