import heapq as hq
import random
import time

def create_array():
	array = range(100000)
	random.shuffle(array)
	return array

def linear_search(bigArray, k):
	return sorted(bigArray, reverse = True)[:k]

def heapsearch(bigArray, k):
	heap = []

	for item in bigArray:
		if len(heap) < k or item > heap[0]:
			if 	len(heap) == k: 
				hq.heappop(heap)
			hq.heappush(heap, item)	
	return heap

start = time.time()
bigArray = create_array()
print "Creating array took: " + str(time.time() - start) + " seconds"

start = time.time()
print linear_search(bigArray, 10)
print "Linear Search: " + str(time.time() - start) + " seconds"

start = time.time()
print heapsearch(bigArray, 10)
print "Heap Search: " + str(time.time() - start) + " seconds"


"""
print hq.nlargest(H, 6)
"""
