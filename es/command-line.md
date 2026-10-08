# La línea de comandos {#sec-command-line}

En este capítulo conocerás la *línea de comandos* y aprenderás a usarla. Aparte de unos pocos comandos clave como `uv add <packagename>`, no necesitas saber usar la línea de comandos para seguir el resto de este libro. Sin embargo, incluso un poquito de conocimiento de la línea de comandos rinde mucho al programar y te será muy útil.

Para probar en tu máquina cualquiera de los comandos de este capítulo, puedes seleccionar 'New Terminal' en la barra de menús de Visual Studio Code (Mac y Linux), usar el Windows Subsystem for Linux o git bash (Windows), o usar una [terminal en línea](https://cocalc.com/doc/terminal.html) gratuita.

Este capítulo se ha beneficiado de numerosas fuentes, incluidas las excelentes notas de [Grant McDermott](https://grantmcdermott.com/), [Introduction to Cultural Analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html) de Melanie Walsh, [Data Science Bootstrap](https://ericmjl.github.io/data-science-bootstrap-notes/), [calmcode.io](https://calmcode.io/) y [Research Software Engineering with Python](https://merely-useful.tech/py-rse/). Un recurso prometedor que, en el momento de escribir esto, aún se estaba compilando es [Data Science at the Command Line](https://www.datascienceatthecommandline.com/2e/).

## ¿Qué es la línea de comandos?

La línea de comandos es una forma de dar instrucciones de texto directamente a una computadora, una línea a la vez (a diferencia de una interfaz gráfica de usuario, o GUI, por la que navegas con el ratón). Recibe muchos nombres: shell, bash, terminal, CLI y línea de comandos. En realidad son cosas distintas, pero la mayoría de la gente suele usarlas como sinónimos casi siempre. El *shell* es la parte de un sistema operativo con la que interactúas, aunque la mayoría usa shell para referirse a la línea de comandos. *bash* es el lenguaje de programación que se usa en la línea de comandos; en realidad es el acrónimo de 'Born Again SHell'. *Terminal* se usa a veces para referirse a la línea de comandos en Mac. Por último, *CLI* es simplemente el acrónimo de command line interface (interfaz de línea de comandos), y se usa a menudo en el contexto de una aplicación; por ejemplo, uv tiene una interfaz de línea de comandos porque lo ejecutas en la línea de comandos para instalar paquetes (`uv add packagename`).

Vale la pena mencionar que hay una gran diferencia entre la línea de comandos de los sistemas basados en UNIX (MacOS y Linux) y la de los sistemas Windows. Aquí solo trataremos la versión UNIX. Windows tiene una línea de comandos, pero no se usa mucho para programar. Si usas una máquina con Windows, puedes acceder a una línea de comandos UNIX mediante el Windows Subsystem for Linux.

## ¿Por qué es útil la línea de comandos?

La línea de comandos tiene muchos usos. Las interfaces gráficas de usuario son, en general, un poco más fáciles de usar, *pero* no son muy repetibles ni escalables. Como la línea de comandos usa instrucciones de texto y se puede programar, es repetible y escalable, propiedades muy útiles para la investigación y el análisis.

Las razones generales por las que podrías usar la línea de comandos para dar instrucciones incluyen:

- funcionalidad del software: algunos programas *solo* tienen interfaz de línea de comandos

- eficiencia: tu computadora tiene memoria limitada, y las interfaces gráficas usan mucha; la línea de comandos usa menos

- reproducibilidad: los scripts que se ejecutan en la línea de comandos son reproducibles de una forma en que hacer clic en una interfaz gráfica no lo es

- funcionalidad del hardware: en la computación de alto rendimiento y en la nube, la línea de comandos suele ser la única opción

- automatización: varios programas, con entradas y salidas, pueden ejecutarse en secuencia desde un script lanzado en la línea de comandos

Estas son algunas tareas concretas para las que podrías usar la línea de comandos:

- mantener tu código bajo control de versiones

- renombrar y mover varios archivos con un solo comando

- buscar archivos en la computadora

- convertir entre tipos de documento, por ejemplo de $\LaTeX$ (.tex) a Word (.docx)

- conectarte a recursos en la nube y usarlos

## Uso de la línea de comandos

Bash suele ser el shell predeterminado en UNIX, pero zsh ha ganado popularidad y ahora es el predeterminado en Mac. Si te preguntas cuál usar, te recomiendo zsh (Z Shell) de [oh-my-zsh](https://ohmyz.sh/).

Para abrir la línea de comandos dentro de Visual Studio Code, puedes usar el atajo de teclado <kbd>⌃</kbd> + <kbd>\`</kbd> (en Mac) o <kbd>ctrl</kbd> + <kbd>\`</kbd> (Windows/Linux), o hacer clic en "View > Terminal".

Ahora deberías ver algo como esto

```bash
username@hostname:~$
```

Veamos qué nos dice esto. `username` indica quién es el usuario actual; `@hostname` denota el nombre de la computadora; `~` es el directorio predeterminado (home); y `$` es el 'prompt de comandos', una señal de que aquí es donde debes escribir tu comando. (Ten en cuenta que esta línea puede verse distinta según el shell y/o el sistema operativo que uses).

Probemos un comando sencillo: escribe `date` en una ventana de línea de comandos y pulsa Enter. Deberías ver la fecha y hora actuales (y la zona horaria). También puedes probar `echo hello` y `whoami`.

Todos los comandos que ejecutas en la terminal tienen la misma estructura:
`command`, seguido de `option(s)`, seguido de `argument(s)`. Las opciones también se llaman flags. Un ejemplo sirve para demostrarlo: si tienes una terminal abierta en un directorio que incluye un archivo CSV llamado 'data.csv', el comando para ver las primeras 5 líneas es:

```bash
head -n 5 data.csv
```

aquí `head` es el comando que muestra el inicio del archivo, `-n` es una opción, `5` es el argumento para obtener 5 líneas del archivo y `data.csv` es el argumento final: el nombre del archivo.

Los flags u opciones, como `-n` en el ejemplo anterior, suelen empezar con un guion (`-`) u, ocasionalmente, con un guion doble (`--`). También se pueden encadenar; por ejemplo, `ls -la` combina `ls -a` y `ls -l`.

::: {.callout-warning}
Los espacios cumplen una función especial cuando usas la línea de comandos. Por eso, es buena práctica evitar los espacios en los nombres de archivo. Si necesitas referirte a un nombre de archivo que contiene espacios, tendrás que usar comillas o escapar los espacios del nombre con una `\`; por ejemplo, `this is my file.txt` se convierte en `this\ is\ my\ file.txt`
:::

Para ejecutar programas desde la línea de comandos, solo necesitas el nombre del programa como comando: de hecho, los comandos *son* programas. El comando `date` hace referencia a un programa real en tu computadora que puedes encontrar. Y esto también explica un poco lo que ocurre cuando *ejecutas un script desde la línea de comandos* (más sobre esto después).

Después de ejecutar algunos comandos, notarás que no puedes moverte por la línea de comandos como lo harías en un archivo de texto o un script de Python. Estos son algunos consejos para moverte por la línea de comandos:

- usa el tabulador para completar comandos que solo has escrito parcialmente. Pruébalo escribiendo `dat` y pulsando el tabulador.

- usa las teclas <kbd>↑</kbd> y <kbd>↓</kbd> para recorrer los comandos anteriores.

- para saltar palabras completas, usa <kbd>⌥</kbd> + <kbd>→</kbd> y <kbd>⌥</kbd> + <kbd>←</kbd> en Mac, o <kbd>ctrl</kbd> + <kbd>→</kbd> y <kbd>ctrl</kbd> + <kbd>←</kbd> en Windows y Linux.

- <kbd>ctrl</kbd> + <kbd>a</kbd> para mover el cursor al inicio de la línea.

- <kbd>ctrl</kbd> + <kbd>e</kbd> mueve el cursor al final de la línea.

- <kbd>ctrl</kbd> + <kbd>k</kbd> para borrar todo lo que está a la derecha del cursor.

- <kbd>ctrl</kbd> + <kbd>u</kbd> para borrar todo lo que está a la izquierda del cursor.

- <kbd>ctrl</kbd> + <kbd>r</kbd> para buscar entre los comandos usados anteriormente

### Navegar entre directorios

Ya que hablamos de navegar, es útil entender *en qué lugar* de la computadora estás cuando abres la línea de comandos. Si abres un panel de terminal dentro de VS Code, empezarás (al menos por defecto) en la misma carpeta que tu proyecto. Si abres una terminal fuera de VS Code, empezarás en un directorio raíz de tu computadora; por ejemplo, en Mac, al abrir una nueva ventana de terminal empiezas en `/Users/yourusername/`.

Para saber "dónde" estás al abrir una terminal, puedes usar el comando `pwd`, que significa "print working directory" (mostrar el directorio de trabajo).

La siguiente tabla muestra algunos comandos útiles para moverte por tu computadora con la línea de comandos. Ten en cuenta que `cd` acepta una ubicación *relativa* a tu directorio actual.

  | Comando               | Qué hace                                                     |
  | --------------------- | ------------------------------------------------------------ |
  | `pwd`                 | Muestra el directorio actual                                 |
  | `cd`                  | Comando para cambiar de directorio                           |
  | `cd ..`               | Sube un nivel en el directorio (`cd ../..` para dos niveles) |
  | `cd ~`                | Va a tu directorio home                                      |
  | `cd -`                | Va al directorio anterior                                    |
  | `cd documents/papers` | Va directamente a un directorio llamado 'papers'             |

## Uso de Python en la línea de comandos

La línea de comandos es útil para Python de varias formas (y también se aplican a otros lenguajes).

Por supuesto, los paquetes se instalan desde la línea de comandos; por ejemplo, para instalar Jupyter Lab (para ejecutar notebooks), el comando es

```bash
uv add jupyterlab
```

Si tienes un script llamado `analysis.py`, puedes ejecutarlo con Python en la línea de comandos usando

```bash
uv run python analysis.py
```

que llama a Python como programa y le pasa `analysis.py` como argumento. Si tienes varias versiones de Python (lo cual deberías tener si sigues las buenas prácticas y usas una versión por proyecto), puedes ver *qué* versión de Python se está usando con

```bash
which python
```

## Comandos útiles para la terminal

Ahora veremos algunos comandos útiles para la terminal.

  | Comando  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Qué hace                                                                                                                                                                 |
  | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
  | `man <command>`                                                                                                                                            | Muestra el manual del comando indicado                                                                                                                                   |
  | `touch <filename>`                                                                                                                                         | Crea un archivo vacío llamado `<filename>`                                                                                                                               |
  | `code <filename>`                                                                                                                                          | Abre un archivo en VS Code (y lo crea si no existe)                                                                                                                      |
  | `mkdir <foldername>`                                                                                                                                       | Crea una carpeta nueva llamada `foldername`                                                                                                                              |
  | `echo <text>`                                                                                                                                              | Imprime `<text>`                                                                                                                                                         |
  | `cat <filename>`                                                                                                                                           | Imprime todo el contenido de `<filename>`                                                                                                                                |
  | `head <filename>`                                                                                                                                          | Imprime el inicio de un archivo                                                                                                                                          |
  | `tail <filename>`                                                                                                                                          | Imprime el final de un archivo                                                                                                                                           |
  | `> <filename>`                                                                                                                                             | Redirige la salida de la pantalla a `<filename>`. Por ejemplo, `echo "Hello World" > hello.txt`                                                                          |
  | `>> <filename>`                                                                                                                                            | Redirige la salida de la pantalla al final de `<filename>`, es decir, añade la salida en lugar de sobrescribir el archivo                                                |
  | `                                                                                                                                                          | `                                                                                                                                                                        | El símbolo pipe: usa la salida de un comando como entrada de otro. Por ejemplo, `head -n 10 data.csv                                                     | > hello_world.txt` escribiría las primeras 10 líneas de data.csv en un archivo llamado hello_world.txt |
  | `less <filename>`                                                                                                                                          | Imprime el contenido de un archivo de forma paginada. Usa `ctrl+v` y `Alt+v` (o `⌘+v` y `⌥+v` en Mac) para desplazarte hacia arriba y hacia abajo. Pulsa `q` para salir. |
  | `wc -l`                                                                                                                                                    | Devuelve el número de líneas de la entrada, por ejemplo `cat <filename>                                                                                                  | wc -l`. Usa `wc` solo para contar palabras.                                                                                                              |
  | `sort`                                                                                                                                                     | Ordena alfabéticamente las líneas de un archivo                                                                                                                          |
  | `uniq`                                                                                                                                                     | Elimina las líneas duplicadas de la entrada, por ejemplo `cat <filename>                                                                                                 | uniq`, o `uniq -d` para mostrar los duplicados                                                                                                           |
  | `mv`                                                                                                                                                       | Mueve o renombra un archivo; por ejemplo, `mv file1 file2` renombraría `file1` a `file2`, mientras que `mv file1 ~` movería `file1` al directorio de inicio              |
  | `cp`                                                                                                                                                       | Copia un archivo; por ejemplo, `cp file1 file2` copiaría `file1` en `file2`, mientras que `cp file1 ~` haría una copia de `file1` en el directorio de inicio             |
  | `rm <filename>`                                                                                                                                            | Elimina un archivo de forma permanente                                                                                                                                   |
  | `rmdir <directory>`                                                                                                                                        | Elimina de forma permanente un directorio vacío                                                                                                                          |
  | `rm -rf <directory>`                                                                                                                                       | ⚠ Elimina de forma permanente todo lo que hay en un directorio ⚠                                                                                                         |
  | `grep <searchterm>`                                                                                                                                        | Busca un término dado, por ejemplo `cat hello_world.txt                                                                                                                  | grep world`                                                                                                                                              |
  | `ls`                                                                                                                                                       | Básicamente, significa listar el contenido (archivos y carpetas) del directorio actual                                                                                   |
  | `ls -a`                                                                                                                                                    | Lista el contenido del directorio actual, incluso lo oculto                                                                                                              |
  | `ls -l`                                                                                                                                                    | Lista el contenido en un formato más legible y muestra los permisos                                                                                                      |
  | `ls -S`                                                                                                                                                    | Lista el contenido por tamaño                                                                                                                                            |
  | `file <filename>`                                                                                                                                          | Da información sobre el tipo de archivo de `<filename>`                                                                                                                  |
  | `find`                                                                                                                                                     | Busca archivos concretos en tu computadora; se puede encadenar con otros comandos mediante pipe, por ejemplo `find *.md -size +5k -type f                                | xargs wc -l` contará el número de líneas (`wc -l`) de todos los archivos (`-type f`) que terminan en `.md` y que pesan más de 5 kilobytes (`-size +5k`). |
  | `diff -u <filename1> <filename2>`                                                                                                                          | Muestra un único resumen de las diferencias entre dos archivos.                                                                                                          |

![Más detalles del comando grep](https://pbs.twimg.com/media/DcPeD_CW0AEkSar?format=jpg&name=small)
*Más detalles del comando grep, por [\@b0rk](https://twitter.com/b0rk).*

Puedes escribir bucles for en bash (recuerda que es un lenguaje). La estructura general es

```bash
for i in LIST
do
  OPERATION $i # the $ sign indicates a variable in bash
done
```

Se pueden condensar en una sola línea (aunque resulta menos legible):

```bash
for i in {1..5}; do echo $i; done
```

Un ejemplo más interesante es obtener el número de líneas de texto, el número de palabras y el número de caracteres de cada archivo CSV de un directorio:

```bash
for i in $(ls *.csv)
do 
  wc $i
done
```

Podemos sofisticar aún más el ejemplo anterior y guardar esos recuentos en un nuevo archivo de texto:

```bash
touch counts_of_csvs.txt
for i in $(ls *.csv)
do
  wc $i >> counts_of_csvs.txt
done
```

En los ejemplos anteriores aparecieron un par de características nuevas.

`*` es un *carácter comodín*: le indica a bash que busque cualquier cosa que termine en ".csv". No es el único caso especial; `?` cumple una función similar, pues sustituye a cualquier carácter, pero solo a *uno* en lugar de a un número arbitrario. Si tuvieras una carpeta con `file1.csv`, `file2.csv`, etc., hasta el 9, podrías usar `file?.csv` para referirte a todos ellos, pero esto no incluiría `file10.csv`.

Otro carácter especial que ya hemos visto son las llaves, `{}`. Cuando tienes una subcadena común en una serie de comandos, usar llaves le indica a la línea de comandos que expanda automáticamente lo que contienen. En un ejemplo anterior, se usa con 1 a 5. Pero también se puede usar, por ejemplo, en nombres de archivo:

```bash
cp /path/to/project/{foo,bar,baz}.csv /newpath
```

copiaría los archivos csv llamados `foo`, `bar` y `baz` al directorio `/newpath`. De forma similar,

```bash
touch {a..c}{.csv,.txt}
```

crearía los archivos a.csv, a.txt, b.csv, b.txt, c.csv y c.txt.

## Scripting

Para tareas que se van a repetir, es más reproducible y fiable poner tus comandos de terminal en un script que ejecutarlos de memoria cada vez, ¡además de mucho más fácil! Como la línea de comandos tiene su propio lenguaje, podemos crear scripts que ejecuten comandos. Hay algunas diferencias entre bash y zsh, pero intentaremos que las pautas sean generales.

Crea un script llamado `hello_world.sh`. Dentro, escribe:

```bash
#!/bin/bash
echo "Hello World!"
```

La primera línea se llama shebang e indica con qué programa se deben ejecutar los comandos siguientes (sh significa cualquier shell compatible con Bash). El carácter `#` también indica un comentario. La segunda parte imprimirá un string en la pantalla. Ahora, según uses bash o zsh, ejecuta

```bash
bash hello_world.sh
# or
zsh hello_world.sh
```

Veamos un ejemplo más complejo:

```bash
#!/bin/bash
echo "Starting program at $(date)"
echo "Running program $0 with $# arguments
```

que produce

```bash
Starting program at Thu 25 Mar 2021 21:23:22 GMT
Running program hello_world.sh with 0 arguments
```

Observa que usar `"$(command)"` insertó la salida del comando en el string de texto. Para asignar variables en scripts de bash y zsh, usa la sintaxis `foo=bar` (sin espacios) y accede al valor de la variable con `$foo`.

Los strings se pueden definir con los delimitadores `'` y `"`, pero no son equivalentes. Los strings delimitados con `'` son literales y no sustituyen los valores de las variables, mientras que los delimitados con `"` sí lo hacen.

Bash y zsh tienen un par de características poco habituales en comparación con otros lenguajes debido a su uso. Una de ellas son las variables especiales predefinidas, una de las cuales vimos en el ejemplo anterior. Esta es una lista de algunas de las principales:

- `$0` - Nombre del script
- `$1` a `$9` - Argumentos del script (ordenados por número)
- `$@` - Todos los argumentos
- `$#` - Número de argumentos
- `!!` - Último comando completo, incluidos los argumentos

Puedes encontrar más variables especiales [aquí](https://tldp.org/LDP/abs/html/special-chars.html).

## Herramientas útiles de línea de comandos

[**pandoc**](https://pandoc.org/) es absolutamente genial: si necesitas convertir archivos de texto de un formato a otro, es una auténtica navaja suiza. Aquí no hay espacio para enumerar la enorme cantidad de formatos entre los que puede convertir, pero, lo más importante, puede traducir en ambos sentidos entre todos los siguientes: markdown, $\LaTeX$, docx de Microsoft Word, ODT de OpenOffice, HTML y Jupyter Notebook.

También puede convertir desde cualquiera de esos formatos (y más), en un solo sentido, *a* PDF, Microsoft Powerpoint y $\LaTeX$ Beamer.

Para usar **pandoc**, instálalo siguiendo las instrucciones del sitio web y luego llámalo así:

```bash
pandoc mydoc.tex -o mydoc.docx
```

Este es un ejemplo en el que la entrada es un documento .tex y la salida, `-o`, es un archivo docx de Microsoft Word.

Puedes hacer cosas bastante sofisticadas con **pandoc**; por ejemplo, puedes traducir un libro entero en latex a un documento de Word, con estilo de Word, bibliografía mediante biblatex, ecuaciones y figuras. Nada puede evitar que Word sea un suplicio, pero **pandoc** sin duda ayuda.

[**eza**](https://eza.rocks/) es una mejora del comando `ls`. Está diseñado para ser un listador de archivos mejorado, con más funciones y mejores valores predeterminados. Usa colores para distinguir los tipos de archivo y los metadatos. Sigue las instrucciones del sitio web para instalarlo en tu sistema operativo. Para reemplazar `ls` por `eza`, puedes usar un *alias* de terminal. Hay una buena guía [disponible aquí](https://denisrasulev.medium.com/eza-the-best-ls-command-replacement-9621252323e).

**nano** es un editor de texto integrado que se ejecuta *dentro* de la terminal. Puede ser muy útil si trabajas en la nube (aunque no tiene las funciones avanzadas de un editor de texto con interfaz gráfica como VS Code). Para abrir un archivo con **nano**, el comando es `nano file.txt`. Nano muestra instrucciones de navegación al cargarse, pero salir es lo más difícil: cuando termines, pulsa `Ctrl+X`, luego `y` para guardar y después `enter` para salir.

[**wget**](https://www.gnu.org/software/wget/) es una utilidad de línea de comandos para descargar archivos de internet. Es muy sencilla de usar; la sintaxis es simplemente `wget [options] [url]`. Por ejemplo, para descargar el archivo csv de starwars usado en este libro, el comando es

```bash
wget https://github.com/aeturrell/coding-for-economists/blob/main/data/starwars.csv
```

[**htop**](https://htop.dev/) es una herramienta que te permite ver qué procesos se están ejecutando en tu computadora en cualquier momento (en cada procesador) y cuánta memoria estás usando. Para instalarla en un Mac, puedes usar `brew install htop` si usas homebrew. Si no, puedes compilarla desde el código fuente tras descargarla del sitio web. Para usarla, simplemente escribe `htop` en la línea de comandos.

[**ncdu**](https://dev.yorhel.nl/ncdu) es un analizador de uso de disco. Informa, de forma interactiva y a través de la terminal, cuánto espacio ocupa el contenido de una carpeta. También puedes pulsar Intro para entrar en una carpeta y explorar sus subcarpetas. Esto es especialmente útil cuando usas una computadora remota que no puedes ver mediante una interfaz gráfica de usuario (GUI).

[**ffmpeg**](https://www.ffmpeg.org/) es una herramienta de línea de comandos que pretende "decodificar, codificar, transcodificar, multiplexar, demultiplexar, transmitir, filtrar y reproducir prácticamente cualquier cosa que humanos y máquinas hayan creado. Admite desde los formatos antiguos más oscuros hasta los más punteros". Consulta la documentación para ver todos sus usos.

[**yank**](https://github.com/mptre/yank) lee la entrada de stdin (lo que ves en la terminal) y muestra una interfaz de selección que permite seleccionar un campo y copiarlo al portapapeles. Un caso de uso típico sería copiar y pegar un nombre de archivo que has encontrado con el comando `ls`. Por ejemplo, ejecutar `ls -lah | yank` en un directorio muestra una lista de permisos, tamaños, usuarios, fechas de modificación y nombres de archivos. Después puedes desplazarte con el teclado hasta el nombre de archivo que quieras, pulsar Intro y tener ese nombre en el portapapeles, listo para pegarlo en tu siguiente comando de terminal. Hay una buena demostración [aquí](https://calmcode.io/cool-cli/yank.html).

Para saber más sobre la línea de comandos, consulta [The Art of the Command Line](https://github.com/jlevy/the-art-of-command-line). En cuanto a otros comandos, quizá te interese echar un vistazo a `patch`, `sed` y `awk`.
