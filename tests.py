import requests


def check_route_exists():
    url = "http://127.0.0.1:5000"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Test passed: Status code is 200")
        else:
            print(f"Test failed: Status code is {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Test failed: {e}")


if __name__ == '__main__':
    check_route_exists()
