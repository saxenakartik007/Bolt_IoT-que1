import urllib2
from PIL import Image
from ocr import OCRSpace,OCRSpaceLanguage
def convert():
    img = Image.open('captcha.gif')
    img.save('captchatext.png', 'png')


def processCaptcha(url):
    picture_page = url
    opener1 = urllib2.build_opener()
    page1 = opener1.open(picture_page)
    my_picture = page1.read()
    filename = "captcha.gif"
    fout = open(filename, "wb")
    fout.write(my_picture)
    fout.close()
    convert()
    ocr_object=OCRSpace(api_key="5ebb70ef6d88957",language=OCRSpaceLanguage.English)
    json=ocr_object.ocr_file("captchatext.png")
    captchastr=str( json['ParsedResults'][0]['ParsedText'])
    captchastr=captchastr.lower()
    captchastr=captchastr.replace(" ", "")
    captchastr=captchastr[0:6]
    return captchastr

