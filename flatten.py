liste = [[1,2],[3,4],[5,6,7]]

def Reverse(list):
    for i in list:
        i.reverse()
        list.reverse()
    return list

print(Reverse(liste))
