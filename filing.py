# =============================================================================
# FILE HANDLING
# =============================================================================

file = open("file_1","x")

#x = creating a file
#w = write in file
#a = appending
#r = reading a file

file.write("Hello World")
file.close()

file = open("file_1","r")
print(file.read())
file.close()

file = open("file_1","w")
file.write("kese ho?")
file.close()

file = open("file_1","a")
file.truncate(10) #remove every thing after the given index
file.write("How are you?")
file.close()

file = open("file_1","r")
print(file.read(5))
file.seek(0)
file.tell()
file.close()

file = open("file_1","a")
file.write("\nHow are you?")
file.close()

