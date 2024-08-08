member = input("Add a new member")

file = open("member.txt",'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("member.txt",'w')
existing_members = file.writelines(existing_members)
file.close()
