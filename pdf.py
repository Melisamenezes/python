import os
for file in os.listdir("/home/sois/Downloads"):
    if file.endswith(".pdf"):
        print(os.path.join("/home/sois/Downloads", file))