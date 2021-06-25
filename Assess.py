from base64 import encode
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://app2.bau.edu.jo:7799/eval/LoginCode.jsp")

username = input()
password = input()
natno = input()
n = input()
browser.find_element_by_name("tbstdno").send_keys(username)
browser.find_element_by_name("tbstdpass").send_keys(password)
browser.find_element_by_name("tbstdnatno").send_keys(natno)
browser.find_element_by_css_selector("input[type=\"submit\" i]").click()
#<input type="RADIO" name="evalans" value="5" onchange="rForm.submit();">
for i in range(1,n):
 for i in range(1,20):
     browser.get("https://app2.bau.edu.jo:7799/eval/Evaluation.jsp?qno="+str(i))
     browser.find_elements_by_xpath("//input[@name='evalans' and @value='1']")[0].click()


 pageSource = browser.page_source

 os.remove("PageSource2")
 f = open("PageSource2", 'w+',encoding="utf8") 
 f.write(pageSource)
 f.close()

 file = open("PageSource2","r+",encoding="utf8")
 lines = [387]
 for index,line in enumerate(file):
    if(index in lines):
         browser.find_element_by_name("captcha").send_keys(line)
         #browser.find_elements_by_xpath("input:not([type=\"image\" i])").click()
 file.close()



