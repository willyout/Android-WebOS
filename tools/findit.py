�   findit.py C:\Users\will\Desktop\findit.py    +   C:\Users\will\AppData\Local\Temp\findit.py �  #!/usr/bin/python
# -*- coding:utf-8 -*- 

"""
author: willandlily@gmail.com
"""

"""
Copyright (c) <2012> <willandlily@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""

import os
import re
import sys
import getopt

def grepinit(word):
	template = '''.*(temp)+\s+'''
	template = template.replace('temp', word)
	patt = re.compile(template, re.IGNORECASE)
	return patt

def testregex():
	wo = '-DANDROID'
	patt = grepinit(wo)
	if patt.match(r'COMMON_GLOBAL_CFLAGS:= -DANDROID '):
		print 'match1'
	if patt.match('ddd -DANDROID '):
		print 'match2'

def pygrep(filepath, word, patt, result):
	linen = 0
	fd = open(filepath, 'r')
	for line in fd:
		linen = linen + 1
		if (patt.match(line)):
			result[filepath] = linen
			print filepath, '@ line:', linen, '\n', line  
	fd.close()

def show(dicts):
	print  '#', len(dicts), '''results! you can check results in 'pyfind.txt' file''', '\n'
	with open('pyfind.txt', 'w') as f:
		for key in dicts:
			f.write(key + ' @ line: ' + str(dicts[key]) + '\n')  

def pyfind(directory, word, postfix):
	result = {}
	patt = grepinit(word)
	for root, dirs, files in os.walk(directory):
		for f in files:
			if postfix:
				#for p in postfix:
				if f.endswith(postfix):	
					filepath = os.path.join(root, f)  
					pygrep(filepath, word, patt, result)
					
	#show(result)

def usage():
	info="""

NAME: 
  fuck, find something in some files
	
USAGE:
  ./fuck -d "/home/bin" -p mk -w -DANDROID

Options and arguments: 
  -d,   the directory you want to search, default is script directory  
  -p,   files with postfix you want to search, default is mk
  -w,   the word you want to search, default is -DANDROID
	"""
	print info

def main():
	directory = os.getcwd()
	postfix = 'mk'
	word = '-DANDROID'
	dicts = {}
	
	dicts['-d'] = directory
	dicts['-p'] = postfix
	dicts['-w'] = word
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'd:p:w:')
		#print opts, '\n', args, '\n'
		for flag, argv in opts:
			#print flag, word
			dicts[flag] = argv
			"""
			Python doesn't support switch function.
			"""
		#print dicts
	except getopt.GetoptError:
		print 'args error \n'
		usage()
		sys.exit(2)
	
	print '\n------------------------Begin-----------------------------\n'
	pyfind(dicts['-d'], dicts['-w'], dicts['-p'])
	print '-------------------------End------------------------------'	
	
"""
def pyvol(file):
	files = open(file, 'r')
	if (files.read().find('-DANDROID') != -1):
		print file
	files