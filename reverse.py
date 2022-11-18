listPatika = [[1,"a",["cat"],2],[[[3]],"dog"],4,5]

def flattenn(l):
    flatList=[]
    for e in l:
        if isinstance(e,list):
            flatList.extend(flattenn((e)))
        else:
            flatList.append(e)
    return flatList

print(flattenn(listPatika))