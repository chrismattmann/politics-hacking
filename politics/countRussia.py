#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Partial Credit: http://stackoverflow.com/questions/4371231/removing-punctuation-from-python-list-items
# for great suggestions on removing punc + empty strings

from tika import parser
from collections import Counter
import requests
import string
import sys, getopt

def parseUrl(url):
    parsed = parser.from_file(url)
    words = parsed["content"].lower().split() #lowercase everything                                                                                                
    finalWords = [''.join(c for c in s if c not in string.punctuation) for s in finalWords] # remove punc                                                          
    finalWords = [s for s in finalWords if s] # remove empty strings                                                                                               
    counts = Counter(finalWords)

    totalCount = 0
    for w in counts:
        if "russia" in w:
            totalCount += counts[w]

    print "Total mentions of Russia: "+str(totalCount)

def main(argv=None):
   url = ''
   usage = 'countRussia.py -u <url>'
   if argv is None:
       argv = sys.argv

   try:
      opts, args = getopt.getopt(argv,"hu:",["url="])
   except getopt.GetoptError:
      print usage
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print usage
         sys.exit()
      elif opt in ("-u", "--url"):
         url = arg

   if url != '':
      parseUrl(url)
   else:
      print usage
      sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])
