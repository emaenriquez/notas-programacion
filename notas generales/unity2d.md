 
# Desarrollo de videojuegos 2d con unity

## Introducción al 2D

Gráficos 2D
Los objetos gráficos en 2D se conocen como Sprites. Los sprites son texturas estándar, con técnicas especiales para combinar y administrar 
texturas para mayor eficiencia y comodidad durante el desarrollo. 

Rigidbody 2D, Box Collider 2D y Hinge Joint 2D

# Creación de un juego en 2D
Antes de crear un juego en 2D, debes decidir la perspectiva del juego y el estilo artístico.

Para crear un juego 2D, configura tu proyecto de Unity y luego familiarízate con los conceptos relevantes en el siguiente orden:

- Fundamentos
- Scripting
- Sprites
- Creación de entornos en el juego
- Animación de personajes
- Grafismo
- Física 2D
- Audi
- Interfaz de usuario
- Perfilado, optimización y pruebas
- Editorial

## Fundamentals

### GameObjects (Objetos de juego)
son objetos fundamentales en Unity que representan personajes, accesorios, escenarios y más. Cada objeto de tu juego es un GameObject

El comportamiento de GameObjects está definido por bloques de funcionalidad llamados componentes. Los siguientes componentes son fundamentales para los juegos 2D:

#### Transform: el Componente de transformación determina la Posición, la Rotación y la Escala de cada GameObject en la escena. 
 ![Transform componente](https://docs.unity3d.com/uploads/Main/TransformExample4.png)
| Propiedad | Función                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------|
| Posición  | Posición de la transformación en las coordenadas x, y y z.                                   |
| Rotación  | Rotación de la transformada alrededor del eje x, el eje y y el eje z, medida en grados.       |
| Escala    | Escala de la transformación a lo largo del eje x, el eje y y el eje z. El valor "1" es el tamaño original (el tamaño al que importaste el GameObject)|



- Sprite Renderer:el componente Sprite Renderer renderiza el Sprite y controla cómo se ve en una escena.
Cameras: dispositivos que capturan y muestran el mundo al jugador

- Collider 2D: este componente define la forma de un GameObject 2D con fines físicos Colisiones


