# --*-- encoding:utf-8 --*--

import urllib2
import os

__doc__ ="""
This is a easy fm feel good inc audio file downloader.
written by universeroc
"""

root_url = 'http://mod.cri.cn/'
base_url = root_url + 'eng/ez/'
years = [2014]
months = [m + 1 for m in range(12)]
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def make_dir_if_not_exists(d):
	print 'checking ' + d + ' whether exists...\n'
	if os.path.exists(d):
		print d + ' exists.\n'
		return True
	else:
		os.mkdir(d)
		print 'make ' + d + '\n'

def remote_file_exists(url):
	try:
		h = urllib2.urlopen(url)
		return h.getcode() == 200
	except urllib2.HTTPError, err:
		return False

def download_file(url, file_name):
	try:
		h = urllib2.urlopen(url)
		file = open(file_name, 'wb')
		file.write(h.read())
		file.close()
		print 'finish ' + file_name + '.\n'
	except urllib2.HTTPError, err:
		pass


if __name__ == "__main__":
	make_dir_if_not_exists('fgi')
	for y in years:
		make_dir_if_not_exists('fgi/' + str(y))
		for m in months:
			dd = days[m]
			if is_leap_year(y) and m == 2:
				dd += 1

			for d in range(dd):
				file_name = 'fgi/' + str(y) + '/' + str(m).zfill(2) + str(d + 1).zfill(2) + 'fgi.mp3'
				url = base_url + file_name
				print 'working on ' + url
				if remote_file_exists(url):
					print 'remote file exists start downloading...\n'
					download_file(url, file_name)
				else:
					print 'bad remote file doest not exists!\n'