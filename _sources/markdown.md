(markdown)=
# Markdown

## Introduction

In this chapter, you'll meet the lightweight markup language called *Markdown* that is very popular for lots of coding-related applications and in reproducible analysis. As an example of its many uses, this chapter is written in markdown!

## Prerequisites

Although you can write markdown in any plain text editor, this book recommends [Visual Studio Code](https://code.visualstudio.com/) as a markdown editor. It can also render markdown files that are open so you can see what the finished, output product will look like; you'll need to install the **Markdown All in One** and **Markdown Preview Enhanced** extensions and then either right-click within a markdown file (extension `.md`) and choose *Markdown Preview Enhanced: Open Preview to the Side*.

If you're not using Visual Studio Code, you can experiment with Markdown in the text cells of Jupyter Notebooks in JupyterLab, in the text cells of Google Colab notebooks, or online via [Dillinger](https://dillinger.io/), an online live-coding markdown environment.

### Introduction to Markdown

Markdown is different from What-You-See-Is-What-You-Get document preparation software such as Microsoft Word because the *input* (a form of plain text) looks different from the rendered *output*. In Word, you click buttons to achieve the same formatting. When writing markdown, you specify the formatting elements of your documents with instructions that are, more or less, like code. If you're familiar with how raw HTML and rendered HTML look, it's a similar idea (and HTML is itself a markup language). Note, however, that vanilla markdown cannot execute Python code even if you can include code snippets in it just as you could write down some code in a Word document.

Markdown was created to be as readable as possible, even when you are writing it. It's also very simple, with few commands to remember: the idea is that you should focus on writing text rather than formatting.

The standard extension for files that only contain markdown is `.md`, but you may also see `.qmd` in the context of markdown with executable code chunks. And you can find markdown in the cells of Jupyter notebooks (file extension `.ipynb`) too.

There are plenty of situations in which markdown can be used to communicate:

- coders and data scientists often use markdown to write documents, for example the documentation of packages
- to create websites, reports, slides, and research papers
- in the text cells of Jupyter Notebooks
- as a base format that tools like **pandoc** and **Quarto** can turn into other document types
- to write books about data science!

Some of the advantages of markdown are:

- Markdown files can be opened using by any plain text editor
- Markdown is operating system independent
- Markdown is very readable, even when not being rendered
- Many websites support markdown syntax, eg Github (called Github-flavoured markdown) and Reddit

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

but you will rarely want to write these out yourself! In practice, it's easiest to export a markdown file from a **pandas** data frame using `df.to_markdown()` or use the handy website, [markdown table generator](https://www.tablesgenerator.com/markdown_tables).

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

Note that there is syntax highlighting of data types and reserved keywords. The syntax highlighting supports a wide range of languages. Also note that the syntax is quite similar to what's used for code blocks that will be executed by **Quarto** when using markdown for publishing automated reports (more on this below).

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

To produce this line-break:

***

### Other Markdown Resources

There are plenty of good markdown resources out there:

- the [Reddit markdown guide](https://www.reddit.com/wiki/markdown)
- the [github markdown guide](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- this [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
