from selenium import webdriver
import time
#USA cities
path=r"C:\Users\a\Desktop\scraping\seleniu\msedgedriver.exe"
browser = webdriver.Edge(path)
browser.get("https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population")
city=browser.find_elements_by_xpath('//table[5]/tbody/tr/td[1]/i/a | //table[5]/tbody/tr/td[1]/a | //table[5]/tbody/tr/td[1]/b | //table[5]/tbody/tr/td[1]/i/b')
USA_cities=[x.text for x in city]
print("USA_cities")
print(USA_cities)
print(len(USA_cities))

#Canada cities
time.sleep(10)
browser.get("https://www.britannica.com/topic/list-of-cities-and-towns-in-Canada-2038873")
city=browser.find_elements_by_xpath('//section/ul//a')
Canada_cities=[x.text for x in city]
print("canada_cities")
print(Canada_cities)
print(len(Canada_cities))
time.sleep(5)
browser.quit()