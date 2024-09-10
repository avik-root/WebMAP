import requests  # type: ignore
import pyfiglet  # type: ignore
from termcolor import colored  # type: ignore
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def colored_rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

banner1 = pyfiglet.figlet_format("WebMAP", font="small")
banner2 = pyfiglet.figlet_format("by avik-root", font="digital")
banner3 = pyfiglet.figlet_format("Version 1.1", font="digital")
banner4 = pyfiglet.figlet_format("STABLE", font="digital")
def print_banner():
    r, g, b = random_color()
    print(colored_rgb(r, g, b, banner1))

    r, g, b = random_color()
    print(colored_rgb(r, g, b, banner2))

    r, g, b = random_color()
    print(colored_rgb(r, g, b, banner3))
    print(f"\033[92m{banner4}\033[0m")
def save_to_history(url, directories):
    with open("history.txt", "a") as file:
        file.write(f"Website: {url}\n")
        file.write("Found directories (links):\n")
        for directory in directories:
            file.write(f"{directory}\n")
        file.write("\n")

def extract_directories(url):
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve the website: Status code {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        directories = set()

        for link in links:
            href = link['href']
            full_url = urljoin(url, href)
            if full_url.startswith(url):
                directories.add(full_url)

        print("Found directories (links):")
        for directory in directories:
            print(directory)
        
        save_to_history(url, directories)
        print(f"Results saved to 'history.txt'.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    print_banner()
    while True:
        print("\033[91mGithub: https://github.com/avik-root\033[0m\n\n")
        website_url = input("Enter the website URL (e.g., https://example.com/): ")
        extract_directories(website_url)
        
        cont = input("Do you want to check another website? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
