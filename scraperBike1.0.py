'''Created by Matthew Windham 
July 11,2017.  to use with the AIOTestKing website'''

import requests
from bs4 import BeautifulSoup as bs
var = 1
var2 = 1


print("Go to the First Question in the series you are studying on the  AIO Test king website ")
url = raw_input("input Link here ->")
url = url

##LOOP for questions
while True:    
    if var2 == var:
        r = requests.get(url)
        soup = bs(r.text, "lxml")

        print var
        #print var2


        #   #this part gets the Question to answer
        g_data = soup.find_all("div", {"class": "entry-content"})
        for item in g_data:
            print item.text.encode('utf-8')

    
        ##This part is the right answer.
        right_data = soup.find_all("p", {"class": "rightAnswer"} )
        for item in right_data:
            print item.text.encode("utf-8")
        
        ##This part is going to find the next page to navigate to.
        elm = soup.find('div', {'class', 'nav-next'})
    
        for div in elm:
            elm = [div.a for div in soup.find_all('div', attrs={'class':'nav-next'})]  
        for link in elm:
            url = link['href']
        
            var = var + 1

        var2 = var2 + 1  

        print (".............................")
