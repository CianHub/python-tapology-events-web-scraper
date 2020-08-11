from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get('https://www.tapology.com/fightcenter')

soup = BeautifulSoup(response.text, 'html.parser')
events = soup.findAll(class_='fcListing')

with open("events.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["event"]
    csv_writer.writerow(headers)
    for event in events:
        event_data = []
        event_formatted = event.get_text().split("\n")
        for item in event_formatted:
            if len(item.strip()) > 1:
                event_data.append(item)
        event = (' '.join(event_data) + '\n')
        csv_writer.writerow([event])
