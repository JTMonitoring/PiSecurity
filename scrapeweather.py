from lxml import html
import requests
from chores import mytts

state = "az"
city = "gilbert"

link = "https://www.wunderground.com/weather/us/az/gilbert"
page = requests.get(link)
tree = html.fromstring(page.content)

weather = tree.xpath('//span[@class="wu-value wu-value-to"]/text()')

mytts("It is "+weather[0]+"degrees in "+city, "en")
