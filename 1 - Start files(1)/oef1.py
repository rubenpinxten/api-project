import json

with open("Start files/PythonCoursesTM.json") as json_file:
        courses = json.load(json_file)

for course in courses["courses"]:
    print(course["name"])

    for group in course["groups"]:
        print("\t" + group["name"], end="")

    print("\n")