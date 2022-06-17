# Python for Data Science

## Admin

### Building the Book

To build the book using Jupyter books use

```bash
jupyter-book build .
```

Once this command is run, you should be able to look at the HTML files for the book locally on your computer.

Note that, due to package conflicts, several pages may not compile when taking this approach. One work around is to manually run troublesome notebooks and, when jupyter-book encounters a problem when executing them to build the book, it will pick up the notebook at the last point it was successfully manually executed. If you do have this problem, it may be that jupyter-book is not picking up the right jupyter kernel. You can look at installed kernels using `jupyter kernelspec list`.

### Uploading Built Files

Only upload built files based on a successful commit or merge to the main branch. See [here](https://jupyterbook.org/publish/gh-pages.html) for how to upload revised HTML files, but the key command is

```bash
ghp-import -n -p -f _build/html
```

Typically, only maintainers will need to upload built files.

### Pre-commit

To perform the pre-commit checks, use

```bash
pre-commit run --all-files
```
