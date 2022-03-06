import os
print(os.getcwd())
print("пример пути для файла: " + os.getcwd() + "\файл.формат")
print("а если хотите сохранить в директории с ос, введите просто название")
file_1 = input("путь файла ~> ")
write_1 = input("1 ")
my_file = open(file_1, "w+")
my_file.write(write_1 + " ")
my_file.close()

write_2 = input("2 ")
my_file = open(file_1, "a+")
my_file.write(write_2 + " ")
my_file.close()

write_3 = input("3 ")
my_file = open(file_1, "a+")
my_file.write(write_3 + " ")
my_file.close()

write_4 = input("4 ")
my_file = open(file_1, "a+")
my_file.write(write_4 + " ")
my_file.close()

write_5 = input("5 ")
my_file = open(file_1, "a+")
my_file.write(write_5 + " ")
my_file.close()

write_6 = input("6 ")
my_file = open(file_1, "a+")
my_file.write(write_6 + " ")
my_file.close()

write_7 = input("7 ")
my_file = open(file_1, "a+")
my_file.write(write_7 + " ")
my_file.close()

write_8 = input("8 ")
my_file = open(file_1, "a+")
my_file.write(write_8 + " ")
my_file.close()

write_9 = input("9 ")
my_file = open(file_1, "a+")
my_file.write(write_9 + " ")
my_file.close()

write_10 = input("10 ")
my_file = open(file_1, "a+")
my_file.write(write_10 + " ")
my_file.close()

