def min1(*args):
    first=args[0]
    for i in args[1:]:
        if i<first:
            first=i
    return first
def min2(first,*args):
    for i in args:
        if i<first:
            first = i
    return first
def min3(*args):
    i = list(args)
    i.sort()
    return i[0]

print(min3(1,2,3,4))
print(min2("bb","aa"))
print(min1("1","2"))