"""
image processing with Pillow
"""
from PIL import Image, ImageFilter

img = Image.open('C:/Users/anton/PycharmProjects/Automation_testing/src/exercices_todo/4.5 pikachu.jpg.jpg')
filtered_image = img.convert('L')
filtered_image.thumbnail((400, 200))
filtered_image.save('grey.png', 'png')
filtered_image.show()