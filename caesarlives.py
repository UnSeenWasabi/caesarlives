 # Modified Caesar Cipher from https://inventwithpython.com/chapter14.html

import math

MAX_ALPHA_KEY_SIZE = 26
MAX_NUM_KEY_SIZE = 10

def getMode():
    while True:
        print('[E]ncrypt or [D]ecrypt or [B]rute Force a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode[0]
        else:
            print('Enter either "Encrypt" or "E" or "Decrypt" or "D" or "Brute" or "B" .')

def getMessage():
    print('Please enter your string:')
    return input()

def getKey():
    key = 0
    print('Enter the key number (1-%s)' % (MAX_ALPHA_KEY_SIZE))
    
    while True:
        try:
            key = int(input())
            if (key >= 1 and key <= MAX_ALPHA_KEY_SIZE):
                return key
            else:
                print('Number has to be within 1 - %s.' % (MAX_ALPHA_KEY_SIZE) + ' Please try again')
        except ValueError:
            print ('Please key in a whole number within 1 - %s.' % (MAX_ALPHA_KEY_SIZE) + ' Please try again')

def bruteF(message, key):
   
    if key > MAX_NUM_KEY_SIZE:
        NKey = key % MAX_NUM_KEY_SIZE
        NKey = -NKey
    else:
        NKey = -key

    key = -key
    buffer = ''
        
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                   num -= 26
                elif num < ord('A'):
                   num += 26
            elif symbol.islower():
                if num > ord('z'):
                   num -= 26
                elif num < ord('a'):
                   num += 26
            buffer += chr(num)
            
        elif symbol.isnumeric():    
            num = ord(symbol)
            num += NKey
            if num > ord('9'):
                num -= 10
            elif num < ord('0'):
                num += 10
                
            buffer += chr(num)
 
        else:        
            buffer += symbol
    return buffer
        
def getTranslatedMessage(mode, message, key):
    NKey = key
    buffer = ''
    
    if  NKey > MAX_NUM_KEY_SIZE:
        NKey = NKey % MAX_NUM_KEY_SIZE
 
    if mode[0] == 'd':
        key = -key
        NKey = -NKey
        
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                   num -= 26
                elif num < ord('A'):
                     num += 26
            elif symbol.islower():
                if num > ord('z'):
                   num -= 26
                elif num < ord('a'):
                     num += 26

            buffer += chr(num)
            
        elif symbol.isnumeric():    
            num = ord(symbol)
            num += NKey
            if num > ord('9'):
                num -= 10
            elif num < ord('0'):
                num += 10
            
            buffer += chr(num)
        else:        
            buffer += symbol
    return buffer

mode = getMode()
print('')
message = getMessage()
print('')
if mode[0] != 'b':
    key = getKey()
print('')


if mode[0] != 'b':
    print('Output')
    print('--------------------------------------')
    print(getTranslatedMessage(mode, message, key))
else:
    print('Key | Output ')
    print('--------------------------------------')
    for key in range(1, MAX_ALPHA_KEY_SIZE + 1):
        print(key,' | ' + bruteF(message,key))