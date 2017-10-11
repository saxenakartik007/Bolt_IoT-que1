from pyvirtualdisplay import Display
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
import os
from Image_Converter import processCaptcha
from selenium.webdriver.common.by import By
import json


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
    consignmnet_element = browser.find_element_by_name(
        "ctl00$SPWebPartManager1$g_d6d774b9_498e_4de6_8690_a93e944cbeed$ctl00$txtOrignlPgTranNo")
    consignmnet_element.clear()
    consignmnet_element.send_keys(cons_id)
    print "ConsID " + consignmnet_element.get_attribute("value")
    captcha_element = browser.find_element_by_name(
        "ctl00$SPWebPartManager1$g_d6d774b9_498e_4de6_8690_a93e944cbeed$ctl00$txtCaptcha")
    captcha_element.clear()
    captcha_element.send_keys(captcha)
    print "captcha " + captcha_element.get_attribute("value")
    button_element = browser.find_element_by_name(
        "ctl00$SPWebPartManager1$g_d6d774b9_498e_4de6_8690_a93e944cbeed$ctl00$btnSearch")
    print "buttonclicked"
    button_element.click()
    results = wait.until(lambda browser: browser.find_element_by_id(
        "ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_gvTrckMailArticleDtls"))
    elems = browser.find_elements_by_xpath(
        """//*[@id="ctl00_SPWebPartManager1_g_d6d774b9_498e_4de6_8690_a93e944cbeed_ctl00_gvTrckMailArticleDtls"]/table/tbody/tr[1]/td[1]""")
    print elems
    trs = browser.find_elements(By.TAG_NAME, "tr")
    tds = trs[1].find_elements(By.TAG_NAME, "td")
    for item in tds:
        print item.text
    data["ship date"] = tds[1].text
    if len(str(tds[6])) != 0:
        data["status"] = "Delivered"
        data["delivery date"] = tds[6].text
    else:
        data["status"] = "In-transit"
        data["delivery date"] = "unavailable"
    json_data = json.dumps(data)
    print json_data
finally:
    #tidy-up
    browser.quit()
    display.stop() # ignore any output from this.