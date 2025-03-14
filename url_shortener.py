import random
import string


url_mapping = {}

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(long_url):
    short_url = generate_short_url()
    
    while short_url in url_mapping:
        short_url = generate_short_url()
    
    url_mapping[short_url] = long_url
    return f"Shortened URL: http://short.ly/{short_url}"

def retrieve_url(short_url):
    short_code = short_url.split('/')[-1]  
    return url_mapping.get(short_code, "URL not found")

def main():
    print("URL Shortener")
    while True:
        print("\nOptions:")
        print("1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            long_url = input("Enter the long URL: ")
            print(shorten_url(long_url))
        elif choice == '2':
            short_url = input("Enter the shortened URL (e.g., http://short.ly/abc123): ")
            print(retrieve_url(short_url))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
