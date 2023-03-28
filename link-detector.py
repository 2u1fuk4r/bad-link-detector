import requests

def is_malicious_url(url):
    response = requests.get(url)
    if response.status_code >= 400:
        return True
    return False

if __name__ == '__main__':
    url = input("Please enter a URL: ")
    if is_malicious_url(url):
        print("The provided URL is malicious!")
    else:
        print("The provided URL is safe to visit.")
