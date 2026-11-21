def find_disappeared_numbers(nums: list[int]) -> list[int]:
    present = set()
    for num in nums:
        present.add(num)
        
    missing = []
    for i in range(1, len(nums) + 1):
        if i not in present:
            missing.append(i)
            
    return missing