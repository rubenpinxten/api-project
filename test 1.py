import json

json_course = '{"name":"API Development", "semester":"1"}'

course = json.loads(json_course)

print("Course name:" , course["name"])
print("Semester:", course["semester"])