from bs4 import BeautifulSoup as bs
import re

def wordCount(text):
   if text:
      return len(text.split())
   else:
     return 0

def noniFixitDomains(html, featureFile):
   html = bs(html)
   urlCount = 0.0
   ifixitUrlCount = 0.0

   for a in html.find_all('a', href=True):
      if len(re.findall(r"ifixit", a['href'])):
         ifixitUrlCount = ifixitUrlCount + 1.0
      urlCount = urlCount + 1.0

   if urlCount:
      featureFile.write('%s ' % (1.0 - (ifixitUrlCount/urlCount)))
   else:
      featureFile.write('0.0 ')
