from bs4 import BeautifulSoup

def extract_jpg_filenames(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <img> tags and extract the 'src' attribute
    jpg_filenames = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.endswith('.jpg'):
            # Extract just the filename part
            jpg_filenames.append(src.split('/')[-1])
    
    return jpg_filenames

# Example usage
html_file_path = 'D:/project/PhotoGallery/album/vungtau.html'
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

jpg_filenames = extract_jpg_filenames(html_content)

# Output the list of filenames
for filename in jpg_filenames:
    print(filename)
