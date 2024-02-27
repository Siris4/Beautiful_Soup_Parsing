from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()    #you must indent!!
    # print(contents)

#BeautifulSoup is the class

#then, we create an object from that Class, pass in the contents, and then the parser)
soup = BeautifulSoup(contents, "html.parser")   # or use lxml for XML content, if HTML is not working

print(soup)

print(f"The title tag (soup.title) is: {soup.title}")
print(f"The name of that particular title tag (title.name) is: {soup.title.name}")
print(f"The string that is contained inside the title tag (title.string) is: {soup.title.string}\n")

print(f"The soup.heading (Heading) is: {soup.heading}")
print(f"The soup.h3 (Heading - level 3) is: {soup.h3}")
print(f"The soup.class (Class) is {soup.__class__}")

print(soup.prettify())

# to find the first anchor tag in the website, use:
print(soup.a)

# the first list item (li):
print(soup.li)

#the first paragraph only:
print(soup.p)

# ALL of the items of a particular group:
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

all_paragraph_tags = soup.find_all(name="p")
print(all_paragraph_tags)

all_list_item_tags = soup.find_all(name="li")
print(all_list_item_tags)