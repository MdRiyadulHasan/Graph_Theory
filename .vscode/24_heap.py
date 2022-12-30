import heapq
def heap_sort(lst):
    heapq.heapify(lst)
    nums=[]
    res = []
    for n in lst:
        heapq.heappush(nums,n)
    while nums:
        temp = heapq.heappop(nums)
        res.append(temp)
    return res       
if __name__ == '__main__':
    lst = [10,5,3,2,4,9,50,4,15,35,12]
    ans = heap_sort(lst)
    print (ans)