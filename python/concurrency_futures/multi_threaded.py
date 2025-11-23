import time
from concurrent.futures import ThreadPoolExecutor

import requests

def fetch_url(url):
    response = requests.get(url)
    return f"{url} -> {response.status_code}"

if __name__ == "__main__":
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2"
    ]

    start = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url, urls))

    # results = [fetch_url(url) for url in urls]
    
    end = time.time()

    print(f"Results: {results}")
    print(f"Single-threaded time: {end - start:.2f} seconds")
