import urllib2;
from bs4 import BeautifulSoup;

#Declaring URL and folder_path
masterURL = "https://old.reddit.com/r/ImaginaryLeviathans/";
URL = "";
folder_path = "C:/Users/t0rmsanz/Pictures/HarvestedImages/";


#Requesting access as a user-agent that is not a web drone, and also pulling the info
url_request = urllib2.Request( masterURL, headers = {"User-Agent": "Mozilla/5.0"} );

print('Request has been created. . .' + '\n');
print('Retrieving page contents. . .' + '\n');

page_contents = BeautifulSoup( urllib2.urlopen(url_request) );

print('Contents of page have been retrieved!' + '\n');
print('Now initializing downloads. . .' + '\n');

images = page_contents.findAll('a', 'thumbnail');

for image in images:
	
	#Setting url to the current image url in list
	URL = image['href'];
	print('Downloading: \n' + URL); #Looks nice to see which files are being downloaded
	
	while True:
		try:
			#Request/response and setting user-agent
			url_request = urllib2.Request( URL, headers = {"User-Agent": "Mozilla/5.0"} );
			url_response = urllib2.urlopen(url_request);
			
			#Finds '.jpg' in url
			#Finds first '/' that occurs before the '.jpg'
			#Finds all text between '/' and '.jpg'
			#If you're looking at this, I'm sorry; this could be done better in a regex
			name = URL[URL[:URL.find('.jpg')].rfind( '/' )+1:URL.find('.jpg')];
			
			path = (folder_path + name + '.jpg');
			
			#Writing the pictures to the files
			f = open( path, 'wb' );
			f.write(url_response.read());
			f.close();
			
			break;
		except urllib2.URLError:
			print('UNABLE TO RETRIEVE IMAGE FROM: ' + URL);
			break;
		except ValueError:
			print('INVALID URL: ' + URL);
			break;
