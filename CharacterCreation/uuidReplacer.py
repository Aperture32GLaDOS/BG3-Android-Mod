import os
import uuid

with open("uuids.txt", "r") as file:
    toReplace = file.readlines()

replaceWith = []
for i in toReplace:
    replaceWith.append(str(uuid.uuid4()))

for root, dirnames, filenames in os.walk("./"):
    for filename in filenames:
        path = os.path.join(root, filename)
        with open(path, "r") as file:
            fileContent = file.read()
        for i in range(len(toReplace)):
            fileContent = fileContent.replace(toReplace[i].strip(), replaceWith[i])
        with open(path, "w") as file:
            file.write(fileContent)
