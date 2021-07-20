import opml

outline=opml.parse('export.opml')

def descend(node, depth=0):
    if hasattr(node,'text'):
        print( "  " * depth + "- " + node.text )
    else:
        print('(no text)')

    if hasattr(node,'_note'):
        print( "  " * depth + "  _" + node._note + "_" )

    for subelement in node:
        descend(subelement, depth+1)

if __name__ == "__main__":
    descend(outline)
