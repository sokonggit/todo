temperatures = [10, 12, 14]

temperatures = [str(i) + '\n' for i in temperatures]
print(temperatures)
file = open("file.txt",'w')
file.writelines(temperatures)




