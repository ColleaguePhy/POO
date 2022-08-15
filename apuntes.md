## Bienvenida e introducción
###  ¿Por qué aprender programación orientada a objetos?
* **Analizar:** Obervación - Entendimiento - Lectura
* **Plasmar:** Diagramas
* **Programar:** Programar lo que acabamos de diagramar

**Ventajas**
- Programar más rápido
- Dejar de copiar y pegar código
- Dejar un Programador Jr. 


+ **Encapsulamiento:** ocultar datos mediante código
+ **Abstracción:** es como se pueden representar los objetos en modo de código
+ **Herencia:** se crea una clase nueva a partir de una existente
+ **Polimorfismos:** propiedad que hace posible enviar mensajes sintácticamente iguales a objetos de tipos distintos.

### ¿Qué resuelve la programación orientada a objetos?
- Código muy largo
- Evita que todo se rompa si algo falla
- Facilita el mantenimiento del código
- Evita generar un código espaguitti. Aquél que tiene demasiadas sentencias de control anidadas. 

 *La POO nos ayudata a escribir código de una forma mucho más simple, con mejor mantenimiento y escalabilidad, solucionando problemas de la programación estructurada.*

 ### Paradigma orientado a objetos
**Paradigma:** es la teoría que nos ayudara con las bases y modelos para solucionar problemas.

#### Orientación a objetos
Modelas partes de la solucion de los problemas como objetos. (Perros en el registro de una veterinaria)

#### Se compone de cuatro elementos
* **Clases:** el molde de los objetos a crear. *Molde*
* **Propiedades:** las caracteristicas del molde. *Atributos*
* **Metodos:** las funciones que podra realizar el objeto creado con el molde. *Acciones*
* **Objetos:**es algo que tiene las propiedades y metodos. Se crea con el molde. *Instancia del molde*

 *La teoria es fundamental para entender la mejor forma para resolver problemas, ya que otros ya han pasado por tus problemas y han visto una forma simple de resolverla.*


### Lenguajes orientados a objetos
Java - PHP - Python - JavaScript - C# - Ruby - Kotlin

### Diagramas de Modelado
- **OMT:** Object Moeling Techniques, metodlogía para el análisis orientado a objetos
- **UML:** Unified Modeling Language, lenguaje de modelado unificado. Clases - Casos de uso - Objetos - Actividades - Iteraciones - Estados - Implementación.

## Orientación a objetos
### Objetos
Cuanto tengamos un problema lo primero que debemos hacer es **Identificar objetos**
- Tienen propiedades (sustantivos) y comportamientos (operaciones del objeto - Sustativos/verbos), sustantivos (nombre). 
- Pueden ser físicos y conceptuales

### Abstracción y Clases
Una **Clase** es un molde/modelo por el cual nuesttros objetos se van a construir y nos van a permitir generar más objetos. La **abstracción** es cuando separamos los datos de un objeto para generar un molde.

### Modularidad
**Modular:** dividir un sistema en partes más pequeñas y así crear módulos independientes. *Divides y venceras*
- Reutilizar 
- Evitar colapsos
- Mantenible
- Legibilidad
- Resolución rápida de problemas

Separar las clases en archivos diferentes

### ¿Qué es la herencia?
**Don't repear yourself**
- Promueve la reducción de duplicación en programación
- Toda pieza de información *nunca debe ser duplicada* debido a que la duplicación incrementa la dificultad en los cambios y evolución.

**Herencia**
- Creamos nuevas clases a partir de otras. Se establece una relación de padre e hijo.

Súperclase - Subclase
La superclase tiene todos los atributos en comun de las subclases las cuales heredan estos atributos de la clase padre.

## Clases, objetos y método constructor
### Creando nnuestas carpetas inciales
**Nota:** Para que en las VSC en las carpetas salga un icono se usa la extensión *Material Icon Theme*

### Definiendo clases en Java y Python
En **java** el nombre de los archivos es el mismo nombre de la clase.

### Objetos, método constructor y su sintaxis en código
Los objetos nos ayudan a crear instancia de una clase, el objeto es el resultado de lo que modelamos, de los parámetros declarados y usaremos los objetos para que nuestras clases cobren vida.

Los métodos constructores dan un estado inicial al objeto y podemos añadirle algunos datos al objeto mediante estos métodos. Los atributos o elementos que pasemos a través del constructor serán los datos mínimos que necesita el objeto para que pueda vivir.

### Objetos. Dando vida a nuestras clases en Java y Python
- **Java** trae por defecto el método constructor

### Declarando un método contructor en Python
**Métodos Mágicos**, estos métodos son llamados automáticamente y estrictamente bajo ciertas reglas. 
**El construcor** se declara unsado **__init__**. En relidad el que lo construye en **__new__** e **__init__** lo que hace es personalizar la instancia de la clase, osea lo que este dentro de **__init__** será lo primero en ejecutarse al crear un nuevo objeto de esta clase.

## Herencia
### Otros tipos de herencia
Las clases que esten siendo heredadas las llamaremos familias

## Encapsulamiento
Es hacer que un dato sea inviolable, inalterable cuando se le asigne un *modificador de acces*. No solo es ocultarlo sino protegerlo.

**Modificaciones de Acceso**
- **Public:** Es el más permisivo de todos, Accede a todo.
- **Protected:** Podra ser accedido por la clase, paquetes y subclases
- **Defaul:** Permite el acceso a nivel de clases de internas y paquetes (No podremos ver las herencias si ha de tener)
- **Private:** Solo podra ser modificado dentro de la clase.

## Polimorfismo
- Muchas formas
- Hay un metodo que se comparte entre varias clases, pero donde cada una le da el comportamiento que cada una necesita.
- **Construir metodos con el mismo nombre pero con comportamientos diferentes**
- Un solo método puede tener un número de implementaciones diferentes
   

## En Resumen
En la POO hay 5 cosas fundamentales:

Clases: Son el molde más genérico y del cual podemos instanciar muchos objetos.
Objetos: Son creados de las clases y tienen datos y funcionalidad.
Atributos: Son las características especificas del objeto (Son las variables dentro del código)
Métodos: Son las funciones o acciones que puede hacer este objeto.
**Instaciar:**Es la creación de un objeto desde una clase a eso se le llama instancia o instancias.
Los pilares de la POO son:
Abstracción: Es separar cada uno de los datos de un objeto para poder crear su molde (clase)
Encapsulamiento: Es aislar un dato para que este sea privado y no pueda ser visto o modificado.
Herencia: Es crear una o más clases a partir de una clase que ya existe. Y se les llaman subclases.
**Polomorfismo:**Es construir métodos con el mismo nombre pero con comportamiento diferente.
