# What?

Python library to read workflowy exports into a structure.

It's evolving alongside my project to extract workflowy and upload to Confluence.

It will read a file exported from Workflowy (text, html, or opml, right now OPML is chosen) and create an object model of it.

I haven't decided whether it will be Etree-like or Minidom-like, i.e. optimized for a low-memory-use single pass or designed to suck the whole structure in and offer richer navigation, but first I'm implementing the single pass.



