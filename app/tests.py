import requests
import sys


def check_route_exists():
    url = "http://127.0.0.1:5000"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Test passed: Status code is 200")
            return 0
        else:
            print(f"Test failed: Status code is {response.status_code}")
            return -1
    except requests.exceptions.RequestException as e:
        print(f"Test failed: {e}")
        return -1


if __name__ == '__main__':
    if t := check_route_exists():
        sys.exit(t)
