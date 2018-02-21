"""
Playfair Cipher
James Eason

Instructions: Using your choice of language, implement playfair cipher algorithm. The input to your program would be a key word. 
Your program shall then ask if the user wanted to encrypt or decrypt, based on the choice it shall then accept either plain text or cipher text 
and output the corresponding text. Make sure to implement padding wherever required. Submit the source code and print screens of a sample run.
"""
# Encrypt plaintext with a key
def encrypt(key, plaintext):
	matrix = getMatrix(key)
	prep = prepText(plaintext)
	newText = ""
	for pair in prep:
		newText += changePair(pair, matrix, True)
	print "\nEncrypted message: " + newText
	
# Decrypt ciphertext with a key
def decrypt(key, ciphertext):
	matrix = getMatrix(key)
	prep = prepText(ciphertext)
	newText = ""
	for pair in prep:
		newText += changePair(pair, matrix, False)
	print "\nDecrypted message: " + newText	
	
# Generate key matrix
def getMatrix(key):
	matrix = [["-"]*5 for i in range(5)]
	used = ""
	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[row])):
			next = getNextUnused(used, key)
			matrix[row][col] = next
			used += next		
	print "\nMatrix generated:"
	for row in matrix:
		print row
	return matrix
		
# Get next unused character to add in key matrix
def getNextUnused(used, key):
	# key
	for c in key:
		if not (c in used):
			return c
	# rest of alphabet	
	ascii = ord('A')
	while chr(ascii) in used:
		if chr(ascii) == 'I':
			ascii += 1
		ascii += 1
	return chr(ascii)
	
# Prepare text by putting into array
def prepText(plaintext):
	prep = []
	x = 0
	while x < len(plaintext):
		if x == len(plaintext) - 1 or plaintext[x] == plaintext[x+1]:
			prep.append(plaintext[x] + "X")
			x += 1
		else:
			prep.append(plaintext[x:x+2])
			x += 2
	print "\nPlaintext formatted:"
	print prep
	return prep
	
# Encrypt or decrypt a pair of letters
def changePair(pair, matrix, encrypt):
	# Get row and col of each letter
	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[row])):
			if matrix[row][col] == pair[0]:
				firstRow = row
				firstCol = col
			if matrix[row][col] == pair[1]:
				secondRow = row
				secondCol = col
				
	if encrypt and firstRow == secondRow: # encrypt column shift
		firstCol += 1
		if firstCol > 4:
			firstCol = 0
		secondCol += 1
		if secondCol > 4:
			secondCol = 0
		newPair = matrix[firstRow][firstCol] + matrix[secondRow][secondCol]
	elif not encrypt and firstRow == secondRow: # decrypt column shift
		firstCol -= 1
		if firstCol < 0:
			firstCol = 4
		secondCol -= 1
		if secondCol < 0:
			secondCol = 4
		newPair = matrix[firstRow][firstCol] + matrix[secondRow][secondCol]
	elif encrypt and firstCol == secondCol: # encrypt row shift
		firstRow += 1
		if firstRow > 4:
			firstRow = 0
		secondRow += 1
		if secondRow > 4:
			secondRow = 0
		newPair = matrix[firstRow][firstCol] + matrix[secondRow][secondCol]
	elif not encrypt and firstCol == secondCol: # decrypt row shift
		firstRow -= 1
		if firstRow < 0:
			firstRow = 4
		secondRow -= 1
		if secondRow < 0:
			secondRow = 4
		newPair = matrix[firstRow][firstCol] + matrix[secondRow][secondCol]
	else: #rectangle change
		newPair = matrix[firstRow][secondCol] + matrix[secondRow][firstCol]
	return newPair
				
	
print "Enter a key word for playfair cipher algorithm"
key = raw_input().upper().replace("J", "I")
key = "".join(key.split()) #remove whitespace
print "Using key '" + key + "'"
print "Press 1 to encrypt, 2 to decrypt, or 3 to quit"
selection = raw_input()
if selection == "1":
	print "Enter plain text"
	plaintext = raw_input().upper()
	plaintext = "".join(plaintext.split()) #remove whitespace
	encrypt(key, plaintext)
elif selection == "2":
	print "Enter cipher text"
	ciphertext = raw_input()
	ciphertext = "".join(ciphertext.split()) #remove whitespace
	decrypt(key, ciphertext)
