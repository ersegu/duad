# Agrupar empleados por departamento
# - Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, 
# cree un diccionario que agrupe los empleados por su departamento:

#INPUT: 

employees = [
            {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
            {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
            {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
            {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

department_list = ["Ventas", "TI", "RRHH"]
employees_per_dept = {}

for i in range(len(department_list)):
    temp_employee_list = []
    for employee in employees:
        if(employee["department"] == department_list[i]): 
            temp_employee_list.append({"name": employee["name"],"email":employee["email"]})
    employees_per_dept[department_list[i]] = temp_employee_list

print(employees_per_dept) 

