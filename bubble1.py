
def bubble(nums):

	for i in range(len(nums)-1,0,-1):
		
		for j in range(i):
			if nums[j] > nums[j+1]:
				temp= nums[j]
				nums[j]=nums[j+1]
				nums[j+1]=temp

			



nums=[3,2,1,6,8,9,4]

bubble(nums)

print(nums)