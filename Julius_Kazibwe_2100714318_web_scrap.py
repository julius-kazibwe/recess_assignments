import requests
import csv

def fetch_bird_data(base_url, params):
    # Send a request to the provided URL with the specified parameters
    response = requests.get(base_url, params=params)

    # Parse the JSON response data
    data = response.json()

    # Convert numPages to an integer to handle pagination
    num_pages = int(data["numPages"])

    # For demonstration purposes, limit the number of pages to fetch
    num_pages = 1

    bird_data = []

    if "recordings" in data:
        # Loop through the specified number of pages
        for page_num in range(1, num_pages + 1):
            params["page"] = page_num  # Update the page parameter for each iteration
            response = requests.get(base_url, params=params)
            data = response.json()

            if "recordings" in data:
                # Iterate through the recordings on each page
                for recording in data["recordings"]:
                    bird_data.append(recording)

    return bird_data

def get_bird_species():
    # Set the base URL and parameters for fetching bird species
    base_url = "https://xeno-canto.org/api/2/recordings"
    params = {
        "query": "grp:birds",  
        "page": 1,
        "type": "species"
    }
    return fetch_bird_data(base_url, params)

def get_bird_songs():
    # Set the base URL and parameters for fetching bird songs
    base_url = "https://xeno-canto.org/api/2/recordings"
    params = {
        "query": "grp:birds",  
        "page": 1,
        "type": "song"
    }
    return fetch_bird_data(base_url, params)

def save_to_csv(data, filename, fieldnames):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for recording in data:
            # Handle the case where "recording" is an array of fields
            row_data = {}
            for fieldname in fieldnames:
                if isinstance(recording, list):
                    # Join the array values with commas if it's a list
                    row_data[fieldname] = ", ".join(str(item) for item in recording.get(fieldname, []))
                else:
                    row_data[fieldname] = recording.get(fieldname, "")
            writer.writerow(row_data)

if __name__ == "__main__":
    bird_species = get_bird_species()
    bird_songs = get_bird_songs()

    # Save bird species info to CSV
    species_fieldnames = ["id", "gen", "sp", "ssp", "group", "en", "sex", "stage", "rec", "cnt"]
    save_to_csv(bird_species, "bird_species.csv", species_fieldnames)

    # Save bird songs info to CSV
    songs_fieldnames = ["method", "url", "file", "file-name", "sono", "osci", "lic", "q", "length", "time", "date", "uploaded",
                        "also", "rmk", "bird-seen", "animal-seen", "playback-used", "temp", "regnr", "auto", "dvc", "mic", "smp",
                        "rec", "cnt", "loc", "lat", "lng", "type"]
    save_to_csv(bird_songs, "bird_songs.csv", songs_fieldnames)

    print("Data saved to bird_species.csv and bird_songs.csv")
