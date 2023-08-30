import requests

def get_latest_earthquake():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["Infogempa"]["gempa"]
        print("\nInformasi Gempabumi Terbaru:")
        print("Tanggal:", data["Tanggal"])
        print("Jam:", data["Jam"])
        print("Magnitudo:", data["Magnitude"])
        print("Kedalaman:", data["Kedalaman"])
        print("Koordinat:", data["Lintang"], data["Bujur"])
        print("Lokasi:", data["Wilayah"])
        print("Potensi Tsunami:", data["Potensi"])
        print("Dirasakan:", data.get("Dirasakan", "Tidak ada informasi dirasakan"))
    else:
        print("Gagal mengambil data dari API BMKG")

def get_magnitude_5plus_earthquakes():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["Infogempa"]["gempa"]
        print("\nDaftar 15 Gempabumi M 5.0+ Terbaru:")
        for i, quake in enumerate(data[:15], start=1):
            print(f"{i}. Tanggal: {quake['Tanggal']}  Jam: {quake['Jam']}  Magnitudo: {quake['Magnitude']}  Lokasi: {quake['Wilayah']}")
    else:
        print("Gagal mengambil data dari API BMKG")

def get_perceived_earthquakes():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["Infogempa"]["gempa"]
        print("\nDaftar 15 Gempabumi Dirasakan Terbaru:")
        for i, quake in enumerate(data[:15], start=1):
            print(f"{i}. Tanggal: {quake['Tanggal']}  Jam: {quake['Jam']}  Magnitudo: {quake['Magnitude']}  Lokasi: {quake['Wilayah']}  Dirasakan: {quake.get('Dirasakan', 'Tidak ada informasi dirasakan')}")
    else:
        print("Gagal mengambil data dari API BMKG")

def main():
    while True:
        print("\nPilih opsi:")
        print("1. Gempabumi Terbaru")
        print("2. Daftar 15 Gempabumi M 5.0+")
        print("3. Daftar 15 Gempabumi Dirasakan")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == "1":
            get_latest_earthquake()
        elif choice == "2":
            get_magnitude_5plus_earthquakes()
        elif choice == "3":
            get_perceived_earthquakes()
        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Mohon pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
