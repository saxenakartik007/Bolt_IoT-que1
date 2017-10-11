from pyvirtualdisplay import Display
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
import os
from Image_Converter import processCaptcha


display = Display(visible=0, size=(800, 600))
display.start()
cons_id=raw_input("Tracking id: ")
data={}
data["tracking id"]=cons_id
try:
    browser = webdriver.Chrome(os.path.realpath("chromedriver"))
    browser.get('https://www.indiapost.gov.in/VAS/Pages/trackconsignment.aspx')
    wait = ui.WebDriverWait(browser, 10)
    captcha_image=browser.find_element_by_id("ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_imgCaptcha")
    src = captcha_image.get_attribute("src")
    print "src "+src
    captcha = processCaptcha(src)
    print captcha
finally:
    #tidy-up
    browser.quit()
    display.stop() # ignore any output from this.