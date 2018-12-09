"""
Module 1 Lab 3 - Team 10
Mark Mariscal, Christopher Piwarski, Wais Robleh
28 October 2018

"""

#Given
def get_pic():
 return makePicture(pickAFile())

#Warmup
def noBlue(pic):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    setBlue(p, 0)
  repaint(pic)
  
#Cuts the red value for RGB in half  
def halfRed(pic):
  lessRed(50)
  
#Cuts the amount of red in an image by the given percentage
def lessRed(n):
  setNum = n/float(100)
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r*setNum)
  repaint(pic)

#Problem2 - A function that increases the red value of an image
def moreRed(n):
  setNum = 1/(n/float(100))
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r*setNum)
  repaint(pic)

#problem 3-A function called roseColoredGlasses that makes an image look pink
def roseCoveredGlasses(pic):
 pic = get_pic()
 pixels = getPixels(pic)
 for p in pixels:
  b = getBlue(p)
  g = getGreen(p)
  g *= .82
  b *= .863
  setGreen(p, g)
  setBlue(p, b)
 repaint(pic)
  
#Problem 4 - use makeLighter() to soften up an image
def lightenUp(pic):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p, newColor)
  repaint(pic)
  
#Problem 5 - Create a negative of an image
def makeNegative(pic):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    setRed(p, 255 - r)
    setGreen(p, 255 - g)
    setBlue(p, 255 - b)
  repaint(pic)
  
#Problem 6 - Create a black and white image
def BnW():
  pic = get_pic(pic)
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    avg = (b + g + r)/3  
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)
  repaint(pic)
 
#Problem 6 - A better black and white function
def betterBnW(pic):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    avg = (b*0.114) + (g*0.587) + (r*0.299)/3  
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)
  repaint(pic)
    
