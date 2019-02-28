import urllib2;
from bs4 import BeautifulSoup;

#Declaring URL and folder_path
masterURL = "https://www.reddit.com/r/ImaginaryLeviathans/";
URL = "";
folder_path = "C:/Users/t0rmsanz/Pictures/HarvestedImages/harvest";


#Requesting access as a user-agent that is not a web drone, and also pulling the info
url_request = urllib2.Request( masterURL, headers = {"User-Agent": "Mozilla/5.0"} );

page_contents = BeautifulSoup( urllib2.urlopen(url_request) );

images = page_contents.findAll('a', 'thumbnail');
print( len(images) );

index = 0;
for image in images:
	
	#Setting url to the current image url in list
	URL = image['href'];
	print(URL); #Looks nice to see which files are being downloaded
	
	while True:
		try:
			#Request/response and setting user-agent
			url_request = urllib2.Request( URL, headers = {"User-Agent": "Mozilla/5.0"} );
			url_response = urllib2.urlopen(url_request);
			
			path = (folder_path + str(index+1) + '.jpg');
			#Writing the pictures to the files
			f = open( path, 'wb' );
			f.write(url_response.read());
			f.close();
			
			index += 1;
			break;
		except urllib2.URLError:
			print('UNABLE TO RETRIEVE IMAGE FROM: ' + URL);
			break;
		except ValueError:
			print('INVALID URL: ' + URL);
			break;
