#   1. Best case complexity should be o(n) and occurs when li[i] is less than or equal to 5, so it does not have to 
#      Worst case complexity should be o(n^2) and occurs when  li[i] is greater than 5, this is because li[i] has to go through another for loop, and then more operations
#      Average case complexity should be o(n^2) and occurs when majority of the li[i] is greater than 5, this is an assumption that majority of the indices in li are greater than 5

#   2. The best, average, worst cases are all not the same. This modified code will iterate through the list only once so that the number of
#      operations corresponds to the length of the list, therefore giving a o(n) complexity for all cases

def processdata(li):
    for i in range(len(li)):  
        li[i] *= 2