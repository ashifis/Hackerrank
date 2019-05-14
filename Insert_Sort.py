
dum_arr = [999,1, 13, 15, 45, 7, 87, 87, 77, 54, 6, 9, 89, 0, 3,300]
int count = 78

for i in range(0, len(dum_arr)):
    print(i)
    for j in range(i, -1, -1):

        if j > 0:
            print(j)
            if dum_arr[j]<dum_arr[j-1]:
                temp = dum_arr[j]
                dum_arr[j] = dum_arr[j - 1]
                dum_arr[j - 1] = temp
    print("====")

print(dum_arr)
