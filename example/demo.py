import opml

class Outline(object):
    def __init__(self, node ):
        if hasattr(node,'text'):
            self.text=node.text
        else:
            self.text=None
        if hasattr(node,'_note'):
            self.note=node._note
        else:
            self.note=None
        self.children=list(map(Outline,node))

    def __repr__(self):
        return f'Outline({self.text!r},{self.note!r},{self.children!r})'

if __name__ == "__main__":

    outline=Outline(opml.parse('export.opml'))

    print(outline)


