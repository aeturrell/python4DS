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
(quarto-and-markdown)=
# Quarto and Markdown

In this chapter, you'll meet the lightweight markup language called *Markdown* that is very popular for lots of coding-related applications. However, note that markdown cannot run code. For example, markdown is used to display the documentation for software packages and in the text cells of Jupyter Notebooks. Even this chapter is written in markdown!

You'll also get more in-depth with [**quarto**](https://quarto.org/) in this chapter, following a brief introduction in {ref}`workflow-writing-code`. Quarto markdown is a version of markdown that *can* run code blocks; it's a unified authoring framework for data science, combining your code, its results, and your prose commentary. Quarto markdown documents are fully reproducible and support dozens of output formats, like PDFs, Microsoft Word files, slideshows, and more.

## Markdown

This book recommends [Visual Studio Code](https://code.visualstudio.com/) as a markdown editor. It can also render markdown files that are open; you'll need to install the **Markdown All in One** and **Markdown Preview Enhanced** extensions and then either right-click within a markdown file (extension `.md`) and choose *Markdown Preview Enhanced: Open Preview to the Side*.

If you're not using Visual Studio Code, you can experiment with Markdown in the text cells of Jupyter Notebooks in JupyterLab, in the text cells of Google Colab notebooks, or online via [Dillinger](https://dillinger.io/), an online live-coding markdown environment.

### Introduction to Markdown

Markdown is different from What-You-See-Is-What-You-Get document preparation software such as Microsoft Word because the *input* (a form of plain text) looks different from the rendered *output*. In Word, you click buttons to achieve the same formatting. When writing markdown, you specify the formatting elements of your documents with instructions that are, more or less, like code. If you're familiar with how raw HTML and rendered HTML look, it's a similar idea (and HTML is itself a markup language).

Markdown was created to be as readable as possible, even when you are writing it. It's also very simple, with few commands to remember: the idea is that you should focus on writing text rather than formatting.

The standard extension for files that only contain markdown is `.md`, but you may also see `.qmd` in the context of markdown with executable code chunks. And you can find markdown in the cells of Jupyter notebooks (file extension `.ipynb`) too.

There are plenty of situations where you may wish to use markdown:

- repositories for software or research paper replications
- to create websites, reports, and slides; see {ref}`auto-reports` for more on this
- in the text cells of Jupyter Notebooks; see {ref}`code-where` for more on this
- as a base format that tools like **pandoc** and **Quarto** can turn into other document types
- to write books about coding for economists!

Some of the advantages of markdown are:

- Markdown files can be opened using by any plain text editor
- Markdown is operating system independent
- Markdown is very readable, even when not being rendered
- Many websites support markdown syntax, eg Github (called Github-flavoured markdown) and Reddit.

The rest of this chapter will cover most of the markdown syntax.

#### The Markdown Syntax

##### Headings

Let's run through the basics of markdown. For example, a single hash (`#`) denotes the title of a document, like so:

```markdown
# Heading
```

The next level of sub-heading can be specified by two hashes, like this:

```markdown
## Sub-heading
```

Each next level heading gets successively smaller, for example:

```markdown

### Phylum

#### Class

##### Order

###### Family

```

becomes

### Phylum

#### Class

##### Order

###### Family

If you're using Visual Studio Code, and you're on the explorer panel, you can see the outline (the structure of headings and sub-headings) of your markdown document under the 'outline' drop down.

### In-Line Syntax

Here are some other common syntax features that you'll need:

- to create *italic* text, it's `*one asterisk on either side of the text*` 
- **bold** text is produced from `**two asterisks**`
- ***bold italic*** is `***three asterisks***`
- links are produced with square brackets for the text and parenthesis for the hyperlink, like this `[text](link)`
- in-line code is shown by backticks, like this \`code\`
- `~~strikethrough~~` looks like this ~~strikethrough~~
- `^(superscript)` creates ^(superscript)
- Maths is supported in-line via enclosing dollar signs, eg `${\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}}$`, which renders as ${\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}}$
- Unicode is supported, so you can write symbols like ∰, as are emoji; syntax like `:tada:` creates :tada:

### Text Block Syntax

Quotes can be achieved by adding an arrow, `>`, to every line:

> Here is a quote!

Unordered lists can be produced with either `-` or `*` on separate lines so that

```markdown
- first item
- second item
- third item
```

becomes

- first item
- second item
- third item

Ordered lists can be created by simply writing successive numbers on successive lines:

```markdown
1. first item
2. second item
3. third item
```

becomes

1. first item
2. second item
3. third item

Both types of list can be subsetted so that

```markdown
- first item
  - sub-item
    - sub-sub-item
- second item
```

becomes

- first item
  - sub-item
    - sub-sub-item
- second item

The basic syntax to create tables is

```markdown
| Cheese              | Country         | Cost per kg |
|---------------------|-----------------|-------------|
| Appleby's Cheshire  | UK              | £30         |
| Edam                | Netherlands     | £8          |
| Pélardon            | France          | £37         |
```

which becomes

| Cheese              | Country         | Cost per kg |
|---------------------|-----------------|-------------|
| Appleby's Cheshire  | UK              | £30         |
| Edam                | Netherlands     | £8          |
| Pélardon            | France          | £37         |

but you will rarely want to write these out yourself! In practice, it's easiest to export a markdown file from a **pandas** dataframe using `df.to_markdown()` or use the handy website, [markdown table generator](https://www.tablesgenerator.com/markdown_tables).

While inline code was rendered with backticks, you can render code blocks using three backticks and the name of the language like so:

````markdown
```python
import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
```
````

which gets rendered as:

```python
import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
```

Note that there is syntax highlighting of data types and reserved keywords. The syntax highlighting supports a wide range of languages. Also note that the syntax is quite similar to what's used for code blocks that will be executed by **quarto** when using markdown for publishing automated reports (more on this below).

Display maths is rendered by double dollar signs, like so:

```markdown
$$
{\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}}
$$
```

which renders as

$$
{\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}\,,}
$$

To insert images, use the structure `![alt-text](url or filepath)`, for example

```markdown
![Logo of Python4DS](https://github.com/aeturrell/python4DS/blob/main/logo.png?raw=true)
```

produces

![Logo of Python4DS](https://github.com/aeturrell/python4DS/blob/main/logo.png?raw=true)

You can also produce task lists, for example:

```markdown
- [x] Finish chapter 1
- [ ] Edit chapter 2
- [ ] Launch book :rocket:
```

produces

- [x] Finish chapter 1
- [ ] Edit chapter 2
- [ ] Launch book :rocket:

Footnotes can be be created using `[^1]` followed by `[^2]`, and so on, or by content related ones like `[^note]`. Here are these three being used: one example[^1], and another[^2], while the third is here[^note] and has a label instead of a number (that you can't see when rendered). You'll need to scroll right to the bottom of the page to see the info associated with these footnotes, but the syntax for filling in their info is:

```markdown
[^1]: First footnote.
[^2]: Every new line in a footnote should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]: Named footnotes will still render with numbers instead of the text but allow easier identification and linking.
```

[^1]: First footnote.
[^2]: Every new line in a footnote should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]: Named footnotes will still render with numbers instead of the text but allow easier identification and linking.

Finally, to insert a line-break use

```markdown
***
```

To produce:

***

### Other Markdown Resources

There are plenty of good markdown resources out there:

- the [Reddit markdown guide](https://www.reddit.com/wiki/markdown)
- the [github markdown guide](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- this [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Quarto

Quarto is a unified authoring framework for data science, combining your code, its results, and your prose commentary. It can be used for everything from documents to presentations.

Quarto can run on inputs that include Jupyter Notebooks (`.ipynb`) and quarto markdown `.qmd` files. You will need to install Quarto on your computer.

Quarto markdown is designed to be used in three ways:

1.  For communicating to decision makers, who want to focus on the conclusions, not the code behind the analysis.

2.  For collaborating with other data scientists (including future you!), who are interested in both your conclusions, and how you reached them (i.e. the code).

3.  As an environment in which to *do* data science, as a modern day lab notebook where you can capture not only what you did, but also what you were thinking.

As you work through this chapter, and use Quarto in the future, keep the quarto [documentation](https://quarto.org/) close to hand.

### Quarto Markdown Basics

Note that some of this is similar for Jupyter Notebook files.

This is an example of the contents of a quarto markdown file:

````markdown
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---

For a demonstration of a line plot on a polar axis, see @fig-polar.

```{python}
#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'} 
)
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
````

It contains three important types of content:

1.  A **YAML header** surrounded by `---`s.
2.  **Chunks** of Python code surrounded by ```` ``` ````.
3.  Markdown mixed with simple text formatting like `# heading` and `_italics_`.

When you open an `.qmd` with a text editor you get a simple text file like in the example above. If you are using the Visual Studio Code [quarto extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) (recommended), you can hit render and see how the output will look.

In the 'raw' input quarto markdown file, `{python}` tells **quarto** that a code chunk is in Python and should be executed, and `jupyter: python3` tells **quarto** what installation of Jupyter Notebooks to use. If you're unsure what your installation of Jupyter is called, you can see a list by running `jupyter kernelspec list` on the command line.

Once you have saved a qmd file, you can either render it using the button in VS Code or on the command line using:

```bash
quarto render hello_quarto.qmd
```

to output a HTML file. The powerful combination of markdown and **quarto** doesn't just allow you to write markdown and output executed markdown: you can output a wide range of formats, including Word documents, PDFs (papers and beamer presentations), Powerpoint presentations, HTML slides, HTML pages. To switch to a different output format, the general syntax is `quarto render document.qmd --to docx` and so on.

### Jupyter Notebooks as an input to Quarto

The only thing you need to do to get quarto to render a Jupyter Notebook is to add the yaml header to the first cell as *raw text*. Note that when rendering an `.ipynb` Quarto will not execute the cells within the notebook by default (the presumption being that you already executed them while editing the notebook). If you want to execute the cells you can pass the --execute flag to render:

```bash
quarto render notebook.ipynb --execute
```

### Code Execution Options

Whether in notebooks or quarto markdown files, you have options for code blocks that are outlined in the table below.

| Option | Description |
|---|---|
| `eval` | Evaluate the code chunk (if false, just echos the code into the output). |
| `echo` | Include the source code in output |
| `output` | Include the results of executing the code in the output (true, false, or asis to indicate that the output is raw markdown and should not have any of Quarto’s standard enclosing markdown). |
| `warning` | Include warnings in the output. |
| `error` | Include errors in the output (note that this implies that errors executing code will not halt processing of the document). |
| `include` | Catch all for preventing any output (code or results) from being included (e.g. include: false suppresses all output from the code block). |
| `true` | True |
| `false` | False |

For example, a block that produces output—but for which the code is hidden— would be:

````markdown
```{python}
#| echo: false
print("Hello World! But don't show the code.")
```
````
