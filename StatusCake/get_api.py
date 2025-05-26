import requests
import json

# Ganti dengan API token milik kamu
API_TOKEN = 'r1wcQWH5PRFyxLkmrdMJ'
BASE_URL = 'https://api.statuscake.com/v1/uptime'

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Accept': 'application/json'
}

def get_all_uptime_tests():
    url = f'{BASE_URL}/uptime'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")
        return []

def save_to_json_file(data, filename='monitoring.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"[INFO] Data saved to {filename}")

def print_formatted_data(data):
    for test in data:
        print(f"Name   : {test['name']}")
        print(f"URL    : {test['url']}")
        print(f"Status : {test['status']}")
        print("-" * 40)

if __name__ == '__main__':
    tests = get_all_uptime_tests()
    if tests:
        print_formatted_data(tests)
        save_to_json_file(tests)
    else:
        print("[INFO] No monitoring data found.")
