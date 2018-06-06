#Rashid Barket's Webscrape v1
#Grabs data from Billboard hot 100 and inputs data into an csv file (open with excel)
#Beautiful soup is the library used to webscrape
#Skills learned from Data Science Dojo (https://www.youtube.com/channel/UCzL_0nIe8B4-7ShhVPfJkgw)

from bs4 import BeautifulSoup as soup
import urllib.request

#url to site I'm going to web scrape, downloading client
gamesite = urllib.request.urlopen('https://www.billboard.com/charts/hot-100')
game_html = gamesite.read()
gamesite.close()
page_soup = soup(game_html, "html.parser")

#grabs all 100 songs
articles = page_soup.findAll("article", {"class":"chart-row"})
article=articles[0] #this will iterate through all songs in for loop below

filename = "topsongs.csv"
f = open(filename, 'w', newline='')
headers = "RANK, SONG, ARTIST, LAST WEEK'S POSITION, HIGHEST POSITION\n"
f.write(headers)

#grabbing all songs

for article in articles:

    song_name = article.findAll('h2',{'class':'chart-row__song'})
    
    if( article.findAll('span', {'class':'chart-row__artist'})):
        song_artist = article.findAll('span', {'class':'chart-row__artist'})

    elif(article.findAll('a',{'class':'chart-row__artist'})):
        song_artist = article.findAll('a',{'class':'chart-row__artist'})
        
    cur_pos = article.findAll('span',{'class':'chart-row__current-week'})

    secondary = article.find('div', {'class':'chart-row__secondary'}) #access to secondary info
    
    last_week = secondary.find('span', {'class':'chart-row__value'})
    last = last_week.text

    highest_pos = secondary.find('div',{'class':'chart-row__top-spot'})
    peak_pos = highest_pos.find('span',{'class':'chart-row__value'})
    high=peak_pos.text
    
    name = song_name[0].text.strip()
    artist = song_artist[0].text.strip()
    pos = cur_pos[0].text.strip()
    prev_pos = last.strip()
    peak = high.strip()
    
    #replace function-commas with semicolons or else csv file will read commas
    f.write(pos + ',' + name.replace(',',';') + ", " + artist.replace(',',';') +  ',' + prev_pos + ',' + peak + "\n")
f.close()

print("success, check for CSV file in same directory\n")


