import requests

def get_earthquake_data(min_magnitude=5.0, max_results=10):
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "minmagnitude": min_magnitude,
        "limit": max_results,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Gagal mendapatkan data gempa.")
        return None

def main():
    min_magnitude = float(input("Masukkan magnitudo minimum: "))
    max_results = int(input("Masukkan jumlah hasil yang ingin ditampilkan: "))

    earthquake_data = get_earthquake_data(min_magnitude, max_results)
    if earthquake_data:
        print("Daftar gempa terbaru:")
        for idx, feature in enumerate(earthquake_data["features"], start=1):
            properties = feature["properties"]
            place = properties["place"]
            magnitude = properties["mag"]
            print(f"{idx}. Magnitudo: {magnitude}, Lokasi: {place}")

if __name__ == "__main__":
    main()
