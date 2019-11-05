from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse
from parsel import Selector
import subprocess

class Scraper:
    def getLinkedInURL(driver,idSearch):
        print ("Headless Firefox Initialized")
        #go to the specified URL -> linkedin login page
        driver.get("https://www.linkedin.com/login")
        # find class id based on inspect element and simulate keyboard input
        username = driver.find_element_by_id('username')
        username.send_keys('ahmad.bellington@gmail.com')
        password = driver.find_element_by_id('password')
        password.send_keys('JackDullBoy1999')
        # simulate button click
        submit = driver.find_element_by_class_name('login__form_action_container ')
        submit.click()
        print("Login successful")
        #go to google and simulate searching
        s1 = 'linkedin+'
        s2 = s1 + idSearch
        driver.get("https://www.google.com/search?q="+s2)
        print(driver.current_url)
        #find first search result and click it
        result = driver.find_element_by_class_name('r')
        result.click()
        linkedInURL = driver.current_url
        print(linkedInURL)
        return linkedInURL
    
    def scrapingAbout(idSearch):
        try:
            #enable headless browser
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
            #start scraping using parsel
            driver.get(Scraper.getLinkedInURL(driver,idSearch))
            # get the HTML code of the page source and assign it to sel
            sel = Selector(text=driver.page_source)
            # scrape values
            name = sel.xpath('//*[starts-with(@class,"inline t-24 t-black t-normal break-words")]/text()').extract_first()
            if name:
                name = name.strip()
            title = sel.xpath('//*[starts-with(@class,"mt1 t-18 t-black t-normal")]/text()').extract_first()
            if title:
                title = title.strip()
            connection = sel.xpath('//*[starts-with(@class,"t-16 t-black t-normal")]/text()').extract_first()
            if connection:
                connection = connection.strip()
            region = sel.xpath('//*[starts-with(@class,"t-16 t-black t-normal inline-block")]/text()').extract_first()
            if region:
                region = region.strip()
            dump = {
              "AccountID":idSearch,
              "AccountName": name,
              "AccountTitle": title,
              "AccountRegion": region,
            }
        except NoSuchElementException as exception:
            dump = {'Feedback':'Invalid AccountID','AccountID':idSearch}
        finally:
            #end processes -> firefox and geckodriver
            return dump
            driver.quit()
            subprocess.run(["killall","geckodriver"])
        
        
    def scrapingEducation(idSearch):
        try:
            #enable headless browser
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
            #start scraping using parsel
            driver.get(Scraper.getLinkedInURL(driver,idSearch))
            # get the HTML code of the page source and assign it to sel
            sel = Selector(text=driver.page_source)
            # scrape values
            institution = sel.xpath('//*[starts-with(@class,"pv-entity__school-name t-16 t-black t-bold")]/text()').extract_first()
            if institution:
                institution = institution.strip()
            title = sel.xpath('//*[starts-with(@class,"pv-entity__comma-item")]/text()').extract_first()
            dump = {
               "AccountID":idSearch,
               "EducationInstitution": institution,
               "EducationTitle": title
            }
        except NoSuchElementException as exception:
            dump = {'Feedback':'Invalid AccountID','AccountID':idSearch}
        finally:
            #end processes -> firefox and geckodriver
            driver.quit()
            subprocess.run(["killall","geckodriver"])
            return dump
        
    def scrapingWorkplace(idSearch): #get past and present workplace
        try:
            #enable headless browser
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
            #start scraping using parsel
            driver.get(Scraper.getLinkedInURL(driver,idSearch))
            # get the HTML code of the page source and assign it to sel
            sel = Selector(text=driver.page_source)
            # scrape values
            li = [None] * 2
            exp = sel.xpath('//span[contains(@class,"lt-line-clamp__line")]/text()').getall()
            for i in range(0,2):
                li[i] = exp[i]
                if li[i]:
                    li[i] = li[i].strip()
            dump = {
                "AccountID": idSearch,
                "Workplace1":li[0],
                "Workplace2":li[1],
            }
        except NoSuchElementException as exception:
            dump = {'Feedback':'Invalid AccountID','AccountID':idSearch}
        finally:
            #end processes -> firefox and geckodriver
            driver.quit()
            subprocess.run(["killall","geckodriver"])
            return dump
        
        
                                                
        
 
        

