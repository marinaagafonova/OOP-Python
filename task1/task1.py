import math
def checkForCorrect(i1, i2, l):
	count = 0
	curVal1 = l[i1]
	curVal2 = l[i2]
	dif = l[i2] - l[i1]
	
	print("dif = ", dif, end = " ")
	if dif != 0:
		while not(i1==0 and i2==len(l)-1):
			if not(curVal1-dif in l):
				count += 1
			if not(curVal2+dif in l):
				count +=1
			if(i1 > 0):
				i1-=1
				curVal1 -=dif
			if(i2 < len(l)-1):
				i2+=1
				curVal2 += dif
	else:
		count = -1
	return count
	
def Sort(i1, i2, l):
	curVal1 = l[i1]
	curVal2 = l[i2]
	dif = l[i2] - l[i1]
	i1 -=1
	i2+=1
	while not(i1==0 and i2==len(l)-1):
			if not(curVal1-dif in l):
				l[i1] = curVal1-dif
			if not(curVal2+dif in l):
				l[i2] = curVal1+dif
			if(i1 > 0):
				i1-=1
				curVal1 -=dif
			if(i2 < len(l)-1):
				i2+=1
				curVal2 += dif
	l.sort()
	if(dif<0):
		l.reverse()
	'''
	for i in range(i1, 0, -1):
		if not(math.fabs(l[i]-l[i-1])==math.fabs(dif)):
				l[i-1] = l[i] + dif
	for i in range(i2, len(l)-1):
		if not(math.fabs(l[i+1]-l[i])==math.fabs(dif)):
				l[i+1] = l[i] + dif
'''
list = []
with open("input.txt", 'r') as inf:
	for string in inf:
		temp = string.split()
		for elem in temp:
			list.append(int(elem))
counts = {} # key is count, value is a index of first elem
for i in range(len(list)-1):
	res = checkForCorrect(i, i+1, list)
	print("index = ", i, " count = ", res)
	if res != -1:
		if(counts.get(res)==None):
			counts[res] = i
min = len(list)
for key in counts.keys():
	if key < min:
		min = key
print("min = ", min)
print("index = ", counts.get(min))
index = int(counts.get(min))
Sort(index, index+1, list)
for el in list:
	print(el, end = " ")
with open("output.txt", 'w') as ouf:
	ouf.truncate(0)
	for el in list:
		ouf.write(str(el))
		ouf.write(' ')
print("done")
		

		