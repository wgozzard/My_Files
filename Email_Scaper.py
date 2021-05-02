#This will allow you to scrape emails from any site effortlessly
#I built this to help in email collecting for marketing/sales purposes

#Collect emails from a website using this scraper
#install extract_emails
pip install extract_emails
#import the following libraries
import pandas as pd
import re
from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser

with RequestsBrowser() as browser:
    email_extractor = EmailExtractor("https://www.cmsd.k12.pa.us/athletics", browser, depth=2) #enter what ever URL here
    emails = email_extractor.get_emails()
    
em =[]
for line in emails:
    x = line.as_list()
    
    for y in x:
        z = re.findall('\S+[a-zA-Z0-9]\S+@\S+[a-zA-Z]', y)
        if len(z) > 0:
            em.append(z)
            
#Take this list and move it to a data frame pandas
df = pd.DataFrame(em, columns =['Email List'])
df.head()

#Push list to an excel spreadsheet
df.to_excel("Em_List_2.xlsx") 
