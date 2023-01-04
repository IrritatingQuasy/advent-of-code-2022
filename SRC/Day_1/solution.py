import os

def elf_calories():
    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, "Input.txt")
    return open(file_path)

def count_calories():
    elf_number = {}
    count=0
    elf_number[count] = 0
    for i in elf_calories():
        if i == '\n':
            count+=1
            elf_number[count] = 0
        else:
            elf_number[count] += int(i)
    return elf_number
def most_calories():
    highest_calories = 0
    for i in count_calories().values():
        if i>highest_calories:
            highest_calories = i
    return highest_calories



