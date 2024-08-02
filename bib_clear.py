
# for command line use to clear up unwanted bib fields. Update fields_to_remove to set what to remove.
# expected input is 1 argument, which is the filename of the bib file to clear up without the .bib extenstion.
#
# example
# -------
# file to be cleared: mybibs.bib
# run the following line:
# bib_clear.py mybibs
# will have two outputs: mybibs_orig.bib -- this is a copy of the input file before cleanup, mybibs.bib -- this is the cleared up version of the input file
#
# deniz 2024

import sys
import os
import shutil

src_filename_notype = sys.argv[1] # without.bib
src_filename = src_filename_notype + '.bib'
src_filename_copy = src_filename_notype + '_orig.bib'

shutil.copy(src_filename, src_filename_copy) # copy orig file
open(src_filename, 'w').close() # clear orig file

filename_in = src_filename_copy
filename2 = src_filename_notype + '_bibclearsub.bib'
filename_out = src_filename

# EDIT HERE TO CHANGE FIELDS TO REMOVE
fields_to_remove = ['abstract','url','isbn','local-url','copyright']

# Removes fields listed by going through the file for each item. This is a quick edit over single item version. Creates temp file and deletes it for each field item. Better way mioght be to do all at once.
n = len(fields_to_remove)
for idx, field in enumerate(fields_to_remove):

    start = field + ' = ' # change field as necessary
    end = '},'
    end2 = '}'
    item_start = '@'
    item_end = '}\n'

    if idx == 0:
        f_read =  filename_in
        f_write = filename2 # temp file
    else:
        f_read =  filename2
        f_write = filename_out

    flag = 0
    flag2 = 0
    with open(f_read) as infile, open(f_write, 'w') as outfile:
        for line in infile:
            if line.strip().startswith(start) == True:
                flag = 1
            elif flag == 1:
                if line.strip().endswith(end) == True or line.strip().endswith(end2) == True:
                    flag = 0
                    flag2 = 1
            elif flag2 == 1:
                if line.strip().startswith(item_start) == True:
                    outfile.write(item_end)
                    # outfile.write(line)
                flag2 = 0
                outfile.write(line)
            else: 
                outfile.write(line)
    if idx > 0:
        shutil.copy(filename_out, filename2)

if 0 == n-1:
    shutil.copy(filename2, filename_out)
os.remove(filename2)
