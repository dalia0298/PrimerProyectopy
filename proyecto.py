while True:
    try:
        # Solicitar datos al usuario 
        nombre = input("Introduce tu nombre: ")
        Apellido_Paterno = input("Introduce tu apellido paterno: ")
        Apellido_Materno = input("Introduce tu apellido materno: ")
        edad = int(input("Introduce tu edad: "))
        peso = float(input("Introduce tu peso: "))
        estatura = float(input("Introduce tu estatura: "))
          # Validar que los datos no esten Vacios o sean negativos
        if nombre == "" or Apellido_Paterno == "" or Apellido_Materno == "" or edad <= 0 or peso <= 0 or estatura <= 0:
            print("Error, los datos no pueden estar vacíos o ser negativos.")
        else:
            break  # Datos correctos, salir del bucle
    except ValueError:
        print("Error: asegúrate de introducir números válidos para edad, peso y estatura.")

        # Calcular elIMC
       # Calcular IMC
imc = peso / (estatura ** 2)


# Mostrar los datos
print("✅ Datos guardados correctamente:")
print(f"📝 Nombre: {nombre}")
print(f"👤 Apellido Paterno: {Apellido_Paterno}")
print(f"👤 Apellido Materno: {Apellido_Materno}")
print(f"🎂 Edad: {edad} años")
print(f"⚖️ Peso: {peso} kg")
print(f"📏 Estatura: {estatura} m")
print(f"📊 Tu IMC es: {imc:.2f}")



    