#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from string import digits
digits += "." # for floats
import json
from random import choice

output = "cheapest.json"
products = {
    "B003EM8008": "black",
    "B003ELYQJI": "red",
    "B003EM6AOG": "blue",
    "B003ELYQHK": "green",
    "B003ELYQGG": "orange",
    "B003EM2WAW": "pink",
    "B003EM800S": "silver",
    "B003EM6AQE": "violet"
}
base_url = "https://smile.amazon.com/dp"
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
]
colors = []
for product, color in products.items():
    print("requesting product: %s" % product)
    user_agent = choice(user_agents)
    url = "/".join([base_url, product])
    request = requests.get(url, headers = {"User-Agent": user_agent})
    soup = BeautifulSoup(request.text, "html.parser")
    price_text = soup.select("#price .a-size-medium")[0].text
    price = float("".join([character for character in price_text if character in digits]))
    color = {
        "color": color,
        "price_text": price_text,
        "price": price,
        "link": url,
    }
    colors.append(color)
    print("color: %s" % color)

cheapest = min(colors, key=lambda color: color["price"])
print("cheapest: %s" % cheapest)
with open(output, "w") as pointer:
    json.dump(cheapest, pointer)
