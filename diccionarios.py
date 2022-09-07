# los diccionarios son variables especiales que me permiten almacenar multiples dstos de diferente tipo en una sola variable
empleado={
    'nombre':"juan",
    'cedula': 122020112,
    'cargo':"analista de datos",
    'salario':8000000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,800000]
}
print(empleado)
print(empleado['deudas'][1])
# RECORRIENDO UN DICCIONARIO:
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)