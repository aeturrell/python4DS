# Python for Data Science

[![DOI](https://zenodo.org/badge/496994611.svg)](https://zenodo.org/doi/10.5281/zenodo.10518241)  ![GitHub Release](https://img.shields.io/github/v/release/aeturrell/python4DS)

This is the repo for **Python for Data Science**.

This README is for developers and contributors. If you're here to read the book, head over to [https://aeturrell.github.io/python4DS](https://aeturrell.github.io/python4DS).

## Contributing

We are very keen to encourage contributors! You can contribute by raising issues with the book or by creating pull requests directly. If you are creating a pull request you will need to install the development environment locally and check the book builds after you've made your changes.

Note that we aim to closely follow the content of [**R for Data Science (2e)**](https://r4ds.hadley.nz/).

Before making a pull request you should test that the pre-commit checks pass, including that there are no outputs included, and that the book builds. See below for instructions on how to do these locally.

When you make a pull request, pre-commit and build will run automatically, and fail if there are errors. They are in `.github/workflows/tests.yml`.

## Installing the development environment locally

You will need installations of Python 3.10 and [**uv**](https://docs.astral.sh/uv/). **uv** can be used to install certain distributions of Python through the `uv python install 3.12` command but you can use other Python installations.

Clone this repository.

To install the development environment, run `uv sync` from the project root. This should create a `.venv/` directory with the Python4DS environment in it. You can check that the environment has been installed by running `uv run python -V` in the project root directory.

## Building the book

The book is compiled from source markdown and Jupyter notebook files using [**Quarto**](https://quarto.org/). You will need Quarto installed on your system — see the [Quarto installation guide](https://quarto.org/docs/get-started/).

To build the book, run

```bash
uv run quarto render --execute
```

Once this command is run, you should be able to look at the HTML files for the book locally on your computer. They will be in `_book`. The `freeze: auto` setting means only notebooks whose source has changed will be re-executed on subsequent builds.

## Uploading the book

### Automatic uploads of the book

This repo is configured such that new versions automatically build and upload the book to the website. The GitHub Action that does this is in `.github/workflows/release.yml`.

### Uploading the built book manually

You shouldn't need to upload the book if you are a regular contributor. There are times when you might need to as an admin, but normally the book will be updated automatically upon release of a new version.

First build the book, then publish with:

```bash
uv run quarto publish gh-pages --no-render --no-browser
```

## Code hygiene

This book uses pre-commit to strip output from notebooks, lint, format, and check for large files added by mistake.

To perform the pre-commit checks, use

```bash
uv run pre-commit run --all-files
```

on your staged files. Ensure pre-commit reports all tests as having passed before committing.

## Publishing a new version

1. Open a new branch with the version name, eg `v1.0.4`

2. Change the version in `pyproject.toml` (you can run `uv run version_bumper.py`, which has script-level dependencies)

3. Commit the change with a new version label (eg `v1.0.4`) as the commit message

4. Go to GitHub. Assuming the tests pass, merge into main.

5. The book should automatically build in GitHub actions, and be pushed to the website. A new release will also be created automatically. A new Zenodo entry is also automatically created.

## Running and developing in a Docker container

There is a Dockerfile associated with this project.
 To use it:

1. Pre-reqs: docker installed, VS Code installed, VS Code docker and Remote Explorer extensions installed.
2. Build the image from the file. Right click on the file in VS Code and select "Build Image".
3. On the Docker tab of VS Code, right-click on the `python4DS:latest` image and select 'Run Interactive'.
4. On the Docker tab again, right-click on the running `python4DS:latest` container and click "Attach Visual Studio Code".
5. Do any development as required (see the instructions above)

If you wish to copy any files (eg the built HTML files) back to your local machine to check them, use

```bash
docker cp CONTAINER:app/_book/ temp_dir/
```
