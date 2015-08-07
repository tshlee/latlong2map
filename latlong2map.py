import sys, os, ntpath
from urllib import urlretrieve

fstrIn = sys.argv[1]
file=open(fstrIn,'r')
lo=0;
hi=3;

url_zoom="20"
url_size="600x600"
url_format="png"
url_key="AIzaSyB87HHEk5A-fUfbfpQ0kzBXiZNTgPzbyzo"

pstrOut = sys.argv[2]
if not os.path.exists(pstrOut):
	os.makedirs(pstrOut)

for line in file.readlines()[lo:hi+1]:
	s = line.split(',')
	url_lat = s[0].strip()
	url_long = s[1].strip()

	url = "https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=%s&size=%s&maptype=%s&key=%s&format=%s" % (url_lat, url_long, url_zoom, url_size, "satellite", url_key, url_format)

	fstr = "%s/%s_%s_%s.%s" % (pstrOut, ntpath.basename(pstrOut), url_lat, url_long, url_format)

	urlretrieve(url, fstr)
