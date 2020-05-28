from selenium import webdriver 
from time import sleep 
import pyautogui
from secrets import posx, posy, lfx, lfy, scrollamt, username, password, stalk
import sys
class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dunjudge.me")
    def login(self, uid, pwd):
        self.driver.find_element_by_xpath("/html/body/div/header/nav/div/ul/li/a").click()
        username = self.driver.find_element_by_xpath("/html/body/div/header/nav/div/ul/li/ul/li[1]/form/div[1]/input")
        username.send_keys(uid)

        password = self.driver.find_element_by_xpath("/html/body/div/header/nav/div/ul/li/ul/li[1]/form/div[2]/input")
        password.send_keys(pwd)


        self.driver.find_element_by_xpath("/html/body/div/header/nav/div/ul/li/ul/li[2]/div[2]/a").click()
        sleep(4)


    def problems(self,user):
        self.driver.get("https://dunjudge.me/users/{}/".format(user))
        pyautogui.moveTo(lfx, lfy)
        pyautogui.scroll(-260)
        sleep(5)
        pyautogui.moveTo(posx, posy)
        for i in range(scrollamt):
            pyautogui.scroll(-1000)
        box = self.driver.find_element_by_xpath("/html/body/div/aside[2]/section[2]/div/section[1]/div[3]/div[2]/table/tbody")
        li = box.find_elements_by_tag_name("tr")
        res = []
        cnt = 0
        for row in li:
            cnt += 1
            print("{}/{}".format(cnt,len(li)))
            eles = row.find_elements_by_xpath(".//*")
            if eles[5].text == '100':
                res.append(eles[3].text)
        return res
        
        
        

bot = Bot()
bot.login(username,password)
li = set(bot.problems(stalk))
sys.stdout = open("{}.txt".format(stalk), "w")

print(li)

sys.stdout.close()


bot.driver.close()