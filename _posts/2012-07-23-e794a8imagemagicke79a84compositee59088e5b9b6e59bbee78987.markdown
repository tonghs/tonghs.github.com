---
author: ths
comments: true
date: 2012-07-23 11:44:00+00:00
layout: post
slug: '%e7%94%a8imagemagick%e7%9a%84composite%e5%90%88%e5%b9%b6%e5%9b%be%e7%89%87'
title: 用imageMagick的composite合并图片
wordpress_id: 829
categories:
- 技术
tags:
- composite
- imageMagick
---

composite命令可以非常方便的合并两张图片 





因此用来进行图像加水印、批量增加边框等常用的变换 





最简单的用法为： 





****





**composite -gravity north src.jpg coverback.jpg des.jpg**





其中src.jpg为前景图片 





coverback.jpg为背景图片。 





des.jpg为叠加后的结果 





-gravity north 指叠加位置为垂直据顶部、水平居中（正北方向） 





如果要求在正中间，参数为center 





如果要求在右下角，参数为southeast 





composite还提供更灵活的定位，可以使用 -geometry 配置 





具体的composite参数表见下表 





[-affine _matrix_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#affine)





affine transform matrix 





[-alpha](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#alpha)  
on, activate, off, deactivate, set, opaque, copy", transparent, extract, background, or shape the alpha channel 





[-authenticate _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#authenticate)  
decrypt image with this password 





[-blend _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#blend)  
blend images 





[-blue-primary _point_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#blue-primary)  
chromaticity blue primary point 





[-border _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#border)  
surround image with a border of color 





[-bordercolor _color_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#bordercolor)  
border color 





[-channel _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#channel)  
apply option to select image channels 





[-colors _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#colors)  
preferred number of colors in the image 





[-colorspace _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#colorspace)  
set image colorspace 





[-comment _string_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#comment)  
annotate image with comment 





[-compose _operator_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#compose)  
set image composite operator 





[-compress _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#compress)  
image compression type 





[-debug _events_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#debug)  
display copious debugging information 





[-decipher _filename_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#decipher)  
convert cipher pixels to plain 





[-define _format:option_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#define)  
define one or more image format options 





[-density _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#density)  
horizontal and vertical density of the image 





[-depth _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#depth)  
image depth 





[-displace _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#displace)  
shift image pixels defined by a displacement map 





[-dissolve _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#dissolve)  
dissolve the two images a given percent 





[-dither _method_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#dither)  
apply error diffusion to image 





[-encipher _filename_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#encipher)  
convert plain pixels to cipher pixels 





[-encoding _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#encoding)  
text encoding type 





[-endian _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#endian)  
endianness (MSB or LSB) of the image 





[-extract _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#extract)  
extract area from image 





[-filter _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#filter)  
use this filter when resizing an image 





[-font _name_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#font)  
render text with this font 





[-geometry _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#geometry)  
preferred size or location of the image 





[-gravity _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#gravity)  
horizontal and vertical text placement 





[-green-primary _point_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#green-primary)  
chromaticity green primary point 





[-help](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#help)  
print program options 





[-identify](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#identify)  
identify the format and characteristics of the image 





[-interlace _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#interlace)  
type of image interlacing scheme 





[-interpolate _method_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#interpolate)  
pixel color interpolation method 





[-label _string_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#label)  
assign a label to an image 





[-level _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#level)  
adjust the level of image contrast 





[-limit _type value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#limit)  
pixel cache resource limit 





[-log _format_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#log)  
format of debugging information 





[-monitor](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#monitor)  
monitor progress 





[-monochrome](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#monochrome)  
transform image to black and white 





[-negate](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#negate)  
replace each pixel with its complementary color 





[-page _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#page)  
size and location of an image canvas (setting) 





[-pointsize _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#pointsize)  
font point size 





[-profile _filename_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#profile)  
add, delete, or apply an image profile 





[-quality _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#quality)  
JPEG/MIFF/PNG compression level 





[-quantize _colorspace_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#quantize)  
reduce image colors in this colorspace 





[-quiet](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#quiet)  
suppress all warning messages 





[-red-primary _point_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#red-primary)  
chromaticity red primary point 





[-regard-warnings](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#regard-warnings)  
pay attention to warning messages. 





[-respect-parentheses](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#respect-parentheses)  
settings remain in effect until parenthesis boundary. 





[-rotate _degrees_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#rotate)  
apply Paeth rotation to the image 





[-sampling-factor_geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#sampling-factor)  
horizontal and vertical sampling factor 





[-scene _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#scene)  
image scene number 





[-seed _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#seed)  
seed a new sequence of pseudo-random numbers 





[-set _attribute value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#set)  
set an image attribute 





[-sharpen _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#sharpen)  
sharpen the image 





[-shave _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#shave)  
shave pixels from the image edges 





[-size _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#size)  
width and height of image 





[-stegano _offset_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#stegano)  
hide watermark within an image 





[-stereo _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#stereo)  
combine two image to create a stereo anaglyph 





[-strip](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#strip)  
strip image of all profiles and comments 





[-swap _indexes_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#swap)  
swap two images in the image sequence 





[-synchronize](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#synchronize)  
synchronize image to storage device 





[-taint](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#taint)  
mark the image as modified 





[-thumbnail _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#thumbnail)  
create a thumbnail of the image 





[-tile](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#tile)  
repeat composite operation across and down image 





[-transform](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#transform)  
affine transform image 





[-transparent-color_color_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#transparent-color)  
transparent color 





[-treedepth _value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#treedepth)  
color tree depth 





[-type _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#type)  
image type 





[-units _type_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#units)  
the units of image resolution 





[-unsharp _geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#unsharp)  
sharpen the image 





[-verbose](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#verbose)  
print detailed information about the image 





[-version](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#version)  
print version information 





[-virtual-pixel _method_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#virtual-pixel)  
access method for pixels outside the boundaries of the image 





[-watermark_geometry_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#watermark)  
percent brightness and saturation of a watermark 





[-white-point _point_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#white-point)  
chromaticity white point 





[-white-threshold_value_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#white-threshold)  
force all pixels above the threshold into white 





[-write _filename_](http://blog.csdn.net/cserchen/article/details/script/command-line-options.php#write)  
write images to this file



