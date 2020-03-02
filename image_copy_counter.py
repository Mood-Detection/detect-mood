f_source = open("apple.png", "rb")
f_dest = open("dest1.png", "wb")
 
char_count = 0
 
for line in f_source:
    char_count += len(line)
    f_dest.write(line)
 
print(char_count, "characters copied successfully")
 
f_source.close()
f_dest.close()
