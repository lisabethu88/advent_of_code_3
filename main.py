def get_common_character(first_bag, second_bag, third_bag):
    for character in first_bag:
        if character in second_bag and character in third_bag:
            return character




f = open("input", "r")

sum = 0
line_num = 0
line_list = []

for line in f:
    line_num+=1
    line = line.strip()
    line_list.append(line)
    if line_num % 3 == 0: 
        #find character for each line
        """  length = len(line)
        halfway_point = (length//2)
        first_compartment = line[0:halfway_point]
        second_compartment = line[halfway_point:length] """
        same_item = get_common_character(line_list[0], line_list[1], line_list[2])
        if same_item.isupper():
            sum+= ord(same_item)-38
        else:
            sum+= ord(same_item)-96
        line_list = []
    
f.close()
print(sum)