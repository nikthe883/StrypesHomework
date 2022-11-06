from PIL import Image


img = Image.open("1.jpg")

print("Filename : ",img.filename)

print("Format : ",img.format)

print("Mode : ",img.mode)

print("Size : ",img.size)

print("Width : ",img.width)

print("Height : ",img.height)

print("Image Palette : ",img.palette)

img.close()
