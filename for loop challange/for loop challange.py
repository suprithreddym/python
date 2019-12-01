#print no of segments in ipadress and length of each segment

ipaddress = input("please enter ip address")

segment = 1
segment_length = 0
char = ""

for char in ipaddress:
    if char == '.':
        print("segment {} contains {} length".format(segment,segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

if char != '.':
     print("segment {} contains {} length".format(segment,segment_length))

print("no of segments {}".format(segment))





