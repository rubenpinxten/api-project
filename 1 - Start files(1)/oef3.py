import json

room = "tekst"
list = []
while True:
    room = input("Room number: ")
    list.append(room)
    while room != "end":
        capacity = input("Capacity for " + room + ": ")
        list.append(int(capacity))
        blackboard = input("Blackboard available: ")
        if blackboard in ("y", "Y"):
            list.append(True)
        else:
            list.append(False)
        beamer = input("Beamer available: ")
        if beamer in ("y", "Y"):
            list.append(True)
        else:
            list.append(False)
        desktop = input("Desktop available: ")
        if desktop in ("y", "Y"):
            list.append(True)
        else:
            list.append(False)
        extra = input("Remarks: ")
        list.append(extra)
        print()
        dictionary = {
            "roomNumber": list[0],
            "capacity": list[1],
            "blackboard": list[2],
            "beamer": list[3],
            "desktop": list[4],
            "remarks": list[5]
        }
        list.clear()

        json_object = json.dumps(dictionary, indent=6)

        with open("test.json", "w") as outfile:
            outfile.write(json_object)

        room = input("Room number: ")
        list.append(room)

    exit()





