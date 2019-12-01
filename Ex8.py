# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:21:30 2019

@author: download2
"""

import statistics as st 



print("===========================Exercise one===========================")

X = [3, 1.5 , 4.5 , 6.75 , 2.25 , 5.75 , 2.25]

print(st.mean(X))
print(st.harmonic_mean(X))
print(st.median(X))
print(st.median_low(X))
print(st.median_high(X))
print(st.median_grouped(X))
print(st.mode(X))
print(st.pstdev(X))
print(st.pvariance(X))
print(st.stdev(X))
print(st.variance(X)) 




print("===========================Exercise two===========================")

import random

print(random.random())
print(random.randrange(10))
print(random.choice(["Ali","Khalid","Hussam"]))
print(random.sample(range(1000),10))
print(random.choice("Orange Academy"))

y = [1,5,8,9,2,4]
random.shuffle(y)
print(y)

print(random.randint(10,20))
print(random.randrange(1000,2111,5))
print(random.randint(10,20))
print(random.uniform(10000,11000))


print("==========================Exercise three==========================")

import math

print (math.pi)
print(math.cos(200))
print(math.sin(200))
print(math.tan(200))
print(math.floor(10.8))
print(math.ceil(10.8))


print("==========================Exercise four===========================")



import math

print (math.pi)
print(math.cos(200))
print(math.sin(200))
print(math.tan(200))
print(math.floor(10.8))
print(math.ceil(10.8))


print("_________Question4__________")
from PIL import Image , ImageFilter, ImageDraw

download1 = Image.open("download1.jpg")
download2 = Image.open ("download2.jpg")
print(download1.format, download1.size , download1.mode)

mohamamd_flip = download1.transpose(Image.FLIP_TOP_BOTTOM)
mohamamd_flip.show()

download1_grey = download1.convert("L")
download1_grey.show()

download1_cropped = download1.crop((0,0,50,50))
download1_cropped.show()

download1_draw = Image.open("download1.jpg")
draw = ImageDraw.Draw(download1_draw)
draw.line((0,0) + download1_draw.size , fill = (255,255,255))
draw.line((0, download1_draw.size[1], download1_draw.size[0], 0 ) , fill = (255,255,255))
draw.text((download1_draw.size[0]/2 - download1_draw.size[0]/2 , download1_draw.size[1]/2 + 20) , "download1",
          fill=(255,255,0))
download1_draw.show()


download1_enhaced = download1.filter(ImageFilter.EDGE_ENHANCE)
download1_enhaced.show()


download1_find = download1.filter(ImageFilter.FIND_EDGES)
download1_find.show()



download1_smooth = download1.filter(ImageFilter.SMOOTH)
download1_smooth.show()

download1_sharpen = download1.filter(ImageFilter.SHARPEN)
download1_sharpen.show()

alpha = 0.5
download2 = Image.open("download2.jpg").resize(download1.size)

Image.blend(download1 , download2 , alpha).save(
        "download1_blend.jpg".format(alpha))

download1_blend = Image.open("download1_blend.jpg")
download1_blend.show()

download1_blur = download1.filter(ImageFilter.BLUR)
download1_blur.show()


size = (128,128)
saved = ("download1_thumbnail.jpg")
download1_thumbnail = Image.open("download1.jpg")
download1_thumbnail.thumbnail(size)
download1_thumbnail.save(saved)
download1_thumbnail.show()

download1_rot_90 = download1.rotate(90)
download1_rot_90.show()




download2 = Image.open("download2.jpg").resize(download1.size)
mask = Image.open("mask.jpg")
mask = mask.resize(download1.size)

Image.composite(download1,download2,mask).save(
        "download1_mask.jpg")

download1_mask = Image.open("download1_mask.jpg")
download1_mask.show()






















