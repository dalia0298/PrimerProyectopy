CALCULO DE IMC EN PYTHON
Como primer paso, se declaró un ciclo while para repetir el bloque de código en caso de que los datos ingresados no fueran válidos.

También se utilizó el bloque try-except, el cual evita que el programa falle si el usuario introduce texto en lugar de números al ingresar su edad, peso o estatura.

Se usó la sentencia if para verificar que los campos no estuvieran en blanco o que los valores no fueran negativos. De ser así, el ciclo while volvía a repetir las preguntas hasta que todos los campos estuvieran correctamente rellenados.

Se empleó la instrucción break para salir del ciclo infinito una vez que todos los datos ingresados eran válidos.

Después de que el usuario introduce sus datos correctamente, se realiza el cálculo del IMC (Índice de Masa Corporal) utilizando la fórmula
​
imc = peso / (estatura ** 2)
 
Finalmente, se despliega la información del usuario junto con el resultado del cálculo del IMC utilisando print
EJEMPLO DE SALIDA
Introduce tu nombre: Juan
Introduce tu apellido paterno: Pérez
Introduce tu apellido materno: Gómez
Introduce tu edad: 30
Introduce tu peso: 70
Introduce tu estatura: 1.75

📊 Tu IMC es: 22.86
✅ Datos guardados correctamente:
📝 Nombre: Juan
👤 Apellido Paterno: Pérez
👤 Apellido Materno: Gómez
🎂 Edad: 30 años
⚖️ Peso: 70 kg
📏 Estatura: 1.75 m
