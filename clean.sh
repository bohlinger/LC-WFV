# Source with more good tips:
# https://askubuntu.com/questions/589210/removing-files-older-than-7-days

#Explanation:
#find: the unix command for finding files/directories/links and etc.
#/path/to/: the directory to start your search in.
#-type f: only find files.
#-name '*.gz': list files that ends with .gz.
#-mtime +7: only consider the ones with modification time older than 7 days.
#-execdir ... \;: for each such result found, do the following command in ....
#rm -- '{}': remove the file; the {} part is where the find result gets substituted into from the previous part. -- means end of command parameters avoid prompting error for those files starting with hyphen.

find /lustre/storeA/project/fou/om/LC-WFV/ -type f -mtime +14 -name '*.grib2' -execdir rm -- '{}' \;
