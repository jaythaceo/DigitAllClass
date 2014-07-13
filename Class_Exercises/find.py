
from xml.etree.ElementTree import parse

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
	lat = float(bus.findtext('lat'))
	busid = bus.findtext('id')
	direction = bus.findtext('d')
	if direction.startswith('North'):
		print(busid, direction, lat)
			
