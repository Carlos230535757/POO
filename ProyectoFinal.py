import matplotlib.pyplot as plt

class Empleado:
  def __init__(self, nombre, estado):
    self.nombre = nombre
    self.estado = estado

  def __repr__(self):
    return f"Nombre: {self.nombre}, Estado: {self.estado}"

empleados = []

# Función para agregar un nuevo empleado
def agregar_empleado():
  nombre = input("Ingrese el nombre del empleado: ")
  estado = input("Ingrese el estado del empleado (trabajo/feriado): ")
  empleados.append(Empleado(nombre, estado))

# Función para imprimir el estado de todos los empleados y mostrarlo en un gráfico
def imprimir_estado():
  trabajo = 0
  feriado = 0
  for empleado in empleados:
    if empleado.estado == "trabajo":
      trabajo += 1
    elif empleado.estado == "feriado":
      feriado += 1
    print(empleado)
  # Mostrar gráfico de barras con el estado de los empleados
  labels = ["Trabajo", "Feriado"]
  data = [trabajo, feriado]
  plt.bar(labels, data)
  plt.show()

# Menú para interactuar con la clase Empleado
while True:
  print("Seleccione una opción:")
  print("1. Agregar empleado")
  print("2. Imprimir estado de empleados")
  print("3. Salir")
  opcion = input("Opción: ")
  if opcion == "1":
    agregar_empleado()
  elif opcion == "2":
    imprimir_estado()
  elif opcion == "3":
    break
  else:
    print("Opción inválida")

print("¡Hasta luego!")