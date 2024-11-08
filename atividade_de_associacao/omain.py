from asclasses import *

#INSTANCIANDO MOTORES:
Motor1 = Motor("V6","Ford")
Motor2 = Motor("V12","Chevrolet")
Motor3 = Motor("V8","Honda")

#INSTANCIANDO RODAS:
Roda1 = Roda(18,"Alpina")
Roda2 = Roda(15,"OZ Racing")

#INSTANCIANDO CARROS
Carro1 = Carro()
Carro1.setMotor(Motor1)
Carro1.setRoda(Roda1)
print(f"1° CARRO \nMOTOR = potencia do motor -> {Carro1.getMotor().getPotencia()} | marca do motor -> {Carro1.getMotor().getMarca()} /// RODA = tamanho da roda -> {Carro1.getRoda().getTamanho()} | marca da roda -> {Carro1.getRoda().getMarca()}\n")

Carro2 = Carro()
Carro2.setMotor(Motor3)
Carro2.setRoda(Roda2)
print(f"2° CARRO \nMOTOR = potencia do motor -> {Carro2.getMotor().getPotencia()} | marca do motor -> {Carro2.getMotor().getMarca()} /// RODA = tamanho da roda -> {Carro2.getRoda().getTamanho()} | marca da roda -> {Carro2.getRoda().getMarca()}\n")

Carro3 = Carro()
Carro3.setMotor(Motor2)
Carro3.setRoda(Roda2)
print(f"3° CARRO \nMOTOR = potencia do motor -> {Carro3.getMotor().getPotencia()} | marca do motor -> {Carro3.getMotor().getMarca()} /// RODA = tamanho da roda -> {Carro3.getRoda().getTamanho()} | marca da roda -> {Carro3.getRoda().getMarca()}\n")

Carro4 = Carro()
Carro4.setMotor(Motor2)
Carro4.setRoda(Roda2)
print(f"4° CARRO \nMOTOR = potencia do motor -> {Carro4.getMotor().getPotencia()} | marca do motor -> {Carro4.getMotor().getMarca()} /// RODA = tamanho da roda -> {Carro4.getRoda().getTamanho()} | marca da roda -> {Carro4.getRoda().getMarca()}\n")

Carro5 = Carro()
Carro5.setMotor(Motor3)
Carro5.setRoda(Roda1)
print(f"5° CARRO \nMOTOR = potencia do motor -> {Carro5.getMotor().getPotencia()} | marca do motor -> {Carro5.getMotor().getMarca()} /// RODA = tamanho da roda -> {Carro5.getRoda().getTamanho()} | marca da roda -> {Carro5.getRoda().getMarca()}\n")

Carro6 = Carro()
Carro6.setMotor(Motor1)
Carro6.setRoda(Roda1)
print(f"6° CARRO \nMOTOR = potencia do motor -> {Carro6.getMotor().getPotencia()} | marca do motor -> {Carro6.getMotor().getMarca()} /// RODA = tamanho da roda -> {Carro6.getRoda().getTamanho()} | marca da roda -> {Carro6.getRoda().getMarca()}\n")
