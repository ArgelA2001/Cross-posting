from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
import random
import re
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords

#      TO DO LIST
#make compatible with other sites; grailed, poshmark, etsy etc etc
#  - use send keys to fill out info onto the other sites
# get the picture
#create relisting bot for depop
#  shipping helper
# make a layout that contains image, title, brand, size, price, flaws (if any), category of clothing, default presets
##if there are any listed flaws
#era of year clothing was made, and source
#pick 3 default styles
#somehow identify the color; if not no worries, not too crucial
#
# To Do Today
# create layout ////////////////////////
# parse properly and use dictionary/////////////////////

# listing_layout = {
#     "Title": title,
    # "word value": word_value
#     "key word": key_word,
#     "Type of clothing": clothing_type,
#     "Size": size,
#     "Brand": brand, 
# }
#make sure this leads to the pathing for chromedriver, which is in my D: storage
driver = webdriver.Chrome("D:\chromedriver.exe")
driver.get("https://www.whatnot.com/live/9a0fbd0c-d95c-4cea-a414-3388d5085e70")
driver.maximize_window()
time.sleep(random.randint(5, 7))
driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div/div[1]/div[1]/div[2]/h5[1]').click()
brandss = {
    'disney items':['goofy', 'mickey', 'duck', 'disney', 'star'],
    'brands':['jordan', 'quicksilver', 'hard', 'jimmy buffet', 'liquid', 'logo 7', 'adidas', 'guess', 'harley', 'nike', 'reebok', 'nfl', 'russell', 'adidas', 'jordan' 'levi', 'levi\'s', 'looney tunes', 'tommy', 'mitchell', 'marvel', 'nba', 'warner', 'columbia', 'starter', 'lucky brand', 'old navy', 'nautica', 'true religion', 'champion', 'guess', 'patagonia', 'timberland', 'american eagle', 'fashion nova', 'nutmeg', 'ralph lauren', 'santa cruz', 'under armour', 'billabong', 'calvin klein', 'chaps', 'chalk line', 'bke', 'bongo', 'lee', 'polo ralph lauren', 'j crew', 'hollister', 'jerzees', 'hard rock cafe', 'fila', 'coogi', 'carhartt', 'calvin klein'],
    'nfl' :['bucs', 'cardinals', 'falcons', 'raven', 'bills', 'panthers', 'bears', 'bengals', 'browns', 'cowboys', 'broncos', 'lions', 'packers', 'texans', 'colts', 'jaguars', 'chiefs', 'raiders', 'rams', 'chargers', 'dolphins', 'vikings', 'patriots', 'saints', 'giants', 'jets', 'eagles', 'steelers', '49ers', 'seahawks', 'buccaneers', 'titans', 'commanders', 'redskins', '49er'],
    'nba':['76ers', 'hawks', 'bucks', 'bulls', 'cavaliers', 'celtics', 'clippers', 'grizzlies', 'heat', 'hornets', 'jazz', 'kings', 'knicks', 'lakers', 'magic', 'mavericks', 'nets', 'nuggets', 'pacers', 'pelicans', 'pistons', 'raptors', 'rockets', 'spurs', 'suns', 'thunder', 'timberwolves', 'trailblazers', 'warriors', 'wizards'],
    'band':['korn', 'slipknot', 'rob', 'roses', 'nonpoint'],
    'harley':['harley', 'davidson'],
    'nicecar':['busch', 'matt', 'nascar', 'tony', 'dale', 'jimmy', 'johnson', 'jimmie', 'fireball roberts', 'carl long', 'fred lorenzen', 'david reutimann', 'richard childress', 'ned jarrett', 'kyle petty', 'ricky rudd', 'adam petty', 'joe weatherly', 'donnie allison', 'dave marcis', 'tim richmond', 'bobby labonte', 'ricky craven', 'kyle busch', 'geoff bodine', 'bobby allison', 'joey logano', 'junior johnson', 'todd bodine', 'kenny wallace', 'carl edwards', 'denny hamlin', 'jamie mcmurray', 'benny parsons', 'kevin harvick', 'lee petty', 'jeff burton', 'david pearson', 'kurt busch', 'kenseth', 'terry labonte', 'michael waltrip', 'kasey kahne', 'earnhardt', 'cale yarborough', 'alan kulwicki', 'tony stewart', 'jimmie johnson', 'rusty wallace', 'darrell waltrip', 'davey allison', 'dale jarrett', 'mark martin', 'jeff gordon', 'bill elliott', 'dale earnhardt', 'richard petty'],
    'looney tunes':['acme', 'tweety', 'looney tunes', 'taz', 'sylvester'],
    'mlb':['angels', 'astros', 'athletics', 'jays', 'braves', 'brewers', 'cardinals', 'cubs', 'yankee', 'diamondbacks', 'dodgers', 'giants', 'guardians', 'mariners', 'marlins', 'mets', 'nationals', 'orioles', 'padres', 'phillies', 'pirates', 'rangers', 'rays', 'sox', 'reds', 'rockies', 'royals', 'tigers', 'twins', 'sox', 'yankees'],
    'other sport':['hockey', 'golf', 'crochet'],
    'college wear': ['wisconsin', 'michigan', 'stanislaus', 'uc', 'berkeley', 'ucla', 'mjc']
}
article_of_clothing = {
    'shirt':['shirt', 'shir', 'shirtt', 'shit'],
    'jacket':['jacket', 'zipper'],
    'hoodie':['hoodie', 'hooded', 'hodie'],
    'sweatshirt':['longsleeve', 'sweatshirt']
}
sizes = ['4X', '4XL', 'XXXL', 'xxxxl', 'xxxl', ' XXXL', ' 3xl', ' 3XL', ' 2xl', '2x', '2X', ' XXL', ' 2XL', ' xxl', ' Xl', ' xL', 'XL', ' xl', 'xlarge', 'xLarge' ' L', 'large', 'l', ' M', ' m', ' S', ' s']
ne_prices = []
prices_with_index = []
prices = []
numbers = []
specifically_prices = []
word_title_list = []
list_with_only_title = []
updated_list_without_duplicates1 = []
updated_list_without_duplicates2 = []
word_key_list = []
count = 0
stop_words = set(stopwords.words('english'))
new_key = list(brandss.values())
index_key = new_key[0]
time.sleep(2)
def remove_duplicate_listings():
    for layout in word_title_list:
        if layout['title'] not in list_with_only_title:
            list_with_only_title.append(layout['title'])
            updated_list_without_duplicates1.append(layout)
            if layout['word key'] != '??':
                print(layout['word key'])
                updated_list_without_duplicates2.append(layout)
            else:
                word_key_list.append(layout)
def repeating_list(listing):
    for i in listing:
        print(i)
def identify_brand(w):
    global word_key
    run_once = 0
    if run_once == 0:
        if w in brandss['disney items']:
            word_key = "disney"
        elif w in brandss['brands']:
            word_key = "brands"
        elif w in brandss['nfl']:
            word_key = "nfl"
        elif w in brandss['nba']:
            word_key = "nba"
        elif w in brandss['band']:
            word_key = "band"
        elif w in brandss['harley']:
            word_key = "harley"
        elif w in brandss['nicecar']:
            word_key = "nascar"
        elif w in brandss['looney tunes']:
            word_key = "looney tunes"
        elif w in brandss['mlb']:
            word_key = "mlb"
        elif w in brandss['other sport']:
            word_key = "other sport"
        elif w in brandss['college wear']:
            word_key = "college wear"
        else:
            global count
            count += 1
            word_key = '??'
    global word_title_layout
    word_title_layout = {
        "title": titled,
        "word value": w,[]
        "word key": word_key
                        } 
    if word_title_layout not in word_title_list:
        word_title_list.append(word_title_layout)
    run_once = 1

#creates list of numbers so that it only detects prices, not years, sports team, era, etc
numb = list(range(8, 49))
number = list(range(50, 300))
numberss = numb + number
stringed_numbers = [str(x) for x in numberss]
#creates list of title, price, and how many available, still need to get the pic
#######################################
#Main block of text
for other in driver.find_elements('xpath', '//div[@datacy="listing_item"]'):
    prices.append(other.text)
#trims string down with unnessasary words 
for items in prices:
    okk = items.replace("$", "")
    okkd = okk.replace("Start", "")
    ok = okkd.replace("start", "")
    yes = ok.replace("\n", " ")  
    cool = yes.replace("1 Available", "")
    ne_prices.append(cool)

#creating new tuple list with the index by it
updated_title_list = ne_prices [1:]
for i in range(len(updated_title_list)):
    si = i, updated_title_list[i]
    prices_with_index.append(si)

#Checking for sizes
yes = 0
no = 0
for pri in updated_title_list:
    if any(pr in pri for pr in sizes):
        yes += 1
    else:
        no += 1

#Price Check
#Checking for price in indicating whether it needs price or not!
matches = []
non_matches= []
titles_with_price_indication = []
#do this same thing when it comes to finding if it needs size as well, along with hashtags
for title in updated_title_list:
    pattern = re.findall(r"\s[^#-][1-9]\d\d?", title)
    if pattern:
        patter = [i.strip(' ') for i in pattern] 
        # print(patter)
        # print(len(patter[0]))       
        if len(patter[0]) < 2:
            matches.append(patter)
            titles_with_price_indication.append(patter) 
        else: 
            updated_title = (title) + " Confirm Price:"
            non_matches.append(updated_title)
    else:
        updated_title = (title) + " Needs Price:"
        non_matches.append(updated_title)
titles_and_brands = []
titles_no_brands = []
updated_title_list_lower = [x.lower() for x in updated_title_list]
#y article of clothing; shirt, pants, sweater, etc
#make definitions to better identify all the possible options for sumn like nfl; packers, bears, chicago, etc

for titled in updated_title_list_lower:
    title_words = titled.split(" ")
    for ww in title_words:
        for new_keys in new_key:
            for newer_keys in new_keys:
                if ww in newer_keys:
                    ww_split = ww.split(" ")
                    for www in ww_split:
                        if len(www) >= 3:
                            if www not in stop_words:
                               identify_brand(www)
                               remove_duplicate_listings()
repeating_list(updated_list_without_duplicates2)
print(len(updated_list_without_duplicates2))

#Size Check
#printing for loop to make it look nice in the console, rather than jumbled up list

#Scraping Image
all_picture_links = []
for eleme in driver.find_elements('tag name', "img"):
   all_picture_links.append(eleme.get_attribute("src"))
picture_links = all_picture_links[5:123]
picture_length = len(picture_links)

#code to get all pics, and to get the length, of all the necessary pics, may vary depending on amount of items and whatnot
#what to do if there are multiple pics?
#what to do if some dont have pics, how to skip over them and continue the loop through all the listings?
#be able to identify the index of items without size, price, etc and make it easier
#to fill in that info  for the auto posting in excel with bulk list
# #create general message to go with each post, and general hashtags to pick, most popular tags,
#use dictionary to create a proper posting layout
#give me easy way to categorize listing to seperate mids, to highs
#way tofilter so that if it sells on another one of my sites, then it gets rid of it for all,
#with this ill be ablle to simultaneously work with all of my sites, ebay,depop, whatnot, poshmark, grailed, sell 5 times as much, 
#get rid of even more inventory

#what am I trying to get to?
