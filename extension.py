file = input("entrez le nom du fichier:")
filestandard=file.lower().strip()
#to make a standardisation of the name and avoid errors brought by majuscules or spaces
if filestandard.endswith(".gif"):
    print("image/gif")
elif filestandard.endswith(".jpg") or filestandard.endswith(".jpeg"):
    print("image/jpeg")
elif filestandard.endswith(".png"):
    print("image/png")
elif filestandard.endswith(".pdf"):
    print("application/pdf")
elif filestandard.endswith(".txt"):
    print("text/plain")
elif filestandard.endswith(".zip"):
    print("application/zip")
else :
    print("application/octet-stream")

'''
amelioration : use dictionaries to put the extension in relation
with the type of file and extract the extension from the name to cross it with dictionaries and print the type.
'''
# to verify : check50 cs50/problems/2022/python/extensions
