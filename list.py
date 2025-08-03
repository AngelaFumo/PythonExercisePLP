# 1
my_list=[]
 # 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# 3
my_list[1]=15
# 4
other_list=[50,60,70]
my_list.extend(other_list)
#5
del my_list[-1]
#6
my_list.sort()
#7
position=my_list.index(30)
print(my_list)
print(position)