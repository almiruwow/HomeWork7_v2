import os.path
import json

path_to_data = os.path.join('data')


def load_students():
    with open(os.path.join(path_to_data, 'students.json'), 'r') as file:
        content = file.read()
        json_data = json.loads(content)

    return json_data


def load_professions():
    with open(os.path.join(path_to_data, 'professions.json'), 'r') as file:
        content = file.read()
        json_data = json.loads(content)

    return json_data


def get_student_by_pk(pk):
    students = load_students()

    for student in students:
        if student['pk'] == pk:
            return student

    return None


def get_profession_by_title(title):
    professions = load_professions()

    for profession in professions:
        if profession['title'] == title:
            return profession

    return None


s = {
    "pk": 4,
    "full_name": "Jane Snake",
    "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]}

p = {
    "pk": 1,
    "title": "Testing",
    "skills": ["HTML", "CSS", "React", "JavaScript"]
}


def check_fitness(student, profession):

    student_set = set(student['skills'])
    profession_set = set(profession['skills'])

    has = list(profession_set.intersection(student_set))
    lacks = list(profession_set.difference(student_set))

    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": (100 / len(profession['skills'])) * len(has)
    }
