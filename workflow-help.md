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
(workflow-help)=
# Postscript: Getting Further Help

This book is not an island; there is no single resource that will allow you to master Python for Data Science. As you begin to apply the techniques described in this book to your own data, you will soon find questions that we do not answer. This section describes a few tips on how to get help, and to help you keep learning.

## Resources

Some other resources for learning are:

- [The Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Real Python](https://realpython.com/), which has excellent short tutorials that cover Python more broadly (not just data science)
- [freeCodeCamp's Python courses](https://www.freecodecamp.org/news/search?query=data%20science%20python), though take care to select one that's at the right level for you
- [Coding for Economists](https://aeturrell.github.io/coding-for-economists), which has similar content to this book but is more in depth and aimed at analysts (particularly in economics)

## Google is your friend

If you get stuck, start with Google. Typically adding "Python" or "Python Data Science" (as the Python ecosystem goes *well* beyond data science) to a query is enough to restrict it to relevant results. Google is particularly useful for error messages. If you get an error message and you have no idea what it means, try googling it! Chances are that someone else has been confused by it in the past, and there will be help somewhere on the web.

If Google doesn't help, try [Stack Overflow](http://stackoverflow.com). Start by spending a little time searching for an existing answer, including `[Python]` to restrict your search to questions and answers that use Python.

## In the loop

It's also helpful to keep an eye on the latest developments in data science. There are tons of data science newsletters out there, and we recommend keeping up with the Python data science community by following the (#pydata), (#datascience), and (#python) hashtags on Twitter.

## Making a reprex (reproducible example)

If your googling doesn't find anything useful, it's a really good idea prepare a minimal reproducible example or **reprex**.

A good reprex makes it easier for other people to help you, and often you'll figure out the problem yourself in the course of making it. There are two parts to creating a reprex:

- First, you need to make your code reproducible. This means that you need to capture everything, i.e., include any packages you used and create all necessary objects. The easiest way to make sure you've done this is to use the [**watermark**](https://github.com/rasbt/watermark) package alongside whatever else you are doing:

```{code-cell} ipython3
import pandas as pd
import numpy as np
import watermark.watermark as watermark

print(watermark())
print(watermark(iversions=True, globals_=globals()))
```

- Second, you need to make it minimal. Strip away everything that is not directly related to your problem. This usually involves creating a much smaller and simpler Python object than the one you're facing in real life or even using built-in data.

That sounds like a lot of work! And it can be, but it has a great payoff:

- 80% of the time creating an excellent reprex reveals the source of your problem. It's amazing how often the process of writing up a self-contained and minimal example allows you to answer your own question.

- The other 20% of time you will have captured the essence of your problem in a way that is easy for others to play with. This substantially improves your chances of getting help.

There are several things you need to include to make your example reproducible: Python environment, required packages, data, and code.

- **Python environment**--really just the Python version. This is covered by the first call to the **watermark** package.

- **Packages** and their versions. These should be loaded at the top of the script, so it's easy to see which ones the example needs. By using **watermark** with the above configuration, you will also print the package versions. This is a good time to check that you're using the latest version of each package; it's possible you've discovered a bug that's been fixed since you installed or last updated the package.

- **Data**: as others won't be able to easily download the data you're working with, it's often best to create a small amount of data from code that still have the same problem as you're finding with your actual data. Between **numpy** and **pandas**, it's quite easy to generate data from code; here's an example:

```{code-cell} ipython3
df = pd.DataFrame(
    data=np.reshape(range(36), (6, 6)),
    index=["a", "b", "c", "d", "e", "f"],
    columns=["col" + str(i) for i in range(6)],
    dtype=float,
)
df["random_normal"] = np.random.normal(size=6)
df
```

- **Code**: copy and paste the minimal reproducible example code (including the packages, as noted above). Make sure you've used spaces and your variable names are concise, yet informative. Use comments to indicate where your problem lies. Do your best to remove everything that is not related to the problem. Finally, the shorter your code is, the easier it is to understand, and the easier it is to fix.

Finish by checking that you have actually made a reproducible example by starting a fresh Python session and copying and pasting your reprex in.
