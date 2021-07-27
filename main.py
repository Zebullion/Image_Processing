from PIL import Image,ImageFilter

def main():
  im = Image.open('lotus.png')
  im2 = Image.open('image2.png')
  im1 = Image.open('image1.png')
  im1 = im1.convert('RGBA')

  #pngToJpg(im2,'flower')
 
  #imageFun(im)

  mergeThee(im1,im2)



def mergeThee(image1,image2):
  """composite  2nd image on top of 1st image. Image 1 and 2 must be same size"""
  mergedImage = Image.alpha_composite(image1,image2)
  mergedImage.save('composite.png')


def imageFun(image):
  sImage = image.filter(ImageFilter.SHARPEN)
  
  
  sImage.save('fun.png')

def pngToJpg(image,fileName):
  image = image.convert('RGB')
  image.save(f'{fileName}.jpg')


main()
