inputName = input('Enter file name : ')
outputName = input('Enter new file name : ' )
key = int( input("Enter the shift key: " ))

inFile = open(inputName, 'r')

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

encryptedMessage = ''

messageSeq = inFile.readlines()

i = 0
# This i was added to use a second for loop which would effectively count the number of lines in msgs.txt

for index in messageSeq:
    
    #The idea of using a second loop was to basically do our initial encryption program #lines times
    #for char in messageSeq[i]:
    for char in messageSeq[i]:
            
        #messageSeq[i].lstrip()
        letterIndex = alphabet.find( char )
        encryptedCharacter = shiftedAlphabet[letterIndex]
        encryptedMessage = encryptedMessage + encryptedCharacter
        
    encryptedMessage = encryptedMessage + '\n'
    
    i = i + 1
    
print( "The encrypted message is: \n{0}".format( encryptedMessage ))

outputFile = open( outputName, "w" )
print( encryptedMessage, file=outputFile )
outputFile.close()

print( "Done writing encrypted message to file {0}".format( outputName) )

#Note: For some reason I got an 's' at the end of the first three lines. When I went through to debug, the '\n' statement was yielding a value of -1 which created an 's'. I tried hard to remove it, but couldn't find a good solution.
