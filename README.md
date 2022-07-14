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

on your staged files. Ensure pre-commit reports all tests as having passed before committing.

## Running and Developing in the Docker Container

There is a dockerfile associated with this project. Pre-reqs
 To use it:

1. Pre-reqs: docker installed, VS Code installed, VS Code docker and remote explorer extensions installed.
2. Build the image from the file. Right click on the file in VS Code and select build
3. On the Docker tab of VS Code, right-click on the image and select 'Run Interactive'
4. On the remote explorer tab of VS Code, find the running dev container and select 'attach new window'. This will start up a new VS Code window in the running container
5. Within the new VS Code window, open the folder ("app/")
6. Do any development as required (see the instructions above)

If you wish to copy any files (eg the built HTML files) back to your local machine to check them, use

```bash
docker cp CONTAINER:app/_build/html/ temp_dir/
```

Note that seaborn is currently using a pre-release version so this is installed directly in the dockerfile.
