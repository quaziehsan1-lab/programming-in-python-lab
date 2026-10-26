#11111111111
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]
def display_resources(resources):
    if resources == []:
        print("No resources found.")
    else:
        for resource in resources:
            print(resource)

def search_by_category(resources, category):
    found = False

    for resource in resources:
        if resource[2] == category:
            print(resource)
            found = True

    if found == False:
        print("No resources found.")

def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if found == False:
        print("No unavailable resources.")

display_resources(resources)

print("Electronics:")
search_by_category(resources, "Electronics")

print("Unavailable resources:")
find_unavailable(resources)

display_resources([])

#22222222222

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
    [206, "Rafi", [80, 80, 80]],
    [207, "Karim", [75, 105, 70]],
    [208, "Mina", []]
]


def calculate_average(marks):
    if marks == []:
        return 0

    total = 0
    for mark in marks:
        total = total + mark

    average = total / len(marks)
    return average


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        if marks == []:
            print(student_id, name, "No marks")
        else:
            valid = True

            for mark in marks:
                if mark < 0 or mark > 100:
                    valid = False

            if valid == False:
                print(student_id, name, "Invalid marks")
            else:
                average = calculate_average(marks)
                category = classify_performance(average)
                print(student_id, name, average, category)


display_report(students)