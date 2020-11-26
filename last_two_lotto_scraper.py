import os 
import requests
import csv
from bs4 import BeautifulSoup 


def get_two_digit_lotto():

    two_digit_lotto_url = "http://lotto.sanook.com/2-last/"
    page = requests.get(two_digit_lotto_url)
    soup = BeautifulSoup(page.content, "html.parser")

    data = {
        "date": [],
        "two_digit_lotto": []
    }
    
    for item in soup.find("tbody").find_all("tr"):
        tmp_item = item.find_all("td")
        if len(tmp_item) == 2:
            data["date"].append(tmp_item[0].string)
            data["two_digit_lotto"].append(tmp_item[1].string)

    return data


def write_data_to_json(data):

    current_dir = os.getcwd()
    file_name = "last_two_digit_lotto.csv"
    file_path = os.path.join(current_dir, file_name)

    fields = []
    values = []
    rows = []

    for k, v in data.items():
        fields.append(k)
        values.append(v)
        
    
    for item in zip(values[0], values[1]):
        rows.append(item)

    with open(file_path, 'w', newline='', encoding="utf-8") as out_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


if __name__ == "__main__":
    
    data = (get_two_digit_lotto())  
    write_data_to_json(data)
