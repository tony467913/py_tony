ex_list=[1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in ex_list:
    print(i)
    print("inner of for")
print("outer of for")

for i in range(0,13,5):
    print(i)
print("end of range")


#dictionary
dic={}
dic["language","version","platform"]="python",2.7,64
for key in dic:
    print(key,dic[key])

print("end")
