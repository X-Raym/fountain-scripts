# Script: Export sequences of fountain files in a directory to a Table of Contents file in markdown
# Author: X-Raym
# Author URI: https://www.extremraym.com
# License: GPL v3
# Version: 1.0
# Date: 2018-04-20

#### USER GLOBALS ####

dir = 'E:\\Alien 2347\\' # Your work directory
out_file = 'TOC.md' # Your output file
title = '# Table of Contents\n' # Your file header title

#### IMPORT ####

import re
import os
import glob

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
                seq = match[1] + '. ' + match[0] # Reformat seq string to "1. Sequence title" format
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
printWrite( f, title ) # Add title

for file_name in glob.glob( '*.fountain' ): #Get list of .fountain files
    printWrite( f, '## ' + file_name[:-9] + '\n' ) # Write file title as "## Title"
    content = getFileContent( file_name ) # Get file content
    sequences = getSequences( content ) # Extract its sequences list as array
    for i, seq in enumerate( sequences ): # For each sequences
        printWrite( f, seq ) # Write the sequence to the file
    printWrite( f, '' ) # Add an extra break line to the file

# Close the file
f.close()
