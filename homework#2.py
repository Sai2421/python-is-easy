#This python file has details about a song

"""
"Happier" is a song by American music producer Marshmello and British band Bastille. 
Written and produced by Marshmello, with lyrics from Dan Smith and Steve Mac
"""
def Song():
  return "Happier"
def Band():
  return  "Bastille"
def YearOfRelease():
  return 2018
def DurationInSeconds():
  return   214
def Producer():
  return "Marshmello"
def Genre():
  return "Pop"
def check_pop():
  if Genre()=="Pop":
    return True
  else:
    return False  
    
print(Song())
print(Band())
print(YearOfRelease())
print(DurationInSeconds())
print(Producer())
print(Genre())
print(check_pop())