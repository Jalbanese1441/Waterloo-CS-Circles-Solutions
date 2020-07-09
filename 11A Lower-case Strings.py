def lowerChar(char):
   if ord(char) >= ord('A') and ord(char) <= ord('Z'):
      char = chr(ord(char)+32)
      return char
   else:
      return char
def lowerString(string):
   result = ""
   for i in range(0,len(string)):
      result = result + lowerChar(string[i])
   return result
