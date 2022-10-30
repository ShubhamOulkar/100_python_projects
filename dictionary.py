# Looping through a dictionary
student_score = {
    "Harry" : 81,
    "Ron": 78,
    "Hermione":99,
    "Draco": 74,
    "Neville":62,
}
student_grads = {}

for key in student_score:
    if student_score[key] > 90:
        student_grads[key] = "Outstanding"
        print(f"{key} grades are Outstanding.")
    elif student_score[key] > 80 and student_score[key] <= 90:
        student_grads[key] = "Exceeds Expectations"
        print(f"{key} grades are Exceeds Expectations.")
    elif student_score[key] > 70 and student_score[key] <= 80:
        student_grads[key] = "Acceptable"
        print(f"{key} scores are Acceptable.")
    else:
        student_grads[key] = "Fail"
        print(f"{key} is fail.")

print(student_grads)


# Nesting in dictionary
travel_log = [
{
"country":"France",
"visits":12,
"cities":["Paris","Lille","Dijon"]
},
{
"country":"Germany",
"visits":5,
"cities":["Berlin","Hamburg","Stuttgart"]
},
]

def add_new_country(cotry,visit,city):
    new_dict = {}
    key_list = ["Country","visits","cities"]
    new_dict[key_list[0]] = cotry
    new_dict[key_list[1]] = visit
    new_dict[key_list[2]] = city
    travel_log.append(new_dict)

add_new_country("Russia",2,["Moscow","Saint Petersburg"])

print(travel_log)
