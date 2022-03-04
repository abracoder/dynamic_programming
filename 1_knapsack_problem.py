
#program for 0/1 knapsack problem

def knapsack(weight,val,max_weight,size):
    # print(mem)
    # print(size,max_weight)


    if (size==0 or max_weight==0):
        return 0

    if(mem[size][max_weight] !=-1):
        return mem[size][max_weight]


    if (weight[size-1]<=max_weight):
        mem[size][max_weight]=max(val[size-1]+knapsack(weight,val,max_weight-weight[size-1],size-1),knapsack(weight,val,max_weight,size-1))
        return mem[size][max_weight]
    elif (weight[size-1]>max_weight):
        mem[size][max_weight]=knapsack(weight,val,max_weight,size-1)
        return mem[size][max_weight]



weight=[1,3,4,5]
val=[1,4,5,7]
max_weight=7
size=4
#creating 2d array for memorization

mem=[[-1]*(max_weight+1) for _ in range(size+1)]
# print(mem)

print('max profit=',knapsack(weight,val,max_weight,size))
