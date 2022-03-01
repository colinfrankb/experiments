import requests
import numpy as np


def standard_requests(endpoint, n):
    result = []
    for i in range(0, n):
        response = requests.get(endpoint)
        result.append(response.elapsed)
    
    return result

def session_requests(endpoint, n):
    session = requests.Session()
    result = []
    for i in range(0, n):
        response = session.get(endpoint)
        result.append(response.elapsed)

    return result

def main():
    endpoint = 'https://sweepsouth.com/_next/static/chunks/pages/index-4ad9c7a9aba82474ce6b.js'
    input_data = standard_requests(endpoint, 100)
    dataset = np.array(list(map(lambda x: float(x.microseconds) / 1000, input_data)))
    dataset.tofile('index-4ad9c7a9aba82474ce6b_dataset_after.csv', '\n')
    print(f'Mean: {np.mean(dataset)}')
    print(f'Median: {np.median(dataset)}')
    print(f'95th Percentile: {np.percentile(dataset, 95)}')
    print(f'99th Percentile: {np.percentile(dataset, 99)}')

if __name__ == '__main__':
    main()
