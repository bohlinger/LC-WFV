#!/usr/bin/env python3
"""
needs: pysftp==0.2.8
bug in version 0.2.9
login for test if files are being pushed:
    lftp enmi_lcwfv@acquisition.ecmwf.int
    cd lcwfv_enmi
"""

import pysftp
import sys
import os
import numpy as np
sys.path.append(r'/home/patrikb/wavy/wavy')
from satmod import credentials_from_netrc

# obtain credentials
host = 'acquisition.ecmwf.int'
user, pw = credentials_from_netrc(host)
destination = 'lcwfv_enmi'

# obtain filename
path = '/lustre/storeA/project/fou/om/LC-WFV/'
filelst = np.sort(os.listdir(path))
filename = filelst[-1]
fullname = path + filename

print('transfer: ' + fullname)

with pysftp.Connection(host=host, username=user, password=pw) as sftp:
    sftp.cwd(destination)
    sftp.put(fullname)
