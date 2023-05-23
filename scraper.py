import requests
from bs4 import BeautifulSoup
import json

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count (url):
        """
        this fuction gets an URL as an arguments and find all the sup tag that 
        has an noprint class in it which have a 'citation needed' in it
        and return the num of it
        """
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        all_citations = soup.find_all('sup',class_='noprint')

        return len(all_citations)

def get_citations_needed_report(url):
         """
         This function gets an URL and find all the paragraph that has a 'citation needed' 
         and return the text in it as a string that has all the paragraph 
         """
         page = requests.get(URL)
         soup = BeautifulSoup(page.content, 'html.parser') 
         all_citations = soup.find_all('p') 
         lists_of_p = []
         for x in all_citations:  
            if x.find('sup',class_='noprint'):
                   lists_of_p.append(x.text)          
           
         string_0f_p = '\n'.join(lists_of_p)
         return string_0f_p
if __name__ == '__main__':
         print(get_citations_needed_count(URL)) 
         print(get_citations_needed_report(URL)) 
