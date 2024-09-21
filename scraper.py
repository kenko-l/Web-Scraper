import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def scrape():
    url = 'https://www.simpleshop.com/'  # Replace with the URL you're scraping

    # Fetch the page content
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    # Save the entire HTML content to a file
    with open("../Web-Scraper/page.html", "w", encoding='utf-8') as f:
        f.write(soup.prettify())  # Writes the formatted HTML to the file


    # Extract HTML, CSS, and JavaScript files

    # HTML files
    '''html_files = []
    for link in soup.find_all("a"):
        href = link.attrs.get("href")
        if href and href.endswith(".html"):  # Assuming HTML files end with .html
            html_url = urljoin(url, href)
            html_files.append(html_url)'''

    # JavaScript files
    script_files = []
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)

    # CSS files
    css_files = []
    for css in soup.find_all("link"):
        if css.attrs.get("href") and "stylesheet" in css.attrs.get("rel", []):
            css_url = urljoin(url, css.attrs.get("href"))
            css_files.append(css_url)

    # Output the results
    print("Total script files in the page: ", len(script_files))
    print("Total CSS files in the page: ", len(css_files))

    # Save the extracted links to text files
    with open("../Web-Scraper/javascript_files.txt", "w") as f:
        for js_file in script_files:
            print(js_file, file=f)

    with open("../Web-Scraper/css_files.txt", "w") as f:
        for css_file in css_files:
            print(css_file, file=f)

# Execute the scraping function
if __name__ == '__main__':
    scrape()
