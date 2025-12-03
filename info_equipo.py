class Persona:
    def __init__(self, nombre, pais, descripcion):
        self.nombre = nombre
        self.pais = pais
        self.descripcion = descripcion

    def presentar(self):
        return f"Hola, mi nombre es {self.nombre} de {self.pais} y {self.descripcion}"

# Solicitudes al usuario
nombre = input("Ingresa tu nombre: ")
pais = input("Ingresa tu país: ")
descripcion = input("Escribe una breve descripción: ")

persona = Persona(nombre, pais, descripcion)
print(persona.presentar())