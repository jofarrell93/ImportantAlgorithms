#Calculate the time taken for 1000 runs of:
#binarysearch & unordered sample (slower as has to order sample first)
#binarysearch & ordered sample (fastest)
#list.index() & unordered sample ((un)ordered doesn't matter - linear search)
#list.index() & ordered sample ((un)ordered doesn't matter - linear search)

#Note: In each of the 1000 runs the search sample never changes - only the search term

import time
import random

#UNORDERED binarysearch
#binarysearch function for an unordered list
#function returns:
#index of the search term IF search term exists 
#otherwise -1 if the search term does not exist
def binarysearch_unordered(list, x):
	
	sample=sorted(list) #Make sure to not use list.sort() as this will modify the original list
	
	#Need to return the search term's index if it exists
	#not just a yes/no and therefore can't continue to 
	#slice the list (would lose track of correct index)
	#so need to keep a record of the leftmost and rightmost 
	#index values as we reduce the search sample
	#[0------------------------------------------len()-1]
	#[leftmost------------midpoint-------------rightmost]
	#if sample[midpoint] == search term return 
	#otherwise if sample[midpoint] > search term 
	#update rightmost to reduce the search sample for the next iteration
	#[leftmost---rightmost************[ignore]**********]
	
	index_left, index_right = 0, len(sample)-1
	
	while index_left<=index_right:
		
		#Calculating the mid index 
		#Could use:
		#1) (index_left+index_right)/2
		#2) index_left + (index_right-index_left)/2
		#Apparently odler versions of python had an int overflow issue 
		#so use no. (2) above. Maybe not required for python 3 but good 
		#practice for other languages 
		mid_index = index_left + (index_right-index_left)//2
		
		if sample[mid_index]==x:
			return mid_index
		elif sample[mid_index]<x:
			index_left = mid_index + 1
		else: 
			index_right = mid_index - 1
			
	#if function hasn't returned by now search term does not exist
	return -1

#ORDERED binarysearch 
#binarysearch function for an ordered list
#function returns:
#index of the search term IF search term exists 
#otherwise -1 if the search term does not exist
def binarysearch_ordered(sample, x):
	
	#Need to return the search term's index if it exists
	#not just a yes/no and therefore can't continue to 
	#slice the list (would lose track of correct index)
	#so need to keep a record of the leftmost and rightmost 
	#index values as we reduce the search sample
	#[0------------------------------------------len()-1]
	#[leftmost------------midpoint-------------rightmost]
	#if sample[midpoint] == search term return 
	#otherwise if sample[midpoint] > search term 
	#update rightmost to reduce the search sample for the next iteration
	#[leftmost---rightmost************[ignore]**********]
	
	index_left, index_right = 0, len(sample)-1
	
	while index_left<=index_right:
		
		#Calculating the mid index 
		#Could use:
		#1) (index_left+index_right)/2
		#2) index_left + (index_right-index_left)/2
		#Apparently odler versions of python had an int overflow issue 
		#so use no. (2) above. Maybe not required for python 3 but good 
		#practice for other languages 
		mid_index = index_left + (index_right-index_left)//2
		
		if sample[mid_index]==x:
			return mid_index
		elif sample[mid_index]<x:
			index_left = mid_index + 1
		else: 
			index_right = mid_index - 1
			
	#if function hasn't returned by now search term does not exist
	return -1	
	
	
#parameters for generating random search sample
range_min, range_max=0, 10000
sample_size=10000 #sample has to include all range(10000) to use list.index(search_term) without index errors

#Generate random sample - unordered
list=random.sample(range(range_min, range_max),sample_size)

#Random sample ordered
list_sorted=sorted(list)

num_loops = 1000


#*******************************
#Test: binarysearch_unordered
t_start=time.perf_counter()

for i in range(num_loops):
	search_term=random.randint(range_min, range_max)
	binarysearch_unordered(list,search_term)

t_end=time.perf_counter()

t_taken=t_end-t_start

print(f"{num_loops} calls of binarysearch_unordered took {t_taken} seconds")


#*******************************		
#Test: binarysearch_ordered
t_start=time.perf_counter()

for i in range(num_loops):
	search_term=random.randint(range_min, range_max)
	binarysearch_ordered(list_sorted,search_term)

t_end=time.perf_counter()

t_taken=t_end-t_start

print(f"{num_loops} calls of binarysearch_ordered took {t_taken} seconds")	


#*******************************
#Test: Python 3 built in list.index() with unordered list
t_start=time.perf_counter()

for i in range(num_loops):
	search_term=random.randint(range_min, range_max-1) #randint is inclusive so need min,max-1
	list.index(search_term)

t_end=time.perf_counter()

t_taken=t_end-t_start

print(f"{num_loops} calls of list.index() with an unordered list took {t_taken} seconds")		

	
#*******************************
#Test: Python 3 built in list.index() with ordered list
t_start=time.perf_counter()

for i in range(num_loops):
	search_term=random.randint(range_min, range_max-1) #randint is inclusive so need min,max-1
	list_sorted.index(search_term)

t_end=time.perf_counter()

t_taken=t_end-t_start

print(f"{num_loops} calls of list.index() with an ordered list took {t_taken} seconds")		
		
		
		
		
