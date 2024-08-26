import gdown
import sys

url = sys.argv[1]

def gdownload(url):
	gdown.download_folder(url)
gdownload(url)
