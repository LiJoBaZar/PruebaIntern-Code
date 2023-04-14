# PruebaIntern-Code

Este reto consiste en:

Definimos un árbol binario como un árbol de búsqueda binario con los siguientes requisitos de ordenación:

El valor de cada nodo en el subárbol izquierdo de un nodo es menor que el valor de los datos de ese nodo.
El valor de cada nodo del subárbol derecho de un nodo es mayor que el valor de los datos de ese nodo.
Dado el nodo raíz de un árbol binario, ¿puedes determinar si también es un árbol binario de búsqueda?

Completa en tu editor la siguiente función, que tiene como parámetro: un puntero a la raíz de un árbol binario. Debe devolver un booleano que denote si el árbol binario es o no un árbol binario de búsqueda. Puede que tengas que escribir una o más funciones de ayuda para completar este reto.

Formato de entrada

No es responsable de leer ninguna entrada desde stdin. Los stubs de código oculto ensamblarán un árbol binario y pasarán su nodo raíz a su función como argumento.

Restricciones

Formato de salida

No es responsable de imprimir ninguna salida a stdout. Su función debe devolver true si el árbol es un árbol binario de búsqueda; en caso contrario, debe devolver false. Los stubs de código oculto imprimirán este resultado como una respuesta Sí o No en una nueva línea.

Ejemplo de entrada

árbol

![Image of the challenge](https://github.com/LiJoBaZar/PruebaIntern-Code/blob/f1bd5513aa0859166ded8b753c65e426c3f5de0c/images/Entrada.png)

Ejemplo de salida

No

# SOLUCIÓN

Se crea un programa en Python que verifica si un árbol binario dado es un árbol de búsqueda binario válido. El programa utiliza una implementación de la clase Node para crear nodos de árbol binario y la función check_binary_search_tree_ para verificar si el árbol es un árbol de búsqueda binario válido.

# Cómo ejecutar el programa:

- Previa instalación Python 3.
- Ejecuta el comando python main.py en la terminal.
- Ejecuta el archivo .py
- Ingresa a solicitud en la terminal para ingresar los valores del árbol binario. Si el árbol es un árbol de búsqueda binario válido, la salida esperada es "Yes". De lo contrario, la salida esperada es "No".

# Cómo agregar valores al árbol binario

Para agregar valores al árbol binario, se deben seguir las instrucciones que aparecen en la terminal después de ejecutar el programa. Primero, ingresa el número de nodos que deseas agregar al árbol. Luego, ingresa los valores para cada nodo, uno a la vez. Los valores pueden ser números enteros positivos o negativos.

Por ejemplo, si deseas agregar los valores 5, 3, 7, 1 y 9 al árbol binario, debes ingresar los siguientes valores en la terminal:

![Image of the Enter](https://github.com/LiJoBaZar/PruebaIntern-Code/blob/f1bd5513aa0859166ded8b753c65e426c3f5de0c/images/Entrada.png)

En este caso, la lista contiene los valores del árbol binario en orden ascendente, lo que significa que el árbol binario es un árbol de búsqueda binario válido, y va a generar el siguiente arból:

![Image of the Eject](https://github.com/LiJoBaZar/PruebaIntern-Code/blob/6961d47922d382f6c170a4ad256fe5f39c0cfad3/images/Ejecutar.png)

Para este caso, la salida esperada es "Yes", ya que el árbol binario creado es un árbol de búsqueda binario válido, donde todos los valores en el subárbol izquierdo del nodo raíz son menores que el valor del nodo raíz, y todos los valores en el subárbol derecho del nodo raíz son mayores que el valor del nodo raíz.

![Image of the Verify binari false or true]([https://github.com/LiJoBaZar/PruebaIntern-Code/blob/6961d47922d382f6c170a4ad256fe5f39c0cfad3/images/FalseOrTrue.png](https://github.com/LiJoBaZar/PruebaIntern-Code/blob/aac5182d34c5fed0b843a2399bf367c11aab63c0/images/FalseOrTrue.png))

# Lenguaje utilizado: Python

Elegí Python como lenguaje de programación para este proyecto porque es un lenguaje de alto nivel de el cuál tengo conocimientos básicos y previos usos, fácil de leer y escribir. Además, tiene una gran cantidad de bibliotecas y herramientas disponibles que facilitan el desarrollo de programas. Python también es ampliamente utilizado en el campo de la ciencia de datos y la inteligencia artificial, lo que lo convierte en una excelente opción para proyectos de programación relacionados con estos temas.

## Autor

<a target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" height="30" width="40" /></a> [Johanna Balcazar](https://www.linkedin.com/in/johanna-balcazar-696554240/)


<a href = 'https://github.com/Luiyi-F'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg" /></a> [Johanna Balcazar](https://github.com/LiJoBaZar)
