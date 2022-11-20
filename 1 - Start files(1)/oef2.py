import json
groups = {}
with open("Start files/PythonCoursesTM.json") as json_file:
    # read out the file and parse the JSON object using the load() function:
    courses = json.load(json_file)
    for course in courses["courses"]:
        for group in course["groups"]:
            groups[group["name"]] = group["students"]

for group in sorted(groups):
    print(group + ": " + str(groups[group]) + " students")
    