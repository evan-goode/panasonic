#!/usr/bin/env python3

###
# quick and dirty: fetches the cheapest color of panasonic 120 on amazon
###

from bs4 import BeautifulSoup
import requests
from string import digits
import operator
import json

digits += "."

out_json = "cheapest.js"
url = "https://www.amazon.com/dp/B003EM8008/"
request = requests.post(url)
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
with open(out_json, "w") as file:
	file.write("const cheapest = " + json.dumps({
		"color": lowest[0],
		"price": "$" + "%0.2f" % lowest[1],
		"link": link_by_color[lowest[0]]
	}) + ";")
