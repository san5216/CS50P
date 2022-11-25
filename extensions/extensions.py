fileName = input("Type the filename: ").lower().strip()

splitFile = fileName.rsplit(sep=".")

extension = splitFile[len(splitFile) - 1]

d = {
    "gif": "image",
    #"jpg": "image",
    "jpeg": "image",
    "png": "image",
    "pdf": "application",
    "zip": "application",
    #"txt": "plain",
}

if extension == "jpg":
    print("image/jpeg")
elif extension == "txt":
    print("text/plain")
elif extension in d:
    print(d[extension], extension, sep="/")
else:
    print("application/octet-stream")
