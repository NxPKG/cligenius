# Building a Package

When you create a CLI program with **Cligenius** you probably want to create your own Python package.

That's what allows your users to install it and have it as an independent program that they can use in their terminal.

And that's also required for shell auto completion to work (unless you use your program through `cligenius` command).

Nowadays, there are several ways and tools to create Python packages (what you install with `pip install something`).

You might even have your favorite already.

Here's a very opinionated, short guide, showing one of the alternative ways of creating a Python package with a **Cligenius** app, from scratch.

/// tip

If you already have a favorite way of creating Python packages, feel free to skip this.

///

## Prerequisites

For this guide we'll use <a href="https://python-poetry.org/" class="external-link" target="_blank">Poetry</a>.

Poetry's docs are great, so go ahead, check them and install it.

## Create a project

Let's say we want to create a CLI application called `portal-gun`.

To make sure your package doesn't collide with the package created by someone else, we'll name it with a prefix of your name.

So, if your name is Rick, we'll call it `rick-portal-gun`.

Create a project with Poetry:

<div class="termy">

```console
$ poetry new rick-portal-gun

Created package rick_portal_gun in rick-portal-gun

// Enter the new project directory
cd ./rick-portal-gun
```

</div>

## Dependencies and environment

Add `cligenius` to your dependencies:

<div class="termy">

```console
$ poetry add cligenius

// It creates a virtual environment for your project
Creating virtualenv rick-portal-gun-w31dJa0b-py3.10 in /home/rick/.cache/pypoetry/virtualenvs
Using version ^0.12.0 for cligenius

Updating dependencies
Resolving dependencies... (1.2s)

---> 100%

Package operations: 8 installs, 0 updates, 0 removals

  - Installing mdurl (0.1.2)
  - Installing markdown-it-py (3.0.0)
  - Installing pygments (2.17.2)
  - Installing click (8.1.7)
  - Installing rich (13.7.1)
  - Installing shellingham (1.5.4)
  - Installing typing-extensions (4.11.0)
  - Installing cligenius (0.12.3)

Writing lock file

// Activate that new virtual environment
$ poetry shell

Spawning shell within /home/rick/.cache/pypoetry/virtualenvs/rick-portal-gun-w31dJa0b-py3.10

// Open an editor using this new environment, for example VS Code
$ code ./
```

</div>

You can see that you have a generated project structure that looks like:

```
.
├── poetry.lock
├── pyproject.toml
├── README.md
├── rick_portal_gun
│   └── __init__.py
└── tests
    └── __init__.py
```

## Create your app

Now let's create an extremely simple **Cligenius** app.

Create a file `rick_portal_gun/main.py` with:

```Python
import cligenius


app = cligenius.Cligenius()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    cligenius.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    cligenius.echo("Loading portal gun")
```

/// tip

As we are creating an installable Python package, there's no need to add a section with `if __name__ == "__main__":`.

///

## Modify the README

Let's change the README to have something like:

```Markdown
# Portal Gun

The awesome Portal Gun
```

## Add a "script"

We are creating a Python package that can be installed with `pip install`.

But we want it to provide a CLI program that can be executed in the shell.

To do that, we add a configuration to the `pyproject.toml` in the section `[tool.poetry.scripts]`:

```TOML hl_lines="8 9"
[tool.poetry]
name = "rick-portal-gun"
version = "0.1.0"
description = ""
authors = ["Rick Sanchez <rick@example.com>"]
readme = "README.md"

[tool.poetry.scripts]
rick-portal-gun = "rick_portal_gun.main:app"

[tool.poetry.dependencies]
python = "^3.10"
cligenius = "^0.12.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Here's what that line means:

`rick-portal-gun`: will be the name of the CLI program. That's how we will call it in the terminal once it is installed. Like:

<div class="termy">

```console
$ rick-portal-gun

// Something happens here ✨
```

</div>

`rick_portal_gun.main`, in the part `"rick_portal_gun.main:app"`, with underscores, refers to the Python module to import. That's what someone would use in a section like:

```Python
from rick_portal_gun.main import # something goes here
```

The `app` in `"rick_portal_gun.main:app"` is the thing to import from the module, and to call as a function, like:

```Python
from rick_portal_gun.main import app
app()
```

That config section tells Poetry that when this package is installed we want it to create a command line program called `rick-portal-gun`.

And that the object to call (like a function) is the one in the variable `app` inside of the module `rick_portal_gun.main`.

## Install your package

That's what we need to create a package.

You can now install it:

<div class="termy">

```console
$ poetry install

Installing dependencies from lock file

No dependencies to install or update

  - Installing the current project: rick-portal-gun (0.1.0)
```

</div>

## Try your CLI program

Your package is installed in the environment created by Poetry, but you can already use it.

<div class="termy">

```console
// You can use the which program to check which rick-portal-gun program is available (if any)
$ which rick-portal-gun

// You get the one from your environment
/home/rick/.cache/pypoetry/virtualenvs/rick-portal-gun-w31dJa0b-py3.10/bin/rick-portal-gun

// Try it
$ rick-portal-gun --help

// You get all the standard help
Usage: rick-portal-gun [OPTIONS] COMMAND [ARGS]...

  Awesome Portal Gun

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.

  --help                Show this message and exit.

Commands:
  load   Load the portal gun
  shoot  Shoot the portal gun
```

</div>

## Create a wheel package

Python packages have a standard format called a "wheel". It's a file that ends in `.whl`.

You can create a wheel with Poetry:

<div class="termy">

```console
$ poetry build

Building rick-portal-gun (0.1.0)
 - Building sdist
 - Built rick-portal-gun-0.1.0.tar.gz
 - Building wheel
 - Built rick_portal_gun-0.1.0-py3-none-any.whl
```

</div>

After that, if you check in your project directory, you should now have a couple of extra files at `./dist/`:

``` hl_lines="3 4"
.
├── dist
│   ├── rick_portal_gun-0.1.0-py3-none-any.whl
│   └── rick-portal-gun-0.1.0.tar.gz
├── pyproject.toml
├── README.md
├── ...
```

The `.whl` is the wheel file. You can send that wheel file to anyone and they can use it to install your program (we'll see how to upload it to PyPI in a bit).

## Test your wheel package

Now you can open another terminal and install that package from the file for your own user with:

<div class="termy">

```console
$ pip install --user /home/rick/rick-portal-gun/dist/rick_portal_gun-0.1.0-py3-none-any.whl

---> 100%
```

</div>

/// warning

The `--user` is important, that ensures you install it in your user's directory and not in the global system.

If you installed it in the global system (e.g. with `sudo`) you could install a version of a library (e.g. a sub-dependency) that is incompatible with your system.

///

/// tip

Bonus points if you use <a href="https://github.com/pipxproject/pipx" class="external-link" target="_blank">`pipx`</a> to install it while keeping an isolated environment for your Python CLI programs 🚀

///

Now you have your CLI program installed. And you can use it freely:

<div class="termy">

```console
$ rick-portal-gun shoot

// It works 🎉
Shooting portal gun
```

</div>

Having it installed globally (and not in a single environment), you can now install completion globally for it:

<div class="termy">

```console
$ rick-portal-gun --install-completion

zsh completion installed in /home/rick/.zshrc.
Completion will take effect once you restart the terminal.
```

</div>

/// tip

If you want to remove completion you can just delete the added line in that file.

///

And after you restart the terminal you will get completion for your new CLI program:

<div class="termy">

```console
$ rick-portal-gun [TAB][TAB]

// You get completion for your CLI program ✨
load   -- Load the portal gun
shoot  -- Shoot the portal gun
```

</div>

## Support `python -m` (optional)

You may have seen that you can call many Python modules as scripts with `python -m some-module`.

For example, one way to call `pip` is:

<div class="termy">

```console
$ pip install readyapi
```

</div>

But you can also call Python with the `-m` *CLI Option* and pass a module for it to execute as if it was a script, like:

<div class="termy">

```console
$ python -m pip install readyapi
```

</div>

Here we pass `pip` as the value for `-m`, so, Python will execute the module `pip` as if it was a script. And then it will pass the rest of the *CLI Parameters* (`install readyapi`) to it.

These two are more or less equivalent, the `install readyapi` will be passed to `pip`.

/// tip

In the case of `pip`, in many occasions it's actually recommended that you run it with `python -m`, because if you create a virtual environment with its own `python`, that will ensure that you use the `pip` from *that* environment.

///

### Add a `__main__.py`

You can support that same style of calling the package/module for your own package, simply by adding a file `__main__.py`.

Python will look for that file and execute it.

The file would live right beside `__init__.py`:

``` hl_lines="7"
.
├── poetry.lock
├── pyproject.toml
├── README.md
├── rick_portal_gun
│   ├── __init__.py
│   ├── __main__.py
│   └── main.py
└── tests
    └── __init__.py
```

No other file has to import it, you don't have to reference it in your `pyproject.toml` or anything else, it just works by default, as it is standard Python behavior.

Then in that file you can execute your **Cligenius** program:

```Python
from .main import app
app()
```

Now, after installing your package, if you call it with `python -m` it will work (for the main part):

<div class="termy">

```console
$ python -m rick_portal_gun --help

Usage: __main__.py [OPTIONS] COMMAND [ARGS]...

  Awesome Portal Gun

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.

  --help                Show this message and exit.

Commands:
  load   Load the portal gun
  shoot  Shoot the portal gun
```

</div>

/// tip

Notice that you have to pass the importable version of the package name, so `rick_portal_gun` instead of `rick-portal-gun`.

///

That works! 🚀 Sort of... 🤔

See the `__main__.py` in the help instead of `rick-portal-gun`? We'll fix that next.

### Set a program name in `__main__.py`

We are setting the program name in the file `pyproject.toml` in the line like:

```TOML
[tool.poetry.scripts]
rick-portal-gun = "rick_portal_gun.main:app"
```

But when Python runs our package as a script with `python -m`, it doesn't have the information of the program name.

So, to fix the help text to use the correct program name when called with `python -m`, we can pass it to the app in `__main__.py`:

```Python
from .main import app
app(prog_name="rick-portal-gun")
```

/// tip

You can pass all the arguments and keyword arguments you could pass to a Click application, including `prog_name`.

///

<div class="termy">

```console
$ python -m rick_portal_gun --help

Usage: rick-portal-gun [OPTIONS] COMMAND [ARGS]...

  Awesome Portal Gun

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.

  --help                Show this message and exit.

Commands:
  load   Load the portal gun
  shoot  Shoot the portal gun
```

</div>

Great! That works correctly! 🎉 ✅

Notice that now it uses `rick-portal-gun` instead of `__main__.py` in the help.

### Autocompletion and `python -m`

Have in mind that TAB completion (shell auto-completion) won't work when using `python -m`.

Auto-completion depends on the name of the program called, it's tied to each specific program name.

So, to have shell completion for `rick-portal-gun` you would have to call it directly:

<div class="termy">

```console
$ rick-portal-gun [TAB][TAB]
```

</div>

But you can still support `python -m` for the cases where it's useful.

## Publish to PyPI (optional)

You can publish that new package to <a href="https://pypi.org/" class="external-link" target="_blank">PyPI</a> to make it public, so others can install it easily.

So, go ahead and create an account there (it's free).

### PyPI API token

To do it, you first need to configure a PyPI auth token.

Login to <a href="https://pypi.org/" class="external-link" target="_blank">PyPI</a>.

And then go to <a href="https://pypi.org/manage/account/token/" class="external-link" target="_blank">https://pypi.org/manage/account/token/</a> to create a new token.

Let's say your new API token is:

```
pypi-wubalubadubdub-deadbeef1234
```

Now configure Poetry to use this token with the command `poetry config pypi-token.pypi`:

<div class="termy">

```console
$ poetry config pypi-token.pypi pypi-wubalubadubdub-deadbeef1234
// It won't show any output, but it's already configured
```

</div>

### Publish to PyPI

Now you can publish your package with Poetry.

You could build the package (as we did above) and then publish later, or you could tell poetry to build it before publishing in one go:

<div class="termy">

```console
$ poetry publish --build

# There are 2 files ready for publishing. Build anyway? (yes/no) [no] $ yes

---> 100%

Building rick-portal-gun (0.1.0)
 - Building sdist
 - Built rick-portal-gun-0.1.0.tar.gz
 - Building wheel
 - Built rick_portal_gun-0.1.0-py3-none-any.whl

Publishing rick-portal-gun (0.1.0) to PyPI
 - Uploading rick-portal-gun-0.1.0.tar.gz 100%
 - Uploading rick_portal_gun-0.1.0-py3-none-any.whl 100%
```

</div>

Now you can go to PyPI and check your projects at <a href="https://pypi.org/manage/projects/" class="external-link" target="_blank">https://pypi.org/manage/projects/</a>.

You should now see your new "rick-portal-gun" package.

### Install from PyPI

Now to see that we can install it form PyPI, open another terminal, and uninstall the currently installed package.

<div class="termy">

```console
$ pip uninstall rick-portal-gun

Found existing installation: rick-portal-gun 0.1.0
Uninstalling rick-portal-gun-0.1.0:
  Would remove:
    /home/rick/.local/bin/rick-portal-gun
    /home/rick/.local/lib/python3.10/site-packages/rick_portal_gun-0.1.0.dist-info/*
    /home/rick/.local/lib/python3.10/site-packages/rick_portal_gun/*
# Proceed (Y/n)? $ Y
    Successfully uninstalled rick-portal-gun-0.1.0
```

</div>

And now install it again, but this time using just the name, so that `pip` pulls it from PyPI:

<div class="termy">

```console
$ pip install --user rick-portal-gun

// Notice that it says "Downloading" 🚀
Collecting rick-portal-gun
  Downloading rick_portal_gun-0.1.0-py3-none-any.whl.metadata (435 bytes)
Requirement already satisfied: cligenius<0.13.0,>=0.12.3 in ./.local/lib/python3.10/site-packages (from rick-portal-gun==0.1.0) (0.12.3)
Requirement already satisfied: typing-extensions>=3.7.4.3 in ./.local/lib/python3.10/site-packages (from cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (4.11.0)
Requirement already satisfied: click>=8.0.0 in ./.local/lib/python3.10/site-packages (from cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (8.1.7)
Requirement already satisfied: shellingham>=1.3.0 in ./.local/lib/python3.10/site-packages (from cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (1.5.4)
Requirement already satisfied: rich>=10.11.0 in ./.local/lib/python3.10/site-packages (from cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (13.7.1)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.local/lib/python3.10/site-packages (from rich>=10.11.0->cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (2.17.2)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.local/lib/python3.10/site-packages (from rich>=10.11.0->cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (3.0.0)
Requirement already satisfied: mdurl~=0.1 in ./.local/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->cligenius<0.13.0,>=0.12.3->rick-portal-gun==0.1.0) (0.1.2)
Downloading rick_portal_gun-0.1.0-py3-none-any.whl (1.8 kB)
Installing collected packages: rick-portal-gun
Successfully installed rick-portal-gun-0.1.0
```

</div>

And now test the newly installed package from PyPI:

<div class="termy">

```console
$ rick-portal-gun load

// It works! 🎉
Loading portal gun
```

</div>

## Generate docs

You can use the `cligenius` command to generate docs for your package that you can put in your `README.md`:

<div class="termy">

```console
$ cligenius rick_portal_gun.main utils docs --output README.md --name rick-portal-gun

Docs saved to: README.md
```

</div>

You just have to pass it the module to import (`rick_portal_gun.main`) and it will detect the `cligenius.Cligenius` app automatically.

By specifying the `--name` of the program it will be able to use it while generating the docs.

/// tip

If you installed `cligenius-slim` and don't have the `cligenius` command, you can use `python -m cligenius` instead.

///

### Publish a new version with the docs

Now you can publish a new version with the updated docs.

For that you need to first increase the version in `pyproject.toml`:

```TOML hl_lines="3"
[tool.poetry]
name = "rick-portal-gun"
version = "0.2.0"
description = ""
authors = ["Rick Sanchez <rick@example.com>"]
readme = "README.md"

[tool.poetry.scripts]
rick-portal-gun = "rick_portal_gun.main:app"

[tool.poetry.dependencies]
python = "^3.10"
cligenius = "^0.12.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

And in the file `rick_portal_gun/__init__.py`:

```Python
__version__ = '0.2.0'
```

And then build and publish again:

<div class="termy">

```console
$ poetry publish --build

---> 100%

Building rick-portal-gun (0.2.0)
 - Building sdist
 - Built rick-portal-gun-0.2.0.tar.gz
 - Building wheel
 - Built rick_portal_gun-0.2.0-py3-none-any.whl

Publishing rick-portal-gun (0.2.0) to PyPI
 - Uploading rick-portal-gun-0.2.0.tar.gz 100%
 - Uploading rick_portal_gun-0.2.0-py3-none-any.whl 100%
```

</div>

And now you can go to PyPI, to the project page, and reload it, and it will now have your new generated docs.

## What's next

This is a very simple guide. You could add many more steps.

For example, you should use <a href="https://git-scm.com/" class="external-link" target="_blank">Git</a>, the version control system, to save your code.

You can add a lot of extra metadata to your `pyproject.toml`, check the docs for <a href="https://python-poetry.org/docs/libraries/" class="external-link" target="_blank">Poetry: Libraries</a>.

You could use <a href="https://github.com/pipxproject/pipx" class="external-link" target="_blank">`pipx`</a> to manage your installed CLI Python programs in isolated environments.

Maybe use automatic formatting with <a href="https://github.com/psf/black" class="external-link" target="_blank">Black</a>.

You'll probably want to publish your code as open source to <a href="https://github.com/" class="external-link" target="_blank">GitHub</a>.

And then you could integrate a <abbr title="Continuous Integration">CI</abbr> tool to run your tests and deploy your package automatically.

And there's a long etc. But now you have the basics and you can continue on your own 🚀.
