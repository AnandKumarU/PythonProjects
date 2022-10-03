f=101
print(f)
#global vs. local variables in functions
def someFunction():
    global f
    print(f)
    f='I am learning python'
    print(f)
someFunction()
print(f)