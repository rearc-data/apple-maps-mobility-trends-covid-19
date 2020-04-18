import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import boto3
import os
import urllib.request

def source_dataset(new_filename, s3_bucket, new_s3_key):

	# instantiate a chrome options object so you can set the size and headless preference
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--window-size=1280x1696')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--user-data-dir=/tmp/user-data')
	chrome_options.add_argument('--hide-scrollbars')
	chrome_options.add_argument('--enable-logging')
	chrome_options.add_argument('--log-level=0')
	chrome_options.add_argument('--v=99')
	chrome_options.add_argument('--single-process')
	chrome_options.add_argument('--data-path=/tmp/data-path')
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--homedir=/tmp')
	chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
	chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
	chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

	driver = webdriver.Chrome(chrome_options=chrome_options)

	driver.get("https://www.apple.com/covid19/mobility")
	time.sleep(5)

	class_element = driver.find_element_by_class_name('download-button-container')
	a_element = class_element.find_element_by_tag_name("a")
	source_dataset_url = a_element.get_attribute('href')

	# Download the file from `url` and save it locally under `file_name`:
	urllib.request.urlretrieve(source_dataset_url, '/tmp/' + new_filename)

	#uploading new s3 dataset
	s3 = boto3.client('s3')
	s3.upload_file('/tmp/' + new_filename, s3_bucket, new_s3_key)
