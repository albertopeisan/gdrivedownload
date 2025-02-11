import gdown

if __name__ == '__main__':
    # Add file URLs
    urls = []

    print("Start downloading...")

    for url in urls:
        gdown.download(url, fuzzy=True)

    print("End downloading...")
