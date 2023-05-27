# Ejemplo de MT

Vamos a construir usando la biblioteca automata la MT que decide el lenguaje:

```
Sea Σ = { a, b, c], Suma ⊆  Σ∗},
L = { 2^3^#w | w ∈ Σ* }
```

## El diagrama de Transiciones para una Máquina de Turing que Decide el Lenguaje

![Maquina de Turing Suma](assets/images/suma.jpg)

## Instrucciones

Instalar:

- python 3.9 o superior
- pip
- virtualenv

La primera vez en windows (en linux se activa con ". venv/bin/activate" ):

```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Para ejecutar

Antes de arrancar a trabajar hay que activar el entorno virtual

En Windows:  

```
venv\Scripts\activate.bat
```

En Linux:  

```
. venv/bin/activate
```

Una vez activado el entorno virtual corremos los tests:  

```
python -m pytest
```

### Usar desde consola del SO

```bash
python suma.py
```

Tipeamos las cadenas y luego de apretar enter imprime ACEPTA o RECHAZA.

Podemos usar con un archivo con un conjunto de casos:

```bash
python suma.py < casos.txt
```

Si nos gustaría ver paso a paso lo que pasa con todas las configuraciones y el historial de computo completo:

```bash
python suma.py --debug
```

### Usar desde consola de python

```python
import suma

suma.evaluar('aabbcccc')
```

Devuelve True cuando acepta y False cuando rechaza.

Para poder observar el historial de cómputo, llamar a evaluar con True en el segundo parámetro:

```python
import suma

suma.evaluar('aabbcccc', True)
```

### Probar con pytest

pytest es una biblioteca de python que nos permite ejecutar pruebas.

Desde el entorno virtual ejectuar:

```
python -m pytest
```

## Licencia

Esta obra fue elaborada por [Miguel Carboni](https://github.com/miguelius) y publicada bajo una [Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional][cc-by-sa]. Podes usarla libremente citando la fuente. Y sí, no es gran cosa, pero de esta forma se cubre si alguno la registra y después me quiere cobrar por usarla...

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/deed.es
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
