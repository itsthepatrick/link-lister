import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote

def list_links(url, output_file):
    """Extract and save hyperlinks from the given URL."""
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags
        anchors = soup.find_all('a', href=True)

        # Save links to a file in UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            for anchor in anchors:
                # Convert relative URLs to absolute and decode percent-encoded characters
                link = urljoin(url, unquote(anchor['href']))
                file.write(f"{link}\n")

        print(f"Links saved to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure the "output" directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    while True:
        # Get the URL from the user
        url = input("Enter the URL to extract links (or type 'done' to finish): ")
        if url.lower() == 'done':
            print("Exiting the program. All tasks completed.")
            break

        # Get the file name from the user
        file_name = input("Enter the name for the output file (without extension): ")
        output_file = os.path.join(output_dir, f"{file_name}.txt")

        # Extract and save links
        list_links(url, output_file)
