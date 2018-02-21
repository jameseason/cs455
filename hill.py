"""
Hill Cipher
James Eason

Instructions: Using your choice of language, implement Hill cipher algorithm. The input to your program would be a key matrix (make it capable of dealing 
with 2X2 and 3X3 key matrix). Your program shall then ask if the user wanted to encrypt or decrypt, based on the choice it shall then accept either
plain text or cipher text and output the corresponding plain or cipher text. Remember not to use any special packages for matrix calculations. 
Also, make sure to implement the concept of padding in case the input is not long enough. Submit the source code and print screens of a sample run. (3 points)
"""
import math

# Encrypt plaintext string with key matrix
def encrypt(keyMatrix, plaintext):
	prep = prepText(plaintext, len(keyMatrix))
	newText = ""
	for text in prep:
		cipherMatrix = multiplyMatrices(keyMatrix, textToMatrix(text, len(keyMatrix)))
		newText += matrixToText(cipherMatrix)
	print "\nEncrypted message: " + newText
	
# Decrypt ciphertext string with key matrix
def decrypt(keyMatrix, ciphertext):
	inverseMatrix = invert(keyMatrix)
	prep = prepText(ciphertext, len(keyMatrix))
	newText = ""
	for text in prep:
		plainMatrix = multiplyMatrices(inverseMatrix, textToMatrix(text, len(keyMatrix)))
		newText += matrixToText(plainMatrix)
	print "\nDecrypted message: " + newText

# Invert a matrix
def invert(matrix):
	size = len(matrix)
	inverted = [[0]*size for i in range(size)]
	if size == 2:
		deter = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
		if deter == 0 or deter%13 == 0 or deter%2 == 0:
			print "Error: determinant is invalid. Could not invert matrix"
			return matrix
		else:
			deter %= 26
			deter = 27 / deter
			inverted[0][0] = (matrix[1][1] * deter) % 26
			inverted[0][1] = (-matrix[0][1] * deter) % 26
			inverted[1][0] = (-matrix[1][0] * deter) % 26
			inverted[1][1] = (matrix[0][0] * deter) % 26
	elif size == 3:
		deter = int(matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[1][0]*matrix[2][1]*matrix[0][2] +
				matrix[2][0]*matrix[0][1]*matrix[1][2] - matrix[0][0]*matrix[2][1]*matrix[1][2] -
				matrix[2][0]*matrix[1][1]*matrix[0][2] - matrix[1][0]*matrix[0][1]*matrix[2][2])
		if deter == 0 or deter%13 == 0 or deter%2 == 0:
			print "Error: determinant is invalid. Could not invert matrix"
			return matrix
		else:
			inverted[0][0] = ((matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) * deter) % 26
			inverted[0][1] = ((matrix[0][2]*matrix[2][1] - matrix[0][1]*matrix[2][2]) * deter) % 26
			inverted[0][2] = ((matrix[0][1]*matrix[1][2] - matrix[0][2]*matrix[1][1]) * deter) % 26
			inverted[1][0] = ((matrix[1][2]*matrix[2][0] - matrix[1][0]*matrix[2][2]) * deter) % 26
			inverted[1][1] = ((matrix[0][0]*matrix[2][2] - matrix[0][2]*matrix[2][0]) * deter) % 26
			inverted[1][2] = ((matrix[0][2]*matrix[1][0] - matrix[0][0]*matrix[1][2]) * deter) % 26
			inverted[2][0] = ((matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]) * deter) % 26
			inverted[2][1] = ((matrix[0][1]*matrix[2][0] - matrix[0][0]*matrix[2][1]) * deter) % 26
			inverted[2][2] = ((matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) * deter) % 26
	print "\nInverted:"	
	for row in inverted:
		print row
	return inverted

# Convert text to number matrix
def textToMatrix(text, size):
	matrix = [["-"] for i in range(size)]
	for row in range(0, size):
		matrix[row][0] = alphaToNum(text[row])
	print "\nUsing text matrix:"
	for row in matrix:
		print row
	return matrix
	
# Convert alpha character to corresponding number (A == 0)
def alphaToNum(alpha):
	return ord(alpha) - 65	

# Convert number to corresponding alpha character
def numToAlpha(num):
	return chr(num + 65)
	
# Convert number matrix to text
def matrixToText(matrix):
	text = ""
	for row in range(len(matrix)):
		text += numToAlpha(matrix[row][0])
	return text

# Prepare text by dividing it up into an array
def prepText(plaintext, size):
	prep = []
	while len(plaintext) % size != 0:
		plaintext += "Z"
	for x in xrange(0, len(plaintext), size):
		prep.append(plaintext[x:x+size])
	print "\nPlaintext formatted:"
	print prep
	return prep
	
# Multiply two matrices together
def multiplyMatrices(keyMatrix, textMatrix):
	result = [[0] for i in range(len(keyMatrix))]
	for i in range(len(keyMatrix)):
		for j in range(len(textMatrix[0])):
			for k in range(len(textMatrix)):
				result[i][j] += keyMatrix[i][k]*textMatrix[k][j]
	for row in range(len(result)):
		result[row][0] %= 26
	print "Multiplication result:"
	for r in result:
	   print r
	return result

# Convert key string input to a matrix`	
def convertKeyMatrix(keyString):
	size = int(math.sqrt(len(keyString)))
	matrix = [[0]*size for i in range(size)]
	count = 0
	for row in range(0, size):
		for col in range(0, size):
			matrix[row][col] = int(keyString[count])
			count += 1
	print "\nUsing key matrix:"
	for row in matrix:
		print row
	return matrix

print "Enter key matrix with each number separated by a space (left to right, top to bottom)."
key = raw_input().strip().split()
while len(key) < 4 and len(key) < 9:
	key.append(5)
while len(key) > 9:
	key = key[:-1]
matrix = convertKeyMatrix(key)
print "\nPress 1 to encrypt, 2 to decrypt, or 3 to quit"
selection = raw_input()
if selection == "1":
	print "\nEnter plain text"
	plaintext = raw_input().upper()
	plaintext = "".join(plaintext.split()) #remove whitespace
	encrypt(matrix, plaintext)
elif selection == "2":
	print "\nEnter cipher text"
	ciphertext = raw_input()
	ciphertext = "".join(ciphertext.split()) #remove whitespace
	decrypt(matrix, ciphertext)
