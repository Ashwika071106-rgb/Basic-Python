intro = input("Enter your introduction : ")
print(intro)
characterCount = 0
wordCount = 0
for i in intro : 
    characterCount = characterCount+1
    if(i == ' '):
        wordCount = wordCount+1
print("Number of words in the string : " )
print(wordCount + 1)
print("Number of characters in the string : " )
print(characterCount)