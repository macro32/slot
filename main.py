#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 john@johnratcliffe.com
#  

import subprocess

import argparse

import logging


# logger stuff
logger = logging.getLogger('slot')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('slot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


parser = argparse.ArgumentParser(description='A Silly LOTtery program. A win every time!', prog='slot')

parser.add_argument('-f', '--filename', default='history.cvs',
                    help='lottery history file in CSV format')

parser.add_argument('-d', '--database', 
                    help='Database name',
                    default='slot.db')


args = parser.parse_args()


# set up operational parameters
def init():
	# check program args
	# extract args and create processing classes
	# set up logging
	# set up database
	pass
	
# process the history file
def process():
	pass
		
# clean up
def cleanup():
	# remove temporary files
	# write summary/statistics
	pass

def main(args):
    print( "slot: silly lottery program" )
    print( "processing...." )
    
    init()
    process()
#    cleanup()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
