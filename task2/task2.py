def ShiftColumnsLeft (matrix, steps) :  # +исправить rows colums, +сделать чтение из файла, +вынести realsteps
	for i in range (len(matrix)) :
		while steps!=0:
			steps -=1
			temp = matrix[i][0]
			for j in range(len(matrix[0])-1, -1, -1):
				value = matrix[i][j]
				matrix[i][j] = temp
				temp = value
def ShiftColumnsRight (matrix, steps) :
	for i in range (len(matrix)) :
		while steps!=0:
			steps -=1
			temp = matrix[i][0]
			for j in range(1,len(matrix[0])):
				value = matrix[i][j]
				matrix[i][j] = temp
				temp = value
			matrix[i][0] = temp

def ShiftRowsLeft (matrix, steps) :
	for j in range (len(matrix[0])) :
		while steps>0:
			steps -=1
			temp = matrix[0][j]
			for i in range(len(matrix)-1, -1, -1):
				value = matrix[i][j]
				matrix[i][j] = temp
				temp = value
def ShiftRowsRight (matrix, steps) :
	for j in range (len(matrix[0])) :
		while steps>0:
			steps -=1
			temp = matrix[0][j]
			for i in range(1,len(matrix)):
				value = matrix[i][j]
				matrix[i][j] = temp
				temp = value
			matrix[0][j] = temp
def PrintArray (matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(array[i][j], end = " ")
		print()


		
f = open (input("Input file name: "),'r')
array = []

for line in f:
    array.append([x for x in line.split(" ")])
f.close()
print(array)

shift = int(input("количество позиций = "))
operation = input("Что сдвинуть? - ")

print()
if (operation == "строки"):
	if(shift<0):
		shift *= (-1)
		shift = shift % len(array[0]);
		ShiftRowsLeft(array, shift)
	else:
		ShiftRowsRight(array, shift)
elif (operation == "столбцы"):
	if(shift<0):
		shift *= (-1)
		shift = shift % len(array[0]);
		ShiftColumnsLeft(array, shift)
	else:
		ShiftColumnsRight(array, shift)
else:
	print("ошибка ввода")

PrintArray(array)