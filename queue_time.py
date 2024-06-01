def queue_time(customers, n): # O(m*nlogn)
    tills = [0]*n
    for i in customers: # m times
        tills[0] += i
        tills.sort() # O(nlogn)
    return max(tills) 

def queue_time_optimized(customers, n): # O(m*n)
    tills = [0]*n
    for i in customers: # m times
        min_element = min(tills) # O(n)
        min_index = tills.index(min_element) # O(n)
        tills[min_index] += i 
    return max(tills)
