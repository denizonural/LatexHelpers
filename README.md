# 1. bib_clear.py  -  Biblatex Cleanup

Remove unwanted fields from bibitems in a .bib file. Created because citation manager doesn't have enough .bib export options about which secondary fields in bibitems should be excluded. This script will remove unwanted fields. The fields can be edited in the file. 

Example use:
1. Copy bib_clear.py into the same folder as your target .bib file. Ideally, keep it in the folder where you export .bib files as a default from your citation manager.
2. Open terminal.
3. Run following, where **MYBIB.bib** is the filename for the .bib file you want to use it on.
   ```
   python bib_clear.py MYBIB
   ```
5. Your **MYBIB.bib** will be edited, and now bibitems don't contain any of the items listed as the fields_to_remove variable. The original bibfile is saved as a new file: **MYBIB_orig.bib**

   Default list is:
   ```
   fields_to_remove = ['abstract','url','isbn','local-url','copyright']
   ```
