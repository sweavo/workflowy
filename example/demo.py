import opml

outline=opml.parse('export.opml')

def descend(node, depth=0):
    print( "  " * depth + "- " + node.text )
    for subelement in node:
        descend(subelement, depth+1)

descend(outline[0])
