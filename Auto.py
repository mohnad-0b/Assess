from time import sleep
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

username = "" # your username
password = '' # Password
natno = "" # the ID number
n = 5 # number of course

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://app2.bau.edu.jo:7799/eval/Login.jsp")

# login 

browser.find_element_by_name("tbstdno").send_keys(username)
browser.find_element_by_name("tbstdpass").send_keys(password)
browser.find_element_by_name("tbstdnatno").send_keys(natno)
browser.find_element_by_css_selector("input[type=\"submit\" i]").click()
browser.implicitly_wait(100)

for i in range(n):
    for j in range(1,20):
        browser.get("https://app2.bau.edu.jo:7799/eval/Evaluation.jsp?qno="+str(j))
        browser.find_elements_by_xpath("//input[@name='evalans' and @value='1']")[0].click()

    pageSource = browser.page_source
    
    f = open("PageSource2", 'w+',encoding="utf8") 
    f.write(pageSource)
    f.close()
    
    file = open("PageSource2","r+",encoding="utf8")
    lines = [387]
    
    for index,line in enumerate(file):
        if(index in lines):
            browser.find_element_by_name("captcha").send_keys(line)
            break
    sleep(5)
