def check(arr):
    if arr[0][0] != 8:
        valid = all(ele == arr[0] for ele in arr)
        if not valid:
            print("not ok")
        return [1, arr[0][1]]
    else:
        return [1] + check(arr[0][1])

ar = (8, [(8, [(8, [(9, 3), (9, 4), (9, 3)])])])
ar1 = (8, [(9, 3), (9, 4), (9, 3)])
a=1
l = [[{0:1}], [0,1], 2, 3]

env = l[:]
env[3] = 4
env[0][0][0] = 3
if not None:
    print("A")
