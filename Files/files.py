fh=open("hello.txt",'r+')
fh.writelines("hello world")
print(fh.readlines())
fh.close()