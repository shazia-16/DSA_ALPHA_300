def contains_duplicates2(nums,k):
    seen={}   #to store last seen index    
    for i in range(len(nums)):
        num =nums[i]
        if num in seen and i-seen[num]<=k:
            return True
        seen[num]=i   #update last seen index
    return False
print(contains_duplicates2([1,2,3,1],3))

