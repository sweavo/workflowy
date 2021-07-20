import opml

outline=opml.parse('export.opml')

for element in outline:
    print(element.text)
    for subelement in element:
        print("  " + subelement.text)
