# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:30:27 2018

@author: Shafi
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup



# getting details of  flipkart from the url

def detail(url):
    html = urlopen(url)
    soup = BeautifulSoup(html,'lxml')
    flipkart_list=[]

    divtags=soup.find_all('div',class_="bhgxx2 col-12-12")


    for i in divtags:

        # getting the title/brand name  of the product
        try:
           
            temp1 = str(i.find('div',{"class":"_3wU53n"}).text)
            #product[a]["title"] = temp
        except:
           temp1=""
         # getting the price  of the product
            
        try:
            temp2 = i.find('div',{"class":"_1vC4OE _2rQ-NK"}).text
            #product[a]["price"]= temp
        except:
            temp2 = ""
        
        # getting the rating  of the product
        
        try:
            temp3 = i.find('div',{"class":"hGSR34 _2beYZw"}).text
            #product[a]["rating"] = temp
        except:
            temp3 = ""
            
        # getting the url  of the product
        try:
            temp4 = i.find('a').get('href')
            
            #product[a]["rating"] = temp
        except:
            temp4 = ""

        
        if(temp1!=''):
            flipkart_list.append([temp1 , temp2,temp3 , "https://www.flipkart.com" + temp4, "Flipkart"])
        
	# if vertical structure list do not come then we the products are presented in horizontal
        if(not flipkart_list):
            
            temp = soup.find_all("div" , {"class":"_3liAhj _1R0K0g"})
        
            for i in temp:
                try:
                    temp2 = i.find('a',{"class":"_2cLu-l"}).get("title")
                except: 
                    temp2 = ""
                try:
                    temp1 = i.find('div',{"class":"hGSR34 _2beYZw"}).text
                except:
                    temp1 = ""
                try:
                    temp3 = i.find("div" , {"class":"_1vC4OE"}).text
                except:
                    temp3 = ""
                try:
                    temp4 =  i.find('a').get('href')
                except:
                    temp4 = ""
                if(temp2!=''):
                    flipkart_list.append([temp2 , temp3,temp1 , "https://www.flipkart.com" + temp4, "Flipkart"])
                        
                
    return flipkart_list



# getting details from amazon
def details(url):
    html = urlopen(url)
    global soup
    soup = BeautifulSoup(html,'lxml')
    global title_list
    all_titles = soup.find_all('li',class_="s-result-item celwidget ")
    title_list = all_titles
    amazon_list = []

    for i in title_list:

        # getting the title/brand name of the product
        try:
            temp1 = str(i.h2.text)
            #product[a]["title"] = temp
        except:
            temp1=""
            
        # getting the price  of the product
            
        try:
            temp2 = i.find("span",{"class":'a-size-base a-color-price s-price a-text-bold'}).text.strip()
            #product[a]["price"]= temp
        except:
            temp2 = ""
        # getting the rating  of the product
        
        try:
            temp = i.find_all("span", {"class":"a-icon-alt"})
            for k in temp:
                if(k.text!="prime"):
                    temp3 = k.text.strip()
                    j = temp3.split(" ")
                    temp3 = j[0]
    
                    break
            #product[a]["rating"] = temp
        except:
            temp3 = ""
         # getting the url  of the product
            
        try:
            temp4 = i.h2.parent["href"]
        except:
            temp4 =""
       
        amazon_list .append([temp1 , temp2,temp3 , temp4 , "Amazon"])

    return amazon_list 

def main(query):
    query=query.replace(' ', "%20")
    url = "https://www.flipkart.com/search?q="+ query
    a = detail(url)
    
    urls = "https://www.amazon.in/s?keywords="+query
    a = a + details(urls)
    
    b =sorted(sorted(a,key = lambda x : x[1]),key = lambda x : x[2], reverse = True)
    
    return b
    

if __name__ == '__main__':
    main()





            