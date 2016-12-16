import numpy as np
import hashlib

content = []
allSignatures = []
k,b,m = 0,0,0

'''Returns a list of all lines in the file.'''
def readFileLines():
	with open('big.txt') as f:
		content = f.readlines()
	return content

'''Returns a list of all substring of size sizeSub in the string.'''
def getAllSubstrings(string):
	length = len(string)
	return [string[i:i + k] for i in xrange(length) if (i+k) <= length]

'''Returns a hash code for the substring using B hash functions.
The result can be only smaller than B.'''
#TODO Implementar para aceitar varias funcoes hash
def getHashCode(substr):
	return int(hashlib.md5(substr).hexdigest()[:8], 16) % m


'''Returns the array of Bloom Filter signature for the line string.
The result will be of size M. Every position will be zero, except for those
where the substring's hash is valid (in this case it will be one).'''
def getSignatureOfLine(line):
	signature = np.zeros((m,), dtype=np.int)
	substr = getAllSubstrings(line)
	for sub in substr:
		subHash = getHashCode(sub)
		signature[subHash] = 1
	return signature

'''Create the list of signatures for every line in the file.
K represents the size of the substrings to search in the text.
M represents the size of the list of signature for each line.
B represents the number of hash functions used to calculate the position in the signature list for the substring.'''
def preProcessText():
	for line in content:
		signature = getSignatureOfLine(line)
		allSignatures.append(signature)

'''Returns True if the word is in the text or False if its not.
It divides the word in substrings of size K, get the hash of each one 
and compare with the respective position in the line signature.
If it matches with the signature the KMP algorithm is used to determine if
the word is really in the text.'''
def wordInText(word):
	subs = getAllSubstrings(word)
	for line in xrange(len(content)):
		sigLine = allSignatures[line]
		#print sigLine
		wordInLine = True
		for sub in subs:
			subHash = getHashCode(sub)
			#print sub, subHash
			if sigLine[subHash] == 0:
				wordInLine = False
				break
		if wordInLine:
			#USAR KMP
			return True
	return False

'''Searchs for the word in the text and check all the cases it can go wrong first.'''
def findWord(word):
	if len(word) < k :
		print 'The word is smaller than the K given.\n'
		return
	
	if wordInText(word):
		print '\nWord found!'
	else:
		print '\nWord not found.'


def main():
	global content,k,b,m
	#content = ['Essa e a linha 1.', 'Valeu. Essa e a linha dois.']
	content = readFileLines()

	try:
		k=int(raw_input('K (size of substring to match):'))
	except ValueError:
		print "Not a number\n"

	try:
		b=int(raw_input('B (number of hash functions to use):'))
	except ValueError:
		print "Not a number\n"

	try:
		m=int(raw_input('M (size of the signature list for each line):'))
	except ValueError:
		print "Not a number\n"

	
	print '\nPreprocessing text...\n'
	preProcessText()

	while True:
		word = raw_input('Word to search for:')

		findWord(word)


if __name__ == "__main__": main()
