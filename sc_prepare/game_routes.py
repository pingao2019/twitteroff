

import requests
import bs4

game_id = 13

url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)

result = requests.get(url)
print(type(result))
soup = bs4.BeautifulSoup(result.text, features='lxml')

print(soup.find('name').text)
#find the following information about a game:- Name - Max and Min Players - Play Time - Game Description - Some of the game mechanics
print(soup.find('Play Time').text)
print(soup.find('Game Description').text)
print(soup.find('Some of the game mechanics').text)
print(soup.find('Min Players').text)








