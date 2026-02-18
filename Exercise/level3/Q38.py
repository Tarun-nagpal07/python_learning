'''use the Pillow library to open an image, resize it to a 200x200 thumbnail (preserving aspect
ratio), convert it to grayscale, and save it as a new file.'''

from PIL import Image

img = Image.open('output.jpg')
# img.show()

img.thumbnail((200,200))
g = img.convert('L')
g.save('grayscale.png')