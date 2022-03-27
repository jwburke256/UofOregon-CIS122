text_file = "random_numbers.txt"
fin = open(text_file)
for line in fin:
    if isinstance(line.strip(), str) == True:
        print("string")
    elif isinstance(line.strip(), int) == True:
        print("integer")
    else:
        print("not string or integer")
