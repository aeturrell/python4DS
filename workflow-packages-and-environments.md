---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python4DS
  language: python
  name: python3
---
(workflow-packages-and-environments)=
# Workflow: Packages and Environments

In this chapter, you're going to learn about packages and how to install them plus virtual coding environments that keep your packages isolated and your projects reproducible.

## Packages

### Introduction

Packages (also called libraries) are key to extending the functionality of Python. The default installation of Anaconda comes with many (around 250) of the packages you'll need, but it won't be long before you'll need to install some extra ones. There are packages for geoscience, for building websites, for analysing genetic data, for economics—pretty much for anything you can think of. Packages are typically not written by the core maintainers of the Python language but by enthusiasts, firms, researchers, academics, all sorts! Because anyone can write packages, they vary widely in their quality and usefulness. There are some that you'll be seeing them again and again.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Name a more iconic trio, I&#39;ll wait. <a href="https://t.co/pGaLuUxQ3r">pic.twitter.com/pGaLuUxQ3r</a></p>&mdash; Vicki Boykis (@vboykis) <a href="https://twitter.com/vboykis/status/1032631145035427840?ref_src=twsrc%5Etfw">August 23, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The three Python packages **numpy**, **pandas**, and **maplotlib**, which respectively provide numerical, data analysis, and plotting functionality, are ubiquitous. So many scripts begin by importing all three of them, as in the tweet above!

There are typically two steps to using a new Python package:

1. *install* the package on the command line (aka the terminal), eg using `pip install pandas`

2. *import* the package into your Python session, eg using `import pandas as pd`

When you issue an install command for a specific package, it is automatically downloaded from the internet and installed in the appropriate place on your computer. To install extra Python packages, you issue install commands to a text-based window called the "terminal".

### The Command Line in Brief

The *terminal* or *command line* or sometimes the *command prompt* was labelled 4 in the screenshot of Visual Studio Code from the chapter on {ref}`introduction`. The terminal is a text-based way to issue all kinds of commands to your computer (not just Python commands) and knowing a little bit about it is really useful for coding (and more) because managing packages, environments (which we haven't yet discussed), and version control (ditto) can all be done via the terminal. We'll come to these in due course in the chapter on {ref}`command-line`, but for now, a little background on what the terminal is and what it does.

```{note}
To open up the command line within Visual Studio Code, use the <kbd>⌃</kbd> + <kbd>\`</kbd> keyboard shortcut (Mac) or <kbd>ctrl</kbd> + <kbd>\`</kbd> (Windows/Linux), or click "View > Terminal".

Windows users may find it easiest to use the Anaconda Prompt as their terminal, at least for installing Python packages.

If you want to open up the command line independently of Visual Studio Code, search for "Terminal" on Mac and Linux, and "Anaconda Prompt" on Windows. 
```

Firstly, everything you can do by clicking on icons to launch programmes on your computer, you can also do via the terminal, also known as the command line. For many programmes, a lot of their functionality can be accessed using the command line, and other programmes *only* have a command line interface (CLI), including some that are used for data science.

```{tip}
The command line interacts with your operating system and is used to create, activate, or change python installations.
```

Use Visual Studio Code to open a terminal window by clicking Terminal -> New Terminal on the list of commands at the very top of the window. If you have installed the Anaconda distribution of Python, your terminal should look something like this as your 'command prompt':

```bash
(base) your-username@your-computer current-directory %
```

on Mac, and the same but with '%' replaced by '$' on linux, and (using the Anaconda Prompt)

```bash
(base) C:\Users\YourUsername>
```

on Windows. If you don't see the word `(base)` at the start of the line, you may need to type `conda activate` first.

The `(base)` part is saying that your current Python environment is the base one (later, we'll see how to add others for reproducibility and to isolate projects). Unfortunately, and confusingly, the commands that you can use in the terminal on Mac and Linux, on the one hand, and Windows, on the other, are different but many of the principles are the same.

For now, to at least try out the command line, let's use something that works across all three of the major operating systems. Type `python` on the command prompt that came up in your new terminal window. You should see information about your installation of Python appear, including the version, followed by a Python prompt that looks like `>>>`. This is a kind of interactive Python session, in the terminal. It's much less rich than the one available in Visual Studio Code (it can't run scripts line-by-line, for example) but you can try `print('Hello World!')` and it will run, printing your message. To exit the terminal-based Python session, type `exit()` to go back to the regular command line.

### Installing Packages

To install extra Python packages, there are two options, and both use the command line.

```{admonition} Activating Conda Python Environments
You'll need to have conda "activated" before installing a package in the terminal--if you don't see the name of an environment, eg `(base)`, at the start of your terminal's line, use the `conda activate` command first. On Windows, this is usually the command prompt (available in the integrated Visual Studio Code terminal) or the Anaconda Command Prompt (available in the start menu).
```

Install packages on the command line by typing

```bash
conda install package-name
```

and hitting return, where `package-name` might be `pandas`. This will try to install a version of the package that is already optimised for your type of computer, and will automatically come with any dependencies (packages the package you're installing needs to run). The pre-built packages that are provided by Anaconda are convenient for a host of reasons. Anaconda provide pre-built versions of around 7,500 of the most popular packages (including the statistical programming language R).

However, there are over 330,000 Python packages on PyPI (the Python Package Index) so you may sometimes find one that is not covered by `conda install`. When there isn't a pre-built Anaconda version of a package available, the next thing to try is

```bash
pip install packagename
```

In true programming-humour style, pip is a recursive acronym that stands for 'pip install packages'. You can see what packages you have installed by entering `conda list` into the command line.

Here's a full example of the commands used to install the **pandas** package into the base environment (you may not need the first one):

```bash
your-username@your-computer current-directory % conda activate
(base) your-username@your-computer current-directory % conda install pandas
```

```{admonition} Exercise
Try installing the **matplotlib**, **pandas**, and **statsmodels** packages using `conda install`.
```

```{admonition} Exercise
Install the **skimpy** package. (Hint: `conda install` may not be enough.)
```

### Using Packages

Once you have installed a package, you need to be able to use it! This is usually done via an import statement at the top of your script or Jupyter Notebook. For example, to bring in **pandas**, it's

```python
import pandas as pd
```

Why does Python do this? The idea of not just loading every package is to provide clarity over what function is being called from what package. It's also not necessary to load every package for every piece of analysis, and you often actually want to know what the *minimum* set of packages is to reproduce an analysis. Making the package imports explicit helps with all of that.

You may also wonder why one doesn't just use `import pandas as pandas`. There's actually nothing stopping you doing this except i) it's convenient to have a shorter name and ii) there does tend to be a convention around imports, ie `pd` for **pandas** and `np` for **numpy**, and your code will be clearer to yourself and others if you follow the conventions.

## Virtual Code Environments

Virtual code environments allow you to isolate all of the packages that you're using to do analysis for one project from the set of packages you might need for a different project. They're an important part of creating a reproducible analytical pipeline but a key benefit is that others can reproduce the environment you used and it's best practice to have an isolated environment per project.

It may be easier to illustrate creating separate environments with an example. Let's say you're using Python 3.8, **statsmodels**, and **pandas** for one project, project A. And, for project B, you're using Python 3.9 with **numpy** and **scikit-learn**. Even with the same version of Python, best practice would be to have two separate virtual Python environments: environment A, with everything needed for project A, and environment B, with everything needed for project B. For the case where you're using different versions of Python, this isn't just best practice, it's essential.

Many programming languages now come with an option to install packages and a version of the language in isolated enironments. In Python, there are multiple tools for managing different environments. Of those, the easiest to work with is probably [**Anaconda**](https://docs.conda.io/projects/conda/en/latest/index.html) (conda for short).

If you're just getting going with data science, this book recommends that you use Anaconda (aka conda) environments.

### Using Anaconda to Manage Python Environments

Much of these two subsections is covered by the Anaconda documentation on [managing virtual environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

If you're using Anaconda, you manage and change environments on the command line (more on the command line in {ref}`command-line`). Before following these instructions, check that you have Anaconda installed and activated. You should see something like `(base) username@computername:~$` on the command line (base is the default conda environment).

To create a new environment called "myenv" with a specific version of Python (but no extra packages installed), it's

```bash
conda create -n myenv python=3.8
```

where you can of course specify other versions of Python by changing the number. To throw in a package or two, just add them to the end, for example

```bash
conda create -n myenv python=3.8 pandas jupyter
```

You can see a list of the currently installed environments by running

```bash
conda env list
```

Running the same command within an environment will list only those packages installed in that environment.

When you install Anaconda, you will begin with a "base" environment. It's a good idea not to use this for projects but to instead to create a new environment for each project.

There are two downsides to installing environments directly from the command line. One is that you may have lots of packages. The second is that you may wish to keep a record of the environment you created. For both of these reasons, you can specify a conda environment using a file.

The pandas example we saw above would look like

```yaml
name: myenv
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pandas
  - jupyter

```

The environment is given by `name`, the channel (where to look for the packages) by `channels`, the specific packages by `dependencies`. Not all packages are available on conda's channels, so sometimes extra ones are needed. By specifying `conda-forge` we get the widest possible selection of packages. Some packages are only available on pip; these can be specified with a sub-section of the file like so for the **skimpy** package:

```yaml
name: myenv
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pandas
  - jupyter
  - pip:
    - skimpy

```

This goes into a file called `environment.yml`, which can be installed by running

```bash
conda env create -f environment.yml
```

This book is put together using an isolated *conda* environment specified in a file. It's an unusually big one because there are a lot of packages featured in the book! Here they are:

```{code-cell} ipython3
:tags: ["hide-input"]
from rich import print

with open("environment.yml", 'r') as stream:
    data_loaded = stream.read()

print(data_loaded)
```

Of course, you can install packages as you go too, you don't have to specify them when you create the environment. With the relevant environment activated, use `conda install packagename` to do this.

Finally, to remove an environment, it's

```bash
conda remove --name myenv --all
```

### Using and Switching Between Conda Environments

To switch between conda environments on the command line, for example from the base environment to an environment called "myenv", use

```bash
conda activate myenv
```

on the command line. However, this only switches the environment if you plan to run code on the command line!

Fortunately, Visual Studio Code has you covered and makes it very easy to switch Python environments for a project at the click of a button.

![A typical user view in Visual Studio Code](https://github.com/aeturrell/coding-for-economists/blob/main/img/vscode_layout.png?raw=true)

In the screenshot above, you can see the project-environment in two places: on the blue bar at the bottom of the screen, and (in 5), at the top right hand side of the interactive window. Click on either to change the Python environment that will be used to execute code. A similar top right selector is present for Jupyter Notebooks too.
