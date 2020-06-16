from xml.dom import minidom

svg_file = "svg-cards.svg"
doc = minidom.parse(svg_file)  # parseString also exists
for tag in doc.getElementsByTagName('g'):
    print(tag.toxml())
doc.unlink()