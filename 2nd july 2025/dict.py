# dict practice questions
student = {
    "id": 101,
    "name": "Fatima",
    "marks": 88,
    "subjects": ["Math", "English", "Science"]
}
#1 Print the student’s name from the student dictionary.
print(student["name"])
#2 Add a new key called "grade" with the value "A" to the student dictionary.
student.update({"grade" : "A"})
print(student)
#3 Update the "marks" of the student to 92
student["marks"] = 92
print(student)
#4 Add another subject "History" to the student’s list of subjects.
student["subjects"] = ["Math", "English", "Science" , "History"]
#5 Remove the "id" key from the dictionary.
del student["id"]
print(student)
