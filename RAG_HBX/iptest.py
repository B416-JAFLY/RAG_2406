import requests

def get_ip():
    url = 'http://ifconfig.me'
    response = requests.get(url)
    if response.status_code == 200:
        print("Your IP is:", response.text.strip())
    else:
        print("Failed to retrieve IP")

get_ip()
