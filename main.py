import time
no_of_students = int(input("no. of students:\n"))
dic = {}
i = 0
avg = {}
while i < no_of_students:
  x = input("<name> <marks1> <marks2> <marks3>:\n").split()
  time.sleep(5)
  name = x[0]
  marks1 = float(x[1])
  marks2 = float(x[2])
  marks3 = float(x[3])
  marks = [marks1, marks2, marks3]
  average = (marks1+marks2+marks3)/3
  dic[name] = marks
  avg[name] = average
  i += 1
  f = open("data", "a")
  f.write(f"{i} -- {name} -- {marks1} -- {marks2} -- {marks3} -- {average}\n")
  f.close()
print(dic)
y = input("which student marks avg do u want?\n")
print("%.2f"%(avg[y]))
