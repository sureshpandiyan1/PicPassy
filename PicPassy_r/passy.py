import random
import time, os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

def srt_wrt(filename,mails):
    file = open(filename,'wb')
    zz = bytes('$$'+ str(mails)  ,encoding="utf_16")
    with open('ignore.jpg', 'rb') as f:
        byte = f.read() + zz
        file.write(byte)
        



def rd_that(filename):
    m = []
    with open(filename,'rb') as lkj:
        lkj = str(lkj.read()).split('\\')
        m.append(lkj)
        l = ''.join(m[0][len(m[0])-200:len(m[0])])
        l =  l.replace('x00','')
        f,s = l.split('$$')
        zz = str(s[0:len(s)-1])
    return zz

# step 1 we should say cupuser - mailid + password shouldbeinside the picture
def regsz_passer(f,passer):
    cupuserimg = Image.new('RGB',(random.randint(50,300),random.randint(140,300)),(0,0,0))
    cupuserimg.save('ignore.jpg')
    cupuserimg = Image.open('ignore.jpg')
    w, h = 600,140
    draw = ImageDraw.Draw(cupuserimg)
    text = " "
    font = ImageFont.truetype('arial.ttf',24)
    tw, th = draw.textsize(text,font)
    draw.text((w/12,h/3), text, font=font)
    cupuserimg.save('ignore.jpg')
    srt_wrt(f+".jpg",passer)


    
