import urllib.request


def main():
    # The important detail here is that the domain name of the URL is actually the
    # server container's name, which works because of Docker's automatic service
    # discovery.
    url = "http://iafisher-server:8080/whatever"

    print(f"Sending HTTP request to {url}")
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(f"Got HTTP response with status {response.status}")


if __name__ == "__main__":
    main()
