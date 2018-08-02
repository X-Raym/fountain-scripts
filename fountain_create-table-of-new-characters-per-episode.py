# Script: Export list of new characters per episode in markdown
# Author: X-Raym
# Author URI: https://www.extremraym.com
# License: GPL v3
# Version: 1.0
# Date: 2018-05-31

#### USER GLOBALS ####

out_file = 'NEW-CHARACTERS-PER-EPISODES.md' # Your output file
title = '# New Characters Per Episodes\n' # Your file header title

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
def getCharacters( content ):
    out = [] # Déclaration de liste
    characters = {} # Déclaration de dictionnaire
    for i, line in enumerate( content ):
        if re.match( '^([A-Z| ]+)$', line ): # Find sequence lines (start with a point)
            match = re.match( '^([A-Z| ]+)', line )
            if not match[0] in new_characters:
                characters[ match[0] ] = 0 # on s'en fiche de la valeur de cette clé.
                new_characters[ match[0] ] = 0

    for k, v in characters.items():
        out.append( k )

    return out

# Print and write
def printWrite( f, str ):
    f.write( str + '\n' )
    print( str )

#### RUN ####

new_characters = {}

# Set work directory
os.chdir( dir )

# Create output file
f = open( out_file, 'w+', encoding='UTF-8' )
printWrite( f, title ) # Add title

for file_name in glob.glob( '*.fountain' ): #Get list of .fountain files
    printWrite( f, '## ' + file_name[:-9] + '\n' ) # Write file title as "## Title"
    content = getFileContent( file_name ) # Get file content
    characters = getCharacters( content ) # Extract its characters list as array
    for i, character in enumerate( characters ): # For each characters
        printWrite( f, str(i+1) + '. ' + character ) # Write the characters to the file
    printWrite( f, '' ) # Add an extra break line to the file

# Close the file
f.close()
