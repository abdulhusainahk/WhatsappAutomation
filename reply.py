from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox(executable_path=r'C:\fire\geckodriver.exe')
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
input("Enter Go after scanning the QR code")
time.sleep(5)
messpending = '//span[@class=\'OUeyt\']'
check='//span[@class=\'_1wjpf _3NFp9 _3FXB1\']'
re=['Hello','hello','Hii','hii','Abdul']
names = ["Ajay","James"]

for name in names:
    person=driver.find_element_by_xpath(messpending)
    person.click()
    match=driver.find_element_by_xpath(check).text
    if match ==name:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got]
        if type(msg[-1]) == str and msg[-1] in re:
            print(msg[-1])
            i=0
            while i<3:
                message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                message.send_keys("Hii :)")
                sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                sendbutton.click()
                i+=1
        else:
            reply = driver.find_element_by_class_name("_2S1VP.copyable-text.selectable-text")
            reply.clear()
            reply.send_keys("Happy New Year! :)")
            reply.send_keys(Keys.RETURN)