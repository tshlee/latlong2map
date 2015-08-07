from urllib import urlretrieve

lo=0;
hi=29;

url_zoom="20"
url_size="600x600"
url_format="png"
url_key="AIzaSyB87HHEk5A-fUfbfpQ0kzBXiZNTgPzbyzo"

pstr = "images"

file=open("RV coordinates.txt",'r')
for line in file.readlines()[lo:hi+1]:
	s = line.split(',')

	url_lat = s[0].strip()
	url_long = s[1].strip()

	url = "https://maps.googleapis.com/maps/api/staticmap?center=" +url_lat +"," +url_long +"&zoom=" +url_zoom +"&size=" +url_size +"&maptype=satellite&key=" +url_key +"&format=" +url_format
	fstr = pstr + "/staticmap_%s_%s.%s" % (url_lat, url_long, url_format)

	urlretrieve(url, fstr)
