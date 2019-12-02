newfile=open("testfile.txt","w+")
for i in range(0,10):
    newfile.write("hi all i am suprith:\n")

newfile.seek(1,0) # seek
print(newfile.read())
print("current file position: ", newfile.tell()) # tell
newfile.close()

print("IS file closed ",newfile.closed)
print("file mode is: ",newfile.mode)
print("file name: ", newfile.name)
