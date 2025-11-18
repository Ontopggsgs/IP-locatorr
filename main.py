import requests

print("====================================")
print("   IP locator v2– created by zitsuro")
print("====================================\n")

ip = input("Enemy IP adress: ").strip()

if not ip:
    print("ip adresa nebyla zadana")
    exit()

try:
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()

    if "error" in data:
        print(f" error: {data.get('reason', 'Nepodařilo se získat údaje')}")
        exit()

    print("\n--- Výsledek ---")
    print(f"IP: {data.get('ip')}")
    print(f"Země: {data.get('country_name')}")
    print(f"Město: {data.get('city')}")
    print(f"Region: {data.get('region')}")
    print(f"Poskytovatel: {data.get('org')}")
    print(f"Souřadnice: {data.get('latitude')}, {data.get('longitude')}")
    print("----------------\n")

except Exception as e:
    print(f"neco se pokazilo: {e}")
