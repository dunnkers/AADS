store = dict()
# store['2-1-2-20']
store[(2,1,2,20)] = True

def hashit(tuple):
    return (2, 1, 2, 20)


print(hashit((2, 1, 2, 20)))

print(store[(2,1,2,20)])
