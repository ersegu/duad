#Ejercicio 5
#5. Dada `n` cantidad de notas de un estudiante, calcular:
    #a. Cuantas notas tiene aprobadas (mayor a 70).
    #b. Cuantas notas tiene desaprobadas (menor a 70).
    #c. El promedio de todas.
    #d. El promedio de las aprobadas.
    #e. El promedio de las desaprobadas.
#https://www.mclibre.org/consultar/python/lecciones/python-entrada-teclado.html

note_counter = 1
approved_notes = 0
failed_notes = 0
average_approved_notes = 0
average_failed_notes = 0
total_average = 0

notes_total = int(input("Enter the number of notes:\n"))

while(note_counter <= notes_total):
    current_note = int(input(f"Enter note number: {note_counter}\n"))
    if(current_note < 70):
        failed_notes = failed_notes + 1
        average_failed_notes = average_failed_notes + current_note
    else:
        approved_notes = approved_notes + 1
        average_approved_notes = average_approved_notes + current_note
    total_average = total_average + current_note
    note_counter = note_counter + 1


if(approved_notes == 0):
    average_approved_notes = 0
else:
    average_approved_notes = average_approved_notes / approved_notes

if(failed_notes == 0):
    average_failed_notes = 0
else:
    average_failed_notes = average_failed_notes / failed_notes


total_average = total_average / notes_total

print("The student has ", approved_notes, "approved notes")
print("The average of approved notes is: ",average_approved_notes)
print("The student has ", failed_notes," failed notes")
print("The average of failed notes is: ",average_failed_notes)
print("The total average is: ", total_average)



