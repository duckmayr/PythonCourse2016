from timeit import *
import random
import matplotlib.pyplot as plt

def selectionSort(nums, iter = 0): #, tmp = 0
	if iter == len(nums) - 1: return nums
	tmp = nums[-1]
	for i in range(iter, len(nums)-1):
		if nums[i] < tmp: tmp = nums[i]
	nums.remove(tmp)
	nums.insert(iter, tmp)
	return selectionSort(nums, iter + 1)

def mergeSort(nums, iter = 0):
	if iter == 0: nums = [[x] for x in nums]
	if len(nums) == 1: return nums[0]
	newNums = []
	for i in [x for x in range(len(nums) - 1) if not x % 2]:
		newNums.append(mergePart(nums[i], nums[i+1], len(nums[i]+nums[i+1]), res = []))
	if len(nums) % 2: newNums.append(nums[-1])
	return mergeSort(newNums, iter + 1)
	
def mergePart(list1, list2, stop, iter = 0, res = []):
	if iter == stop: return res
	if len(list1) == 0:
		res.append(list2[0])
		list2.remove(list2[0])
		return mergePart(list1, list2, stop, iter + 1, res)
	if len(list2) == 0:
		res.append(list1[0])
		list1.remove(list1[0])
		return mergePart(list1, list2, stop, iter + 1, res)
	if list1[0] < list2[0]:
		res.append(list1[0])
		list1.remove(list1[0])
	else:
		res.append(list2[0])
		list2.remove(list2[0])
	return mergePart(list1, list2, stop, iter + 1, res)

sectionSortTimes = []
mergeSortTimes = []
for n in range(1, 51):	
	selTimer = Timer(lambda: selectionSort(random.sample(range(1,n + 1), n)))
	mergeTimer = Timer(lambda: mergeSort(random.sample(range(1,n + 1), n)))
	sectionSortTimes.append(selTimer.timeit(number=10000))
	mergeSortTimes.append(mergeTimer.timeit(number=10000))

plt.axis([0, 50, 0, 20])
plt.plot(range(1,51),sectionSortTimes, 'b-', label='Selection Sort')
plt.plot(range(1,51),mergeSortTimes, 'r-', label='Merge Sort')
plt.legend()
plt.show()