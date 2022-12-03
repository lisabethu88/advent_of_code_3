f = open("input", "r")

sum = 0
for line in f:
    line = line.strip()
    length = len(line)
    halfway_point = (length//2)
    first_compartment = line[0:halfway_point]
    second_compartment = line[halfway_point:length]
    for character in first_compartment:
        if character in second_compartment:
            same_item = character
            if same_item.isupper():
                sum+= ord(same_item)-38
            else:
                sum+= ord(same_item)-96
            break
    
f.close()
print(sum)