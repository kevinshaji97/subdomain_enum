import requests


def request(url):
    try:
        return requests.get("https://"+ url)
    except requests.exceptions.ConnectionError:
        pass
        
target_url = "xiaomi.com"

with open("/home/walter/Downloads/Subdomain.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Subdommain found -->" +test_url)

# url = "google.com"
# request(url)