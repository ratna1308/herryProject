import os

files = os.listdir()
print(files)

# def createIfNotExist(folder):
#     if not os.path.exists(folder):
#         os.mkdir(folder)
#
#
# createIfNotExist("ran1")
# createIfNotExist("Images")
# createIfNotExist("Docs")
# createIfNotExist("Media")

# os.remove("ran1")
os.remove("Images.txt")
# os.remove("Docs")
# os.remove("Media")