from PIL import Image,ImageFilter

def main():
  im = Image.open('lotus.png')
  im2 = Image.open('image2.png')
  im1 = Image.open('image1.png')

  #pngToJpg(im2,'flower')
 
  imageFun(im)


def imageFun(image):
  sImage = image.filter(ImageFilter.SHARPEN)
  sImage = image.rotate(90)
  sImage.save('fun.png')

def pngToJpg(image,fileName):
  image = image.convert('RGB')
  image.save(f'{fileName}.jpg')


main()
