# Script: Export sequences of fountain files in a directory to a Table of Contents file in HTML
# Description: https://github.com/X-Raym/Fountain.js
# Author: X-Raym
# Author URI: https://www.extremraym.com
# License: GPL v3
# Version: 1.0
# Date: 2018-05-17

#### USER GLOBALS ####

out_file = 'TOC.html' # Your output file
title = '# Table of Contents\n' # Your file header title

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

#### FUNCTIONS ####

# Get file content
def getFileContent( pathAndFileName ):
    with open( pathAndFileName, 'r', encoding='UTF-8' ) as theFile: # Open file as UTF-8
        data = theFile.read().split('\n') # Return a array of lines string
        return data

# Get sequences list
def getSequences( content ):
    out = []
    for i, line in enumerate( content ):
        if re.match( '^\.(.+)', line ): # Find sequence lines (start with a point)
            matches = re.findall( '\.(.+) #(\d+)#', line ) # Find elements like ". Sequence title #1#"
            for j, match in enumerate( matches ):
                seq = match[0] # Reformat seq string to "Sequence title" format. Index will come from <ol> tag.
                out.append( seq )
    return out

# Print and write
def printWrite( f, str ):
    f.write( str + '\n' )
    print( str )

#### RUN ####

# Set work directory
os.chdir( dir )

# Create output file
f = open( out_file, 'w+', encoding='UTF-8' )

html_header = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{Title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="X-Raym's Foutain TOC.html Generator">

    <link href="../Fountain.js/app/css/normalize.css" rel="stylesheet">
    <link href="../Fountain.js/app/css/fountain-js.css" rel="stylesheet">
    <link href="../Fountain.js/app/css/style-custom.css" rel="stylesheet">
    <style>
    li a { color: #008000;}
    h3 a { color: #000000;}
  </style>
  </head>

  <body id="fountain-js">
    <section id="workspace" style="display:block;">
      <header class="toolbar">
        <div class="container">
          <ul id="inspector">
            <li></li>
          </ul>
          <p id="script-title">{Title}</p>
          <!--<ul id="toolbar">
            <li class="resize"><a data-tooltip="Resize Script">Resize Script</a></li>
            <li class="dim"><a data-tooltip="Toggle Theme">Toggle Theme</a></li>
            <li class="dock"><a data-tooltip="Full Width">Full Width</a></li>
          </ul>-->
        </div>
      </header>
      <div id="script" class="us-letter dpi100">
        <div class="page toc-page">
          <h2>Table des Matières</h2>
"""
html_header = html_header.replace("{Title}", os.path.basename(dir) + " - TOC")
printWrite( f, html_header ) # Write the sequence to the file

for file_name in glob.glob( '*.fountain' ): #Get list of .fountain files
    file_name_html = file_name.replace(".fountain", ".html")
    printWrite( f, '          <h3><a href="' + file_name_html + '">' + file_name[:-9] + '</a></h3>' ) # Write file title as "## Title"
    content = getFileContent( file_name ) # Get file content
    sequences = getSequences( content ) # Extract its sequences list as array
    printWrite( f, "          <ol>")
    for i, seq in enumerate( sequences ): # For each sequences
        printWrite( f, "            <li><a href='" + file_name_html + "#sequence-" + str(i + 1) + "'>" + seq + "</a></li>") # Write the sequence to the file
    printWrite( f, '          </ol>\n' ) # Add an extra break line to the file

html_footer = """
        </div>
      </div>
    </section>
  </body>
</html>
"""
printWrite( f, html_footer ) # Write the sequence to the file

# Close the file
f.close()
