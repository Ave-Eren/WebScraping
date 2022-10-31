from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file: # opens file in read mode and names the file object "html_file"
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # soup.prettify() basically returns the html in a more readable format
    tags = soup.find_all('a')  # returns a list of all the <a> tags in the html
    # .find() returns the first instance of the tag
    for tag in tags:
        print(tag.get('href'))  # prints the href attribute of the tag
        print(tag.text)  # prints the text inside the tag
        print(tag.attrs)  # prints the attributes of the tag
        print(tag.string)  # prints the string inside the tag
        print(tag.name)  # prints the name of the tag
        print(tag.parent.name)  # prints the name of the parent tag

    # We should use Inspect to get all the HTML code on hostile websites
    # Copilot: We can also use the requests library to get the HTML code of a website
    course_cards = soup.find_all('div', class_='card')  # returns a list of all the <div> tags with the class "card"
    for(course_card) in course_cards:
        course_name = course_card.h5.text
        course_price = course_card.a.text.split()[-1]
        # .a returns the first <a> tag in the current card, .text returns the text inside the tag
        print(f'{course_name} costs {course_price}')

# I feel so powerful with this lmao, but still sleepy

from bs4 import BeautifulSoup
import requests

# Target Website: PharmEasy, PinCode: 143001 (Amritsar) Search query: Paracetamol
html_text = requests.get('https://pharmeasy.in/search/all?name=Paracetamol').text
print(html_text.text)  # This is the HTML code of the website
soup = BeautifulSoup(html_text, 'lxml')

# Now I inspect the page and see what elements I need to extract/grab

meds = soup.find_all('li', class_='drug-card')
drug_name = meds[0].find('div', class_='drug-name').text.replace(' ', '')
print(drug_name)
for med in meds:
    med_name = med.find('h3', class_='drug-name').text
    med_price = med.find('span', class_='price').text
    print(f'{med_name} costs {med_price}')

