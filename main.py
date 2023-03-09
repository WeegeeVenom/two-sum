def twoSum(nums: List[int], target: int) -> List[int]:
	list2 = []
	for i, elem in enumerate(nums):
		for j, elem2 in enumerate(list2):
			if(elem2 == elem): return [j,i]
		list2.append(target - elem)
