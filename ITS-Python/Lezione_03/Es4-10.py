cube_list:list = [(i**3) for i in range (1,11)]
print(cube_list)
print(f"{cube_list[:3]}\n{cube_list[(len(cube_list)//2)-1: (len(cube_list)//2) +2]}\n{cube_list[-3:]}")