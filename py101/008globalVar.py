APPLE = 100 # global var
a = None
def fun():
    global a    # use the global 'a' var in this function
    a = 20   
    return a+100

print(APPLE)    # 100
print('a past:', a)  # None
fun()
print('a now:', a)   # 20