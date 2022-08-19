'''A function to implement a binary search in a given sorted list '''
def binarySearch(lst,low,high,key):
    mid=int((high+low)/2)
    
    if key==lst[mid]:
        return mid
    elif key > lst[mid]:
        if mid==high:
            return -1
        return binarySearch(lst,mid+1,high,key)
    
    else:
        if mid==0:
            return -1
        return binarySearch(lst,low,mid-1,key)

ls = [2,4,6,8,10,20,30,40,200,202095,4589080,1660000661] 
target = 202095
print(binarySearch(ls,0,len(ls)-1,target))