# Script: Create a HTML file for each fountain in a subfolder, for usage with X-Raym Fountain to HTML with Dialog Analyses webapp
# Description: https://github.com/X-Raym/Fountain.js
# Author: X-Raym
# Author URI: https://www.extremraym.com
# License: GPL v3
# Version: 1.0
# Date: 2018-05-17

#### IMPORT ####

import re
import os
import glob
import sys
import os

#### INIT ####

if __name__ == "__main__": # When the script is run
	if len( sys.argv ) == 1: # Check if it was run with an argument
		dir = input("Folder?\t") # If no, ask for user input
	else:
		dir = sys.argv[1] # Take first argument of the command

if os.path.isdir( dir ) == False: # Does the folder exists?
	sys.exit("Folder doesn't exist.") # then kill the script

#### GLOBAL####

html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Responsive Fountain Screenplay with Dialog Analyses by X-Raym</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Fountain.js is a JavaScript parser for the screenplay format Fountain.">
    <meta name="author" content="X-Raym">

    <link href="../Fountain.js/app/css/normalize.css" rel="stylesheet">
    <link href="../Fountain.js/app/css/fountain-js.css" rel="stylesheet">
    <link href="../Fountain.js/app/css/style-custom.css" rel="stylesheet">
  </head>

  <body id="fountain-js">

    <script type="text/javascript" src="../Fountain.js/app/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="../Fountain.js/app/js/jquery.smoothscroll.min.js"></script>
    <script type="text/javascript" src="../Fountain.js/app/js/fountain.min.js"></script>
    <script type="text/javascript" src="../Fountain.js/app/js/highcharts.js"></script>
    <script type="text/javascript" src="../Fountain.js/app/js/xrange.js"></script>
    <script type="text/javascript" src="../Fountain.js/app/js/init.js"></script>
  </body>
</html>
"""

#### RUN ####

# Set work directory
os.chdir( dir )

# Create output files
for file_name in glob.glob( '*.fountain' ): #Get list of .fountain files
	f = open( file_name[:-9] + '.html', 'w+', encoding='UTF-8' )
	f.write( html ) # Write file title as "## Title"
	print( file_name + " => " + file_name[:-9] + '.html' )
	f.close()
