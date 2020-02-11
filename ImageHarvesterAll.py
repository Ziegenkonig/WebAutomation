import urllib2;
import multiprocessing;
import time;
from bs4 import BeautifulSoup;

def finalDownloadStep(file, url_response):

	file.write( url_response.read() );

#Declaring URL and folder_path
masterURLs = ["https://old.reddit.com/r/ImaginaryArchitecture/",
			  "https://old.reddit.com/r/ImaginaryLeviathans/",
			  "https://old.reddit.com/r/ImaginaryCityscapes/",
			  "https://old.reddit.com/r/ImaginaryStarscapes/",
			  "https://old.reddit.com/r/ImaginaryInteriors/",
			  "https://old.reddit.com/r/ImaginaryJedi/",
			  "https://old.reddit.com/r/ImaginaryBestOf/"]


#masterURL = "https://old.reddit.com/r/ImaginaryArchitecture/";
#masterURL = "https://old.reddit.com/r/ImaginaryLeviathans/";
#masterURL = "https://old.reddit.com/r/ImaginaryCityscapes/";
#masterURL = "https://old.reddit.com/r/ImaginaryStarscapes/";
#masterURL = "https://old.reddit.com/r/ImaginaryInteriors/";
#masterURL = "https://old.reddit.com/r/ImaginaryJedi/";
#masterURL = "https://old.reddit.com/r/ImaginaryLibraries/";

URL = "";
folder_path = "C:/Users/*****/Pictures/HarvestedImages/";

for masterURL in masterURLs:


	#Requesting access as a user-agent that is not a web drone, and also pulling the info
	url_request = urllib2.Request( masterURL, headers = {"User-Agent": "Mozilla/5.0"} );

	print('Request has been created. . .' + '\n');
	print('Retrieving page contents. . .' + '\n');

	page_contents = BeautifulSoup( urllib2.urlopen(url_request) );

	print('\nNow harvesting images from: ' + masterURL + '\n');

	print('Contents of page have been retrieved!' + '\n');
	print('Now initializing downloads. . .' + '\n');

	images = page_contents.findAll('a', 'thumbnail');

	for image in images:
		
		#Setting url to the current image url in list
		try:
			URL = image['href'];
			print('Beginning download process for: \n' + URL); #Looks nice to see which files are being downloaded

			while True:
				try:
					#Request/response and setting user-agent
					url_request = urllib2.Request( URL, headers = {"User-Agent": "Mozilla/5.0"} );
					url_response = urllib2.urlopen(url_request);
					
					#Finds '.jpg' in url
					#Finds first '/' that occurs before the '.jpg'
					#Finds all text between '/' and '.jpg'
					#If you're looking at this, i'm sorry; this could be done better in a regex
					name = URL[URL[:URL.find('.jpg')].rfind( '/' )+1:URL.find('.jpg')];
					path = (folder_path + name + '.jpg');

					#Writing the pictures to the files
					print('Opening filepath. . . ');
					f = open( path, 'wb' );
					print('Downloading data. . . ');
					f.write(url_response.read());
					f.close();
					
					print('Download Complete!' + '\n')

					break;
				except urllib2.URLError:
					print('UNABLE TO RETRIEVE IMAGE FROM: ' + URL + '\n');
					break;
				except ValueError:
					print('INVALID URL: ' + URL + '\n');
					break;
				except IOError:
					print('INVALID FILENAME: ' + name)
					break;
		except UnicodeEncodeError:
			print('INVALID ENCODING: Unable to print results due to encoding error.');

		

