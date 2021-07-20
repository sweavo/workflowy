import opml

outline=opml.parse('export.opml')

print(outline.__dict__)

