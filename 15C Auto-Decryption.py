#print(letterGoodness) #testing... it's predefined
#def getLetter(letter,S):
 #   x=ord(letter)
 #   y=64-(x-S)
 #   if x-S<=64:
 #      x=90
 #      S=y
 #      print(letter)
   #    print("decoded is",chr(x-S),(x-S))
#letter=""
#codedmessage ="BZS"#=input()
#S=25#=int(input())
#DecryptedMessage
#highestGoodnessValuea=""
#print(len(codedmessage))
#for i in range(len(codedmessage)):
 #   letter=codedmessage[i]
  #  getLetter(letter,S)


#testMessage="HUD"
#testMessage="BZS"                                
#testMessage="ECV"# Should be cat when S=28
#lettergoodness= [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
highestLetterGoodness=0
decryptedMessage=""# The actual or final decrypted message
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#testMessage="LQKP OG CV GKIJV DA VJG BQQ"
#testMessage="JAZZ"#0.0846
#testMessage="TKJJ"#OFEE with 0.3514
testMessage=input()
bestS=0
S=0# Shift Value
for t in range(26):
    letterGoodnessCounter=0 # current value of the word
    decodedMessage=""
    for i in range(len(testMessage)):
     if testMessage[i] in letters:
       # print(letters.find(testMessage[i]))
          x=letters.find(testMessage[i])
          #print(26-(x-S)) 
           #print("x is:",x,"S is",S,"and x-S is:",x-S)
          if x-S<0:
              x=x+26
         # print(lettergoodness[x-S])
          letterGoodnessCounter= letterGoodnessCounter+letterGoodness[x-S]
          decodedMessage= decodedMessage+ letters[x-S]
     else: decodedMessage= decodedMessage+" "
    if letterGoodnessCounter>highestLetterGoodness:
         bestS=S
         highestLetterGoodness=letterGoodnessCounter
         decryptedMessage = decodedMessage
         #print(S)
         #print(letterGoodnessCounter,decryptedMessage)
    S=S+1
print(decryptedMessage) # Final message
#print(highestLetterGoodness) # based off the most likely number (the number printed below)
#print(bestS)# The most likely S value
