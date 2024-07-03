from flask import Blueprint
import requests
from bs4 import BeautifulSoup
import re

views = Blueprint('views', __name__)

@views.route('/')
def home():
    url = 'https://www.nba.com/stats'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    data = soup.find_all('tr')

    # Define the regex pattern
    pattern = r'(\d+)\.\s([A-Za-z\.\s]+)([A-Z]{3})(\d+)'

    count = 0
    current_category = None

    categories = [
        "POINTS", "REBOUNDS", "ASSISTS", "BLOCKS",
        "STEALS", "TURNOVERS", "THREE POINTERS MADE",
        "FREE THROWS MADE", "FANTASY POINTS"
    ]

    result = "<table>"
    for item in data:
        match = re.search(pattern, item.text)
        if match:
            count += 1
            if count % 5 == 1:
                current_category = categories[(count - 1) // 5]
                result += f"<tr><td colspan='4'><strong>{current_category}</strong></td></tr>"
            player_name = match.group(2)
            team_abbreviation = match.group(3)
            points = match.group(4)
            result += f"<tr><td>{match.group(1)}.</td><td>{player_name}{team_abbreviation}</td><td>{points}</td></tr>"

    result += "</table>"
    return result