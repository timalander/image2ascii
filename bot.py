#!/usr/bin/env python2

import requests #pip install requests
from i2a import convert
from StringIO import StringIO

r = requests.get('https://phaseoneimageprofessor.files.wordpress.com/2013/07/iqpw29_main_image_.jpg')
convert(StringIO(r.content), False, False, 1)
