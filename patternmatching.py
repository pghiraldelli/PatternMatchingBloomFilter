import numpy as np
import hashlib
import time

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

'''Returns a hash code for the substring using the hash function of index i.
The result can be only smaller than B.'''
def getHashCode(substr, i):
	return{
		0:int(hashlib.md5(substr).hexdigest()[:8], 16) % m,
		1:int(hashlib.sha1(substr).hexdigest()[:8], 16) % m,
		2:int(hashlib.sha224(substr).hexdigest()[:8], 16) % m,
		3:int(hashlib.sha256(substr).hexdigest()[:8], 16) % m,
		4:int(hashlib.sha384(substr).hexdigest()[:8], 16) % m,
		5:int(hashlib.sha512(substr).hexdigest()[:8], 16) % m,
	}[i] 


'''Returns the array of Bloom Filter signature for the string.
The result will be of size M. Every position will be zero, except for those
where the substring's hash is valid (in this case it will be one).'''
def getSignature(string):
	signature = np.zeros((m,), dtype=np.int)
	substr = getAllSubstrings(string)
	for sub in substr:
		for i in xrange(b):
			subHash = getHashCode(sub,i)
			signature[subHash] = 1
	return signature

'''Create the list of signatures for every line in the file.
K represents the size of the substrings to search in the text.
M represents the size of the list of signature for each line.
B represents the number of hash functions used to calculate the position in the signature list for the substring.'''
def preProcessText():
	for line in content:
		signature = getSignature(line)
		allSignatures.append(signature)

'''Returns True if the word is in the text or False if its not.
It divides the word in substrings of size K, get the hash of each one 
and compare with the respective position in the line signature.
If it matches with the signature the find method is used to determine if
the word is really in the text.'''
def wordInText(word):
	subs = getAllSubstrings(word)
	sigWord = getSignature(word)
	positionsSigWord = sigWord == 1

	for line in xrange(len(content)):
		sigLine = allSignatures[line]
		
		#get all positions of sigLine where sigWord is 1 and then check if they're all 1.
		sameSignature = np.all(sigLine[positionsSigWord] == 1)

		if sameSignature and (word in content[line]):
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

'''Verify if B is not an invalid number. Returns True if valid and False if not.'''
def bIsValid():
	if b == 0:
		print 'B must be bigger than zero'
		return False

	if b > 6:
		print 'B is bigger than the limit: 6'
		return False

	return True

'''Read all the entries and verify if they all are valid. Returns True if they are and False if they are not.'''
def readEntriesWithSuccess():
	global k,b,m
	try:
		k=int(raw_input('K (size of substring to match): '))
		b=int(raw_input('B (number of hash functions to use. LIMIT is 6): '))
	
		if bIsValid() == False:
			return False

		m=int(raw_input('M (size of the signature list for each line): '))
		return True
	except ValueError:
		print "Not a number\n"
		return False

def main():
	global content
	content = readFileLines()

	if readEntriesWithSuccess() == False:
		return
	
	print '\nPreprocessing text...\n'
	preProcessText()

	while True:
		word = raw_input('Word to search for: ')

		start_time = time.time()
		findWord(word)
		elapsed_time = time.time() - start_time
		
		print 'Total time: ' + str(elapsed_time) + '\n'


if __name__ == "__main__": main()
