from asclasses import *

Marcos = Programador("Marcos")
print(Marcos.getEquip())
print("### \n")

Macbook = Equipamento("Apple","Air")
Marcos.setEquip(Macbook)
print(Marcos.getEquip())
print("### \n")

print(f"Marca = {Marcos.getEquip().getMarca()} /// Modelo = {Marcos.getEquip().getModelo()}")
print("### \n")