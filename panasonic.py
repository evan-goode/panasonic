#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from string import digits
digits += "." # for floats
import operator
import json
from random import choice

output = "cheapest.js"
urls = [
	"https://www.amazon.com/dp/B003EM8008",
	"https://www.amazon.com/dp/B003EM6AOG",
	"https://www.amazon.com/dp/B003ELYQHK",
	"https://www.amazon.com/dp/B003ELYQGG",
	"https://www.amazon.com/dp/B003EM2WAW",
	"https://www.amazon.com/dp/B003ELYQJI",
	"https://www.amazon.com/dp/B003EM800S",
	"https://www.amazon.com/dp/B003EM6AQE",
]
user_agents = [
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
]
url = choice(urls)
user_agent = choice(user_agents)
request = requests.get(url, headers = {"User-Agent": user_agent})
soup = BeautifulSoup(request.text, "html.parser")
raw_colors = soup.select("#twister .swatchAvailable, .swatchSelect)")
price_by_color = {}
link_by_color = {}

for raw_color in raw_colors:
	color_name = raw_color.select(".imgSwatch")[0]["alt"].strip().lower()
	price_text = raw_color.select(".a-size-mini")[0].text
	price = float("".join([character for character in price_text if character in digits]))
	price_by_color[color_name] = price
	link_by_color[color_name] = "https://smile.amazon.com/" + raw_color.select(".a-list-item a")[0]["href"]

lowest = min(price_by_color.items(), key = operator.itemgetter(1))
string = "const cheapest = " + json.dumps({
	"color": lowest[0],
	"price": "$" + "%0.2f" % lowest[1],
	"link": link_by_color[lowest[0]]
}) + ";"
print(string)
with open(output, "w") as file:
	file.write(string) # is this bad? yes. is this _that_ bad? no.
