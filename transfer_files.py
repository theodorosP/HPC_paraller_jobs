import os

def tranfer(path):
	host = 'cobra'
	includes = ["file_1", "file_2"]
	options = '-av --exclude "transfer.py" --include "*/" ' 

	for include in includes:
		options += ' --include "' + include +'"'

	options += ' --exclude "*" '

	cmd = 'rsync ' + options + host + ':' + path + ' .'

	os.system( cmd )
	cmd = 'chmod g+rsx `find . -type d`'
	os.system(cmd)
	cmd = 'chmod g+r -R *'
	os.system(cmd)
