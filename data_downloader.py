#!/usr/bin/python3
import urllib.request, json, os.path as path

def download_functional_groups():
    save_filename = "functional_groups.json"
    if not path.isfile(save_filename):
        print("Downloading NOAA Functional Group Members Dataset")
        functional_group_address = "https://www.webapps.nwfsc.noaa.gov/apex/parr/functional_group_membership/data/page/"
        json_data = data_downloader(functional_group_address)
        save_file(save_filename, json_data)

def download_diets():
    save_filename = "diets.json"
    if not path.isfile(save_filename):
        print("Downloading Diets Dataset")
        diet_address = "https://www.webapps.nwfsc.noaa.gov/apex/parr/west_coast_fish_mammal_bird_diets_by_functional_group/data/page/"
        json_data = data_downloader(diet_address)
        save_file("diets.json", json_data)

def data_downloader(data_url):
    with urllib.request.urlopen(data_url) as address:
        data = json.loads(address.read())

    return data

def save_file(filename, json_data):
    with open(filename, 'w') as file_bytes:
        json.dump(json_data, file_bytes)

if __name__ == "__main__":
    download_functional_groups()
    download_diets()
