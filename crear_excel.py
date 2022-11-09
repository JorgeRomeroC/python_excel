import os.path
import pandas
from pandas import ExcelWriter

ruta = os.path.dirname(os.path.abspath(__file__))

datos = pandas.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "nombre": ["Juan", "Jorge", "Silvana", "Zoe", "Diego", "Jorgito"],
    "apellido": ["Romero", "Novoa", "Contreras", "Pérez", "Torres", "Martinez"]
})
datos = datos[['id', 'nombre', 'apellido']]

write = ExcelWriter(ruta+"/archivo.xlsx")

datos.to_excel(write, "Hoja 1", index=False)

write.save()