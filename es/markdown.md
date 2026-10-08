# Markdown {#sec-markdown}

## Introducción

En este capítulo conocerás el lenguaje de marcado ligero llamado *Markdown*, muy popular en muchas aplicaciones relacionadas con la programación y en el análisis reproducible. Como ejemplo de sus muchos usos, ¡este capítulo está escrito en markdown!

## Requisitos previos

Aunque puedes escribir markdown en cualquier editor de texto plano, este libro recomienda [Visual Studio Code](https://code.visualstudio.com/) como editor de markdown. También puede renderizar los archivos markdown abiertos para que veas cómo quedará el producto final; necesitarás instalar las extensiones **Markdown All in One** y **Markdown Preview Enhanced** y luego hacer clic derecho dentro de un archivo markdown (extensión `.md`) y elegir *Markdown Preview Enhanced: Open Preview to the Side*.

Si no usas Visual Studio Code, puedes experimentar con Markdown en las celdas de texto de los Jupyter Notebooks en JupyterLab, en las celdas de texto de los notebooks de Google Colab, o en línea mediante [Dillinger](https://dillinger.io/), un entorno en línea de edición de markdown en vivo.

### Introducción a Markdown

Markdown es diferente del software de preparación de documentos «lo que ves es lo que obtienes» como Microsoft Word, porque la *entrada* (una forma de texto plano) se ve distinta de la *salida* renderizada. En Word, haces clic en botones para lograr el formato. Al escribir markdown, especificas los elementos de formato de tus documentos con instrucciones que son, más o menos, como código. Si conoces cómo se ven el HTML sin procesar y el HTML renderizado, es una idea similar (y HTML es en sí mismo un lenguaje de marcado). Ten en cuenta, sin embargo, que markdown básico no puede ejecutar código Python, aunque puedes incluir fragmentos de código en él, igual que podrías escribir algo de código en un documento de Word.

Markdown se creó para ser lo más legible posible, incluso mientras lo escribes. También es muy sencillo, con pocos comandos que recordar: la idea es que te concentres en escribir texto y no en el formato.

La extensión estándar para archivos que solo contienen markdown es `.md`, pero también puedes ver `.qmd` en el contexto de markdown con bloques de código ejecutable. Y también puedes encontrar markdown en las celdas de los notebooks de Jupyter (extensión de archivo `.ipynb`).

Hay muchas situaciones en las que markdown puede usarse para comunicar:

- programadores y científicos de datos suelen usar markdown para escribir documentos, por ejemplo la documentación de paquetes
- para crear sitios web, informes, diapositivas y artículos de investigación
- en las celdas de texto de los Jupyter Notebooks
- como formato base que herramientas como **pandoc** y **Quarto** pueden convertir en otros tipos de documentos
- ¡para escribir libros sobre ciencia de datos!

Algunas de las ventajas de markdown son:

- Los archivos markdown pueden abrirse con cualquier editor de texto plano
- Markdown es independiente del sistema operativo
- Markdown es muy legible, incluso sin renderizar
- Muchos sitios web admiten la sintaxis markdown, por ejemplo Github (llamado Github-flavoured markdown) y Reddit

El resto de este capítulo cubrirá la mayor parte de la sintaxis de markdown.

#### La sintaxis de Markdown

##### Encabezados

Repasemos lo básico de markdown. Por ejemplo, una sola almohadilla (`#`) indica el título de un documento, así:

```markdown
# Heading
```

El siguiente nivel de subencabezado se especifica con dos almohadillas, así:

```markdown
## Sub-heading
```

Cada nivel siguiente de encabezado se hace sucesivamente más pequeño, por ejemplo:

```markdown

### Phylum

#### Class

##### Order

###### Family

```

se convierte en

### Filo

#### Clase

##### Orden

###### Familia

Si usas Visual Studio Code y estás en el panel del explorador, puedes ver el esquema (la estructura de encabezados y subencabezados) de tu documento markdown en el desplegable 'outline'.

### Sintaxis en línea

Estas son otras características de sintaxis comunes que necesitarás:

- para crear texto en *cursiva*, se usa `*un asterisco a cada lado del texto*` 
- el texto en **negrita** se produce con `**dos asteriscos**`
- la ***negrita cursiva*** es `***tres asteriscos***`
- los enlaces se producen con corchetes para el texto y paréntesis para el hipervínculo, así `[texto](enlace)`
- el código en línea se muestra con comillas invertidas, así \`código\`
- `~~tachado~~` se ve así ~~tachado~~
- `^(superíndice)` crea ^(superíndice)
- Las matemáticas en línea se admiten encerrándolas entre signos de dólar, por ejemplo `${\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}}$`, que se renderiza como ${\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}}$
- Se admite Unicode, así que puedes escribir símbolos como ∰, al igual que emoji; una sintaxis como `:tada:` crea :tada:

### Sintaxis de bloques de texto

Las citas se logran añadiendo una flecha, `>`, a cada línea:

> ¡Aquí hay una cita!

Las listas sin orden se producen con `-` o `*` en líneas separadas, de modo que

```markdown
- first item
- second item
- third item
```

se convierte en

- primer elemento
- segundo elemento
- tercer elemento

Las listas ordenadas se crean simplemente escribiendo números sucesivos en líneas sucesivas:

```markdown
1. first item
2. second item
3. third item
```

se convierte en

1. primer elemento
2. segundo elemento
3. tercer elemento

Ambos tipos de lista pueden anidarse, de modo que

```markdown
- first item
  - sub-item
    - sub-sub-item
- second item
```

se convierte en

- primer elemento
  - subelemento
    - sub-subelemento
- segundo elemento

La sintaxis básica para crear tablas es

```markdown
| Cheese              | Country         | Cost per kg |
|---------------------|-----------------|-------------|
| Appleby's Cheshire  | UK              | £30         |
| Edam                | Netherlands     | £8          |
| Pélardon            | France          | £37         |
```

que se convierte en

  | Queso              | País         | Coste por kg |
  | ------------------ | ------------ | ------------ |
  | Appleby's Cheshire | Reino Unido  | £30          |
  | Edam               | Países Bajos | £8           |
  | Pélardon           | Francia      | £37          |

¡pero rara vez querrás escribirlas tú mismo! En la práctica, lo más fácil es exportar un archivo markdown desde un dataframe de **pandas** usando `df.to_markdown()` o usar el práctico sitio web [markdown table generator](https://www.tablesgenerator.com/markdown_tables).

Mientras que el código en línea se renderizaba con comillas invertidas, puedes renderizar bloques de código usando tres comillas invertidas y el nombre del lenguaje, así:

````markdown
```python
import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
```
````

que se renderiza como:

```python
import pandas as pd
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])
```

Observa que hay resaltado de sintaxis para los tipos de datos y las palabras clave reservadas. El resaltado de sintaxis admite una amplia variedad de lenguajes. Observa también que la sintaxis es bastante similar a la que se usa para los bloques de código que **Quarto** ejecutará cuando uses markdown para publicar informes automatizados (más sobre esto abajo).

Las matemáticas en bloque se renderizan con dobles signos de dólar, así:

```markdown
$$
{\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}}
$$
```

que se renderiza como

$$
{\displaystyle ds^{2}=\left(1-{\frac {r_{\mathrm {s} }}{r}}\right)^{-1}\,dr^{2}+r^{2}\,d\varphi ^{2}\,,}
$$

Para insertar imágenes, usa la estructura `![alt-text](url or filepath)`, por ejemplo

```markdown
![Logo of Python4DS](https://github.com/aeturrell/python4DS/blob/main/logo.png?raw=true)
```

produce

![Logo de Python4DS](https://github.com/aeturrell/python4DS/blob/main/logo.png?raw=true)

También puedes producir listas de tareas, por ejemplo:

```markdown
- [x] Finish chapter 1
- [ ] Edit chapter 2
- [ ] Launch book :rocket:
```

produce

- [x] Terminar el capítulo 1
- [ ] Editar el capítulo 2
- [ ] Lanzar el libro :rocket:

Las notas al pie se crean usando `[^1]` seguido de `[^2]`, y así sucesivamente, o con etiquetas relacionadas con el contenido como `[^note]`. Aquí se usan las tres: un ejemplo[^1], y otro[^2], mientras que la tercera está aquí[^note] y tiene una etiqueta en lugar de un número (que no puedes ver al renderizar). Tendrás que desplazarte hasta el final de la página para ver la información asociada a estas notas al pie, pero la sintaxis para rellenar su información es:

```markdown
[^1]: First footnote.
[^2]: Every new line in a footnote should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]: Named footnotes will still render with numbers instead of the text but allow easier identification and linking.
```

[^1]: Primera nota al pie.

    [^2]:

    Cada nueva línea en una nota al pie debe ir precedida de 2 espacios.  
    Esto te permite tener una nota al pie con varias líneas.

    [^note]:

    Las notas al pie con nombre se seguirán renderizando con números en lugar del texto, pero facilitan la identificación y el enlazado.

Por último, para insertar un salto de línea usa

```markdown
***
```

Para producir este salto de línea:

--------------------------------------------------------------------------------

### Otros recursos sobre Markdown

Hay muchos buenos recursos sobre markdown:

- la [guía de markdown de Reddit](https://www.reddit.com/wiki/markdown)
- la [guía de markdown de github](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- esta [hoja de referencia de markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
