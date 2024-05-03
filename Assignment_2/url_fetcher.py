
from bs4 import BeautifulSoup
import requests, os, re

# Fetch the content from the URL
def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if 'text' in response.headers['Content-Type']:
            return response.text  # Return text content
        else:
            print("The content from the site is not in UTF-8 format, you should save it as a binary file.")
            return response.content  # Return binary content
    except requests.exceptions.RequestException as e: # Catch all exceptions and print the message from the site
        print(f"Message from the site:\n{e}\n Please check the URL and try again.")
        return None
    
def parse_html(content):
    if not content:
        return None
    Soppa = BeautifulSoup(content, 'html.parser')
    text = Soppa.get_text()
    return text.lower()

# Count the number of dangerous words in the text
def count_dangerous_words(text):
    if not text:
        return 0
    dangerous_words = {"bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"}
    words = re.findall(r'\b\w+\b', text) # Break the words so that it finds only word that are exact
    count = sum(word in dangerous_words for word in words)
    return count

# Sava the text or binary the user fetched
def save_content(content, path):  
    try:
        if os.path.exists(path): # Check if the filename is taken.
            print("File already exists. Please try again with a different name.")
            return False
        if isinstance(content, str):  # if content is text (HTML)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:  # if content is binary (like an image)
            with open(path, 'wb') as f:
                f.write(content)
        print("Saved the file as:", path)
        return True
    except Exception as e:
        print("Saving failed.") 
        return False

def main():
    while True:
        url = input("Input a valid URL: ")
        content = fetch_url(url)
        if content is not None:
            break
    text = parse_html(content)
    if text is not None:
        num_dangerous_words = count_dangerous_words(text)
        print("Number of dangerous words:", num_dangerous_words)
    while True:
        path = input("Input a valid format to save the contents: ")
        if save_content(content, path):
            break

if __name__ == "__main__":
    main()
