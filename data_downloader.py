import urllib.request, json, requests

def download_functional_groups():
    functional_group_address = 'https://www.webapps.nwfsc.noaa.gov/apex/parr/functional_group_membership/data/page/'
    json_data = data_downloader(functional_group_address)
    save_file("functional_groups.json", json_data)

def download_diets():
    diet_address = 'https://www.webapps.nwfsc.noaa.gov/apex/parr/west_coast_fish_mammal_bird_diets_by_functional_group/data/page/'
    json_data = data_downloader(diet_address)
    save_file("diets.json", json_data)

def data_downloader(data_url):
    with urllib.request.urlopen(data_url) as address:
        data = json.loads(address.read())

    return data

def save_file(filename, json_data):
    # Serialize
    json_obj = json_data.dumps(data, indent=2)
    with open(filename, 'w') as file_bytes:
        file_bytes.write(json_obj)

if __name__ == "__main__":
    download_functional_groups()
    # download_diets()
