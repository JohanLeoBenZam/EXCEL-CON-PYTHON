import pandas as pd
import json
from datetime import date

with open("employees.json", "r") as archivo:
    data = json.load(archivo)
salary = []
age = []
name = []
gender = []
proyect = []
email = []
for employ in data:
    if employ["proyect"] != "GRONK":
        age.append(employ["age"])
        name.append(employ["name"])
        gender.append(employ["gender"])
        proyect.append(employ["proyect"])
        email.append(employ["email"])
        f = str(employ["salary"]).replace("$","")
        f = float(f.replace(",",""))
        if int(employ["age"])<30:
            salary.append(f"{f + f * 0.1:.2f}"+"€")
        else:
            salary.append(str(f)+"€")
datos = {
    'salary': salary,
    'age': age,
    'name': name,
    'gender': gender,
    'proyect': proyect,
    'email': email
}
df = pd.DataFrame(datos)
hoy = date.today()
nombre = f'pagos-empleados-{hoy.month}-{hoy.year}.xlsx'
df.to_excel(nombre, index=False)



