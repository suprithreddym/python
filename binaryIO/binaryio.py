with open("binary", 'bw') as bin_file:
    bin_file.write(bytes(range(17)))

with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)