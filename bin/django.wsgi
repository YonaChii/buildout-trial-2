#!/home/pc-0164/.virtualenvs/stage/bin/python


import sys
sys.path[0:0] = [
  '/home/pc-0164/trial/test/src/exam',
  '/home/pc-0164/trial/test/eggs/djangorecipe-1.7-py2.7.egg',
  '/home/pc-0164/.virtualenvs/stage/lib/python2.7/site-packages',
  '/home/pc-0164/trial/test/eggs/zc.recipe.egg-2.0.1-py2.7.egg',
  '/home/pc-0164/trial/test/eggs/zc.buildout-2.2.1-py2.7.egg',
  '/home/pc-0164/trial/test',
  '/home/pc-0164/trial/test/src',
  ]

import djangorecipe.wsgi

application = djangorecipe.wsgi.main('exams.settings', logfile='')
