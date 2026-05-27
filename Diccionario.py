# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# for key , value in alumno.items():
#     print(key,value)

# alumno["Email"]="s.ikari@nerv.gob"
# print()
# for key , value in alumno.items():
#     print(key,value)



productos={
    1:{"nombre":"Control Inalambrico", "Categoria": "Electronica", "precio": 45000},
    2:{"nombre":"Pilas Recargables", "Categoria": "Insumos", "precio": 5000},
    3:{"nombre":"Pasta Termica", "Categoria": "Computacion", "precio": 10000}
}


print(productos[2]["Categoria"])
print(productos[3]["precio"])
print(productos[1]["nombre"])