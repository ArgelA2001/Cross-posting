from json import tool
from multiprocessing.util import ForkAwareThreadLock
from platform import platform
from sqlite3 import complete_statement
from ssl import OP_NO_COMPRESSION
import this
from timeit import repeat
from tkinter import W
from tkinter.colorchooser import Chooser
from typing import OrderedDict
from zipapp import create_archive
import nltk
import re
import pandas as pd
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from Extract_info_from_excel import excel_total_titles, excel_total_price

#study how stores stand out, what makes people compelled to shop at this store rather than the other, 
#returning customers and reward points
# path = '/Users/Argel Arroyo/Desktop/Selenium_python/depop-bulk-lister.json'
# gc = pygsheets.authorize(service_file=path)
# sheet_title = "1CmQ2IPQ1VIfkIbA_iEk7bPcSYgiBRrJYiKlfietOZ88" 
testing =  ['dockers blue thin quarter zip Medium sweater active 30', 'bongo 2010 Sweatshirt Grey Vintage Reverse Weave Champion XL 30', 'Protect your nuts large hoodie puff print 30']

global size_of_item
excel_titles_strip = []
for titles in excel_total_titles:
    tstrip = titles.strip()
    excel_titles_strip.append(tstrip)

#excel_titles_strip['Vintage Christmas Sweatshirt Oneita Large 90\'s White 25', 'Vintage Christmas Sweatshirt Oneita Large 90\'s White 25']
testing_titles = ['True Religion Women Geno Jeans Size 44 Light Denim Washed $55', 'True Religion Denim Jeans Size 29 Bootcut Womens $45', 'Rock Revival Marlo Straight Size 32 Jeans $45', 'True Religion Geno Jeans Size 44 Light Denim Washed $55']
titles = excel_total_titles
# titles = testing
# print(excel_total_titles)
lower_list = []
titles_and_brands = []
titles_no_brands = []
testing_lower = []

general_description = "PLEASE READ CAREFULLY!! Some items may have unlisted markings, but for the most part all marking would be listed. These clothes are often old and used, so tend to not be in pristine condition. Most items that are listed here will by default be used, unless stated otherwise. Items have not been washed so we also highly recommend that you wash before putting it on.  All items have been handpicked by us. Thank you for choosing to support us at RealVintage._ and if there is anything we can do to make your experience better feel free to send us a message! We also give large discounts if purchasing stuff in bulk."

women_clothing = {'women': ['women', 'woman', 'wmn']}

grailed_pants_category = {
    'Casual Pants': ['chino', 'corduroy', 'slacks'],
    'Cropped Pants': ['crop', 'cropped'],
    'Denim': ['denim'],
    'Leggings': ['leggings', 'spandex', 'tights'],
    'Shorts': ['shorts', 'short'],
    'Sweatpants & Joggers': ['sweatpants', 'sweats', 'joggers'],
    'Overalls & Jumpsuits': ['overalls', 'jumpsuit', 'coveralls'],
}

grailed_tops_category = {
    'Long Sleeve T-Shirts': ['longsleeve', 'long'],
    'Polos': ['polos', 'polo'],
    'Shirts (Button Ups)': ['buttonup', 'buttoned'],
    'Short Sleeve T-Shirts': ['shortsleeve', 'short', 'shirt'],
    'Sweaters & Knitwear': ['sweater', 'knitted', 'knitwear'],
    'Sweatshirts & Hoodies': ['sweatshirt', 'hoodies', 'hoodie', 'hooded'],
    'Tank Tops & Sleeveless': ['tanktop', 'tank', 'nosleeve', 'sleeveless'],
    'Jerseys': ['jersey']
}

brandss = {
    'Adidas': ['adidas', 'adida'],
    'Mitchell & Ness': ['mitchell', 'ness'],
    'Nike': ['nike', 'nik', 'acg', 'nike '],
    'J. Galt': ['j. galt'],
    'NBA': ['unk', 'nba', 'kobe', 'lebron', 'kd', '76ers', 'hawks', 'bucks', 'bulls', 'cavaliers', 'celtics', 'clippers', 'grizzlies', 'heat', 'hornets', 'jazz', 'kings', 'knicks', 'lakers', 'magic', 'mavericks', 'nets', 'nuggets', 'pacers', 'pelicans', 'pistons', 'raptors', 'rockets', 'spurs', 'suns', 'thunder', 'timberwolves', 'trailblazers', 'warriors', 'wizards'],
    'NFL': ['nfl', 'raider', 'raiders', 'packers', 'lions', 'saints', 'cardinals', 'chargers', 'bucs', 'buccanears', 'browns', 'cowboys', '49er', 'ravens', 'broncos', 'seahawk', 'seahawks', 'panthers', 'jets', 'colts', 'falcons', 'jaguars', 'jags', 'chiefs', 'bills', 'eagles', 'rams', 'titans', 'bengals', 'steelers', 'dolphins', 'patriots', 'vikings', 'commanders', 'redskins'],
    'NHL': ['nhl'],
    'MLB': ['mlb', 'angels', 'astros', 'athletics', 'jays', 'braves', 'brewers', 'cardinals', 'cubs', 'yankees', 'diamondbacks', 'dodgers', 'giants', 'guardians', 'mariners', 'marlins', 'mets', 'nationals', 'orioles', 'padres', 'phillies', 'pirates', 'rangers', 'rays', 'sox', 'reds', 'rockies', 'royals', 'tigers', 'twins', 'sox', 'yankees'],
    'Fox Racing': ['fox', 'foxracing'],
    'NASCAR': ['intimidator', 'nascar', 'busch', 'matt', 'nascar', 'tony', 'dale', 'jimmy', 'johnson', 'jimmie', 'fireball roberts', 'carl long', 'fred lorenzen', 'david reutimann', 'richard childress', 'ned jarrett', 'kyle petty', 'ricky rudd', 'adam petty', 'joe weatherly', 'donnie allison', 'dave marcis', 'tim richmond', 'bobby labonte', 'ricky craven', 'kyle busch', 'geoff bodine', 'bobby allison', 'joey logano', 'junior johnson', 'todd bodine', 'kenny wallace', 'carl edwards', 'denny hamlin', 'jamie mcmurray', 'benny parsons', 'kevin harvick', 'lee petty', 'jeff burton', 'david pearson', 'kurt busch', 'kenseth', 'terry labonte', 'michael waltrip', 'kasey kahne', 'earnhardt', 'cale yarborough', 'alan kulwicki', 'tony stewart', 'jimmie johnson', 'rusty wallace', 'darrell waltrip', 'davey allison', 'dale jarrett', 'mark martin', 'jeff gordon', 'bill elliott', 'dale earnhardt', 'richard petty'],
    
    'Harley Davidson': ['harley', 'davidson'],
    'Anti Social Social Club': ['anti', 'social', 'social club', 'social clubs'],
    'Arc\'tyrex': ['arc', 'tyrex', 'arctyrex', "arc'tyrex"],
    'Armani': ['exchange', 'armmani'],
    'Asics': ['asics', 'asic'],
    'BONGO': ['bongo', 'bongos'],

    'Balenciaga': ['bal', 'enciaga', 'balenciaga', 'balenci'],
    
    'Birkenstock': ['birks', 'birk', 'birkenstock'],
    'Calvin Klein': ['calvin', 'klein', 'calvin klein'],
    'Cambridge Classics': ['cambridge', 'classics'],
    'Buckle': ['buckle', 'bke'],
    'Chalk Line': ['chalk'],
    'Champion': ['champion'],
    'Cherokee': ['cherokee'],
    'Citizens of Humanity': ['citizens', 'humanity', 'humanities', 'humanity'],
    'Coca-Cola': ['coca', 'cola', 'coca-cola'],
    'Cole Haan': ['cole', 'haan', 'colehaan'],
    'Columbia': ['columbia', 'columbi'],
    'Coogi': ['coogi'],
    'DC Comics': ['dc'],
    'Dickies': ['dickies'],
    'Disney': ['goofy', 'mickey', 'duck', 'disney', 'star', 'boba fett'],
    'Dr. Martens': ['martens', 'marten'],
    'Ecko Unltd.': ['ecko', 'unlimited', 'unltd.', 'unltd'],
    'Ed Hardy': ['hardy'],
    'Fear of God': ['fear', 'god', 'fear of god', 'fog'],
    'Forever 21': ['forever'],
    'G-III': ['g', 'iii', 'g-iii'],
    'GANT': 'gant',
    'Goodfellow & CO': ['goodfellow'],
    'Guess': ['guess'],
    'Hard Rock Cafe': ['hard', 'cafe', 'rock cafe'],
    'JNCO': ['jnco'],
    'Jerzees': ['jerzees'],
    'Jordan': ['jordan', 'jordans', 'jorda'],
    'Kappa': 'kappa',
    'LRG': ['lrg'],
    'Land\'s End': ["land's", 'lands'],
    'Levi': ['levi', 'levis', 'levi\'s'],
    'Liquid Blue': ['liquid'],
    'Looney Tunes': ['acme', 'tweety', 'looney tunes', 'taz', 'sylvester', 'jam'],
    'Lucky Brand': ['lucky'],
    'L.L. Bean': ['ll', 'bean'],
    'Lululemon': ['lululemon', 'lulu'],
    'Marvel': ['marvel', 'spiderman', 'spider-man', 'captain america', 'thor', 'iron man', 'iron-man', 'deadpool', 'marvel'],
    'Miss Me': ['miss', 'me'],
    'Murano': 'murano',
    'Nautica': ['nautica'],
    'New Balance': ['balance'],
    'New Era': ['new era', 'era', 'newera'],
    'Nordstrom': ['nordstrom'],
    'Obermeyer': 'obermeyer',
    'Old Navy': ['oldnavy', 'old'],
    'Oskar Haug': ['haug'],
    'Patagonia': ['pata', 'patagonia'],
    'Planet Hollywood': ['planet', 'hollywood'],
    'Polo Ralph Lauren': ['polo'],
    'Primitive': 'primitive',
    'Pro Player': ['pro player'],
    'Quiksilver': ['quicksilver', 'quiksilver'],
    'RSQ': ['rsq'],
    'Ralph Lauren': ['ralph', 'lauren'],
    'Reebok': ['reebok', 'reeboks'],
    'Rocawear': ['rocawear', 'roca'],
    'Rock Revival': ['rock revival', 'revival'],
    'RVCA': 'rvca',
    'Russell Athletics': ['russell', 'russel'],
    'Salty Crew': ['salty', 'crew'],
    'Star Wars': ['star', 'wars', 'boba', 'yoda', 'mandalorian'],
    'Starter': ['starter', 'starters'],
    'Stussy': 'stussy',
    'Supreme': ['supreme'],
    'The Mountain': ['mountain', 'the mountain'],
    'The North Face': ['north', 'northface'],
    'Timberland': ['timberland', 'timbs', 'timb'],
    'Tommy Bahama': 'bahama',
    'Tommy Hilfigher': ['tommy', 'hilfiger', 'hilfigher'],
    'True Religion': ['true', 'religion'],
    'UGG': 'ugg',
    'Under Armour': ['under', 'armour'],
    'Vans': 'vans',
    'Vineyard Vines': ['vineyard', 'vines', 'vineyards'],
    'Von Dutch': ['von', 'dutch', 'vondutch'],
    'WWE': ['stone cold', 'wwe'],
    'Logo Athletic': ['logo', 'athletic'],
    'Zara': 'zara',
    'Baby Phat': 'baby',
    'American Eagle Outfitters': ['american', 'eagle'],
    'Carhartt': 'carhartt',
    'extras': ['dockers', 'eastland', 'dickies', 'apple', 'aeropostale', 'gymshark', 'guess', 'gymboree', 'ghirardelli', 
                'bebe', 'camel', 'crocs', 'clarks' 'coach', 'dior', 'footjoy', 'ferrari', 'funko', 'fendi',
                'gillette', 'gap', 'keen', 'kith', 'quicksilver', 'minecraft', 'nutmeg', 'obey', 'samsung', 'cabela', 'majestic', 'wrangler', 'woolrich', 'ariat',
                'pendleton', 'converse', 'fila', 'kangol', 'lacoste', 'playboy', 'polaroid', 'chaps', 'billabong', 'lacoste', 'thrasher', 'bape'],
    'American Vintage': ['vintage', 'vnt', 'vtg', '90\'s'],
    }
sizes = {
    
    'L' :['large', 'l'],
    'M' :['medi', 'medium', 'mediun', 'm'], 
    'S' :['small', 'smal', 's'],
    '4XL' :['4x', '4xl', 'xxxxl'], 
    '3XL' :['3x', '3xl', 'xxxl'], 
    '2XL' :['2x', '2xl', 'xxl'], 
    'XL' :['xl'], 
    'XS': ['xs'],
    'XXS': ['xxs'],
    'PANTSSIZE': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', 
                  '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '42', '43', '44', '45', '46', '47', '48', '49', '50'
                  "26x28", "26x30", "26x32", "26x34", "27x28", "27x30", "27x32", "27x34", "28x28", "28x30", "28x32", "28x34", "29x28", "29x30", "29x32", "29x34", 
                  "30x28", "30x30", "30x32", "30x34", "31x28", "31x30", "31x32", "31x34", "32x28", "32x30", "32x32", "32x34", "33x28", "33x30", "33x32", "33x34", "34x28", 
                  "34x30", "34x32", '34x33', "34x34","36x28", "36x30", "36x32", "36x34", "38x28", "38x30", "38x32", "38x34", "40x28", "40x30", "40x32", "40x34", "42x28", "42x30", "42x32", 
                  "42x34", "44x28", "44x30", "44x32", "44x34", "46x28", "46x30", "46x32", "46x34", "48x28", "48x30", "48x32", "48x34", "50x28", "50x30", "50x32", "50x34", "52x28", "52x30", "52x32", "52x34"]
}
colors = {
    'color': ['black', 'blue', 'brown', 'burgundy', 'cream', 'gold', 'green', 'grey', 'khaki', 'multi', 'navy', 'orange', 'pink', 'purple', 'red', 'silver', 'tan', 'white', 'yellow', 'gray']
}
category = {
    #category for dropdown menu::: mostly going to be either shirts, jackets or coats, for now, later will add shoes, shorts, hats, etc
    'Sweatshirts':['sweat', 'pullover', 'long sleeve', 'longsleeve', 'sleeve', 'sweatshirt'],
    'T-Shirts' :[' shirt', 'shirt', 'Shirt', ' shirt ' 'shir', 'shit', 'vest'],
    'Jacket':['jacket', 'jacket ', 'Jacket'],
    'Hoodie':['hoodie', 'hooded', 'hoody', 'Hoodie'],
    'Sweaters':['sweater'],
    'Jerseys': ['jersey'],
    'Shirts (Button Ups)': ['flannel'],
    'Pants': ['pants', 'pant'],
    'Jeans': ['jeans', 'jean'],
    'Sweatpants': ['sweats', 'sweatpants', 'joggers', 'leggings', 'legging'],
    'Shorts': ['shorts', 'short', 'jorts'],
    'Hat': ['hat', 'cap', 'snapback', 'bucket', 'beanie', 'sheisty'],
    'Coat': ['coat'],
    'Vests': ['vest'],
    'Shoes': ['shoes', 'shoe', 'sneaker', 'sandal', 'flipflop', 'cleat'],
    }
condition = {
    'New':['deadstock', 'ds', 'new', 'nwt', 'new with tags', 'with tag', 'new with tag', 'brand new'],
    'Damaged':['distressed', 'tear', 'stained', 'stain', 'tear', 'hole', 'flaw']
    }
age = {
    'modern':['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    'Y2K': ['y2k', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008','2009'],
    '90': ['90\'s', '91', '92', '93', '94', '95', '96', '97', '98', '99']
}
# sub_category = {
#     # for posmark really
# }

def checking(counting):
    print('checking function')
    print(excel_total_titles[counting])
    # print(testing[counting])
    print(grailed_category_list[counting])
    print(grailed_brand_list[counting])
    print(condition_list[counting])
    # print(grailed_size_list[counting])
    print('   ')

count = 0
new_key = list(brandss.values())
condtion_keys = list(condition.values())
new_size = list(sizes.values())
numb = list(range(10, 48))
number = list(range(50, 90))
numba = list(range(91, 300))
numberss = numba + numb + number
stringed_numbers = [str(x) for x in numberss]
number_w_dolla = ["$" + string for string in stringed_numbers]
word_title_list = []
list_with_only_title = []
list_with_only_title2 = []
updated_list_without_duplicates1 = []
final_result_updated_list = []
updated_list_without_duplicates3 = []
updated_list_without_duplicates4 = []
word_key_list = []
prices_with_index = []
matches = []
non_matches= []
identify_price_list = []
all_key_total = []
identify_price_list_titles = []
condition_values = []
for new_keys in new_key:
    for newer_keys in new_keys:
        all_key_total.append(newer_keys)

for value in condtion_keys:
    for val in value:
        condition_values.append(val)
#function to match words with brandss value

def lower(list):
    for lis in list:
        yup = lis.lower()
        lower_list.append(yup)

def repeating_list(listing):
    for i in listing:
        print(i)
    print(len(listing))


total_condition_values = sum([len(condition[x]) for x in condition if isinstance(condition[x], list)])                        
condition_list = []
def updated_condition_function(titles):
    global count
    count = 0
    for titled in titles:
        titledd = titled.lower().split(' ')
        found_condition = False
        for key, value in condition.items():
            for title_words in titledd:
                if title_words == value:
                    condition_list.append(key.title())
                    # print(title_words.title())
                    # print(key.title())
                    found_condition = True
                    break
            if found_condition:
                break
        else:
            condition_list.append('Excellent')

tops_bottoms_outerwear_footwear_for_grailed = []
depop_category_list = []
grailed_category_list = []
def updated_category_function(titles):
    for titled in titles:
        titledd = titled.lower().split(' ')
        found_category = False
        for key, value in category.items():
            for title_words in titledd:
                if title_words in value:
                    depop_category_list.append(key.title())
                    grailed_category_list.append(key.title())
                    # print(title_words.title())
                    # print(key.title())
                    found_category = True
                    if key.title() == 'Sweatshirts' or key.title() == 'T-Shirts' or key.title() == "Hoodie" or key.title() == 'Sweaters' or key.title() == 'Jersey' or key.title() == 'Shirts':
                        tops_bottoms_outerwear_footwear_for_grailed.append('Tops')
                        # print('Tops')
                    elif key.title() == 'Jacket' or key.title() =='Coat' or key.title() == 'Vest':
                        tops_bottoms_outerwear_footwear_for_grailed.append('Outerwear')
                        # print('Outerwear')
                    elif key.title() == 'Pants' or key.title() == 'Jeans' or key.title() =='Sweatpants' or key.title() == 'Shorts':
                        tops_bottoms_outerwear_footwear_for_grailed.append('Bottoms')
                        # print('Bottoms')
                    elif key.title() == 'Shoes':
                        tops_bottoms_outerwear_footwear_for_grailed.append('Footwear')
                        # print('Footwear')
                    elif key.title() == 'Hats':
                        tops_bottoms_outerwear_footwear_for_grailed.append('Accessories')
                        # print('Accessories')
                    else:
                        tops_bottoms_outerwear_footwear_for_grailed.append(' ')
                    break
            if found_category:
                break
        else:
            depop_category_list.append(' ')
            grailed_category_list.append(' ')

grailed_pants_category_list = []
def grailed_pants_category_function(titles):
    for titled in titles:
        titledd = titled.lower().split(' ')
        found_pants_category = False
        for key, value in grailed_pants_category.items():
            for title_words in titledd:
                if title_words in value:
                    grailed_pants_category_list.append(key.title())
                    # print(title_words.title())
                    # print(key.title())
                    found_pants_category = True
                    break
            if found_pants_category:
                break
        else:
            grailed_pants_category_list.append(' ')

grailed_tops_category_list = []
def grailed_tops_category_function(titles):
    for titled in titles:
        titledd = titled.lower().split(' ')
        found_tops_category = False
        for key, value in grailed_tops_category.items():
            for title_words in titledd:
                if title_words in value:
                    grailed_tops_category_list.append(key.title())
                    # print(title_words.title())
                    # print(key.title())
                    found_tops_category = True
                    break
            if found_tops_category:
                break
        else:
            grailed_tops_category_list.append(' ')

total_age_values = sum([len(age[x]) for x in age if isinstance(age[x], list)])
age_list = []
depop_age_list = []
def age_function(titles):
    global age_count
    age_count = 0
    no_count = 0
    for titled in titles:
        titledd = titled.lower()
        for ages in age.values():
            for ind_age in ages:
                age_count += 1
                if ind_age not in titledd:
                    no_count += 1
                    if no_count == total_age_values:
                        depop_age = 'Modern'
                        if titled not in age_list:
                            depop_age_list.append(depop_age)
                            age_list.append(titled)
                            no_count = 0
                else:
                    if ind_age in age['90']:
                        age_of_item = '90s (90s)'
                        depop_age = 'Vintage'
                        
                    elif ind_age in age['Y2K']:
                        age_of_item = '00s (y2k)'
                        depop_age = 'Y2K'
                    elif ind_age in age['modern']:
                        age_of_item = 'Modern (modern)'
                        depop_age = 'Modern'
                    no_count = 0
                    if titled not in age_list:
                        depop_age_list.append(depop_age)
                        age_list.append(titled)
                        no_count = 0

total_colors_values = sum([len(colors[x]) for x in colors if isinstance(colors[x], list)])
grailed_color_list = []
depop_color_list = []
color_title = []
color_tuple = []
def color_function(titles):
    global grailed_color
    global fill_count 
    global color_tupe
    no_count = 0
    grailed_color = ''
    depop_color = ''
    for titled in titles:
        titledd = titled.lower()
        for color in colors.values():
            for ind_color in color:
                if ind_color not in titledd:   
                    no_count += 1
                    if no_count == total_colors_values:
                        depop_color = " "
                        grailed_color = 'Blanc'
                        if titled not in color_title:
                            depop_color_list.append(depop_color)
                            grailed_color_list.append(grailed_color)
                            color_title.append(titled)
                            no_count = 0
                else:
                    no_count = 0
                    if ind_color == 'black':
                        depop_color = 'Black'
                        grailed_color = "Black"
                    elif ind_color == 'blue':
                        depop_color = 'Blue'
                        grailed_color = "Blue"
                    elif ind_color == 'brown':
                        depop_color = 'Brown'
                        grailed_color = "Brown"
                    elif ind_color == 'burgundy':
                        depop_color = 'Burgundy'
                        grailed_color = "Burgundy"
                    elif ind_color == 'cream':
                        depop_color = 'Cream'
                        grailed_color = "Cream"
                    elif ind_color == 'gold':
                        depop_color = 'Gold'
                        grailed_color = "Gold"
                    elif ind_color == 'green':
                        depop_color = 'Green'
                        grailed_color = "Green"
                    elif ind_color == 'grey' or ind_color == 'gray':
                        depop_color = 'Grey'
                        grailed_color = "Grey"
                    elif ind_color == 'khaki':
                        depop_color = 'Khaki'
                        grailed_color = "Khaki"
                    elif ind_color == 'navy':
                        depop_color = 'Navy'
                        grailed_color = "Navy"
                    elif ind_color == 'orange':
                        depop_color = 'Orange'
                        grailed_color = "Orange"
                    elif ind_color == 'pink':
                        depop_color = 'Pink'
                        grailed_color = 'Pink'
                    elif ind_color == 'purple':
                        depop_color = 'Purple'
                        grailed_color = 'Purple'
                    elif ind_color == 'red':
                        depop_color = 'Red'
                        grailed_color = 'Red'
                    elif ind_color == 'silver':
                        depop_color = 'Silver'
                        grailed_color = 'Silver'
                    elif ind_color == 'tan':
                        depop_color = 'Tan'
                        grailed_color = 'Tan'
                    elif ind_color == 'white':
                        depop_color = 'White'
                        grailed_color = 'White'
                    elif ind_color == 'yellow':
                        depop_color = 'Yellow'
                        grailed_color = 'Yellow'
                    elif ind_color == 'multi':
                        depop_color = 'Multi'
                        grailed_color = 'Multi'
                    no_count = 0
                    if titled not in color_title:
                        grailed_color_list.append(grailed_color)
                        depop_color_list.append(depop_color)
                        color_tupe = titled, depop_color
                        color_title.append(titled)
                        color_tuple.append(color_tupe)

size_list = []
def size_function(titles):
    for titled in titles:
        titledd = titled.lower().split(' ')
        found_size = False
        for key, value in sizes.items():
            if found_size:
                break
            for title_words in titledd:
                if title_words in value:
                    found_size = True
                    if key == 'PANTSSIZE':
                        size_for_pants = title_words
                        waist_size = size_for_pants.split('x')[0]
                        waist_size = size_for_pants.split('X')[0]
                        size_list.append(waist_size)
                        # print('waist_size')
                        break
                    else:
                        size_list.append(key) 
                        break
        if not found_size:
            size_list.append('')

gender_list = []
def women_function(titles):
    for titled in titles:
        # print(titled)
        titledd = titled.lower().split(' ')
        found_women = False
        for key, value in women_clothing.items():
            for title_words in titledd:
                if title_words in value:
                    gender_list.append(key.title())
                    # print('Women')
                    # print(title_words.title())
                    # print(key.title())
                    found_women = True
                    break
            if found_women:
                break
        else:
            gender_list.append('Men')
            # print('Men')

depop_brand_list = []
grailed_brand_list = []
def updated_brand_function(titles):
    for titled in titles:
        titledd = titled.lower().split(' ')
        found_brand = False
        for key, value in brandss.items():
            if any([v.lower() in titledd for v in value]):
                # print('        ')
                # print(titled)
                if key == 'extras':
                    for v in value:
                        if v.lower() in titledd:
                            depop_brand_list.append(v.title())
                            grailed_brand_list.append(v.title())
                            found_brand = True
                            # print(v.title())
                            break
                else:
                    if found_brand == True:
                        break
                    else:
                        depop_brand_list.append(key)
                        grailed_brand_list.append(key)
                        found_brand = True
                        # print(key)
                        break
        if not found_brand:
            depop_brand_list.append('')
            grailed_brand_list.append('')

final_final_list = []
def combining_lists_for_depop():
    global total_list
    global category_list
    global price_lists
    global sizing_list
    global overall_final_list
    z = zip(excel_total_titles, depop_category_list, excel_total_price, grailed_brand_list, condition_list, size_list, grailed_color_list)
    for item in z:
        print(item)
        final_final_list.append(item)

def numbered_list(list):
    for i, item in enumerate(list):
        print(i+1, item)
#this enters every single possible thing but the size text, says its invalid for some reason, and I need some help
#everything else works, but the size for some reason, it has to be a depop problem
def create_google_sheet():
    global final_final_list
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = '/Users/Argel Arroyo/Desktop/Selenium_python/depop-bulk-lister.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # The ID and range of a sample spreadsheet.
    spreadsheet_id = '1FHHJ6j0XdHggqJJEQ6MI4eua1H5FiJAQ'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets() 
    range_doc = 'Template!A5:Q110'
    request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_doc, valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values':final_final_list}).execute()

def turning_dictionary_into_list():
    for listin in overall_final_list:
        print(listin.values())
        print('yuh')

################################
#MAIN CHUNK OF CODING
################################
print("Start of Main Chunk of Code")
print("     ")
print("     ")
print("     ")

#color, brand, size, price, condition, category

color_function(titles)
updated_brand_function(titles)
size_function(titles)
age_function(titles)
updated_category_function(titles)
updated_condition_function(titles)
women_function(titles)
grailed_pants_category_function(titles)
grailed_tops_category_function(titles)
# print(size_list)

# numbered_list(size_list)
# print(grailed_tops_category_list)
# combining_lists_for_depop()

def find_diff(missing_list):
    print(' ')
    print('find diff')
    missing_keys = list(set(excel_total_titles) - set(missing_list))
    print(len(missing_keys))
    print(missing_keys)
    print(' ')

def zip_check(missing_list):
    print('  ')
    print('zip check')
    count = 0
    zz = zip(excel_total_titles, missing_list)
    for item in zz:
        print(item)
        count += 1
    print(count)
    print(len(missing_list))
    print(count)
    print(' ')

def printing_list(list):
    print(len(list))
    for index, item in enumerate(list, start=1):
        print(f"{index}. {item}")
printing_list(size_list)


#THOUGHTS ON PROJECT
# Just fixed the identify_size function, was pretty difficutl, but did it and was able to clean up the code in it a bit too,
# identify price is correct too, gives a full 199
# each of these are off by a few so i got to figure out how and why they are off by a bit
# identify_brand is still only returning half of the total, but its good that price and size are taken care of,
# numbered should be easy, title too
# other than figuring out how to only get one sentence to pass through rather than like the same one 6 times but i think i can use the samefile
# filtering method I used in size definition, 
# also am going to need the pictures from it to, adn to be able to transfer,
# i dont want my computer getting stormed with pics like my phone, so i need to be able to go through files too, and i need to properly install my hard drive
#then once that is done i can create an overall layout and enter that in to a google shes

# Ideas for depop, how to use drop down method?
# maybe instead of using bulk lister, just find out how to sign in with bot.

#Ideas to upgrade this
# make the brand function work so that 1, the words have to be exact, not just partly
#2 the words can use the combine with the letter in front or behind it to be even more accurate for those with 2, but that it could still use just 1 word, but using 2 would be more accurate

