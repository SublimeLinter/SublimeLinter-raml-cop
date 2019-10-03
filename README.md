SublimeLinter-raml-cop
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-raml-cop.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-raml-cop)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [raml-cop](https://github.com/thebinarypenguin/raml-cop).

## Installation

SublimeLinter must be installed in order to use this plugin.

Install via [Package Control](https://packagecontrol.io) or `git clone` as usual.

Ensure that `raml-cop` is installed on your system. To install `raml-cop`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

2. Install `raml-cop` by typing the following in a terminal:
   ```
   npm install -g raml-cop
   ```

3. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

4. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plugin for `oh-my-zsh`.

In order for `raml-cop` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation

## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
