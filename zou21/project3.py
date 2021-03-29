# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:27:32 2019

@author: ouzij
"""

import pandas
import matplotlib.pyplot as plt
fileref = open('SCDB_2019_01_justiceCentered_Citation.csv',
               encoding='ISO-8859-1')
scdb = pandas.read_csv(fileref)
f = plt.figure(figsize=(8,6))
scdb_subset = scdb[scdb.term >= 2000]
scdb_subset.groupby('term')['caseId'].nunique().plot(
        kind="bar")
plt.savefig('Q2.png')
scdb[scdb.term >= 2000].groupby(['justiceName', 'direction'])[
        'caseId'].nunique().plot(kind="bar")
f.tight_layout()
plt.savefig('Q3.png')

fileref1 = open('SCDB_2019_01_caseCentered_Citation.csv',
               encoding='ISO-8859-1')
scdb = pandas.read_csv(fileref1)
f = plt.figure(figsize=(8,6))
scdb_subset = scdb[scdb.term >= 2006]
scdb_subset.groupby('caseDisposition')['docketId'].nunique().plot(
        kind="bar")
plt.savefig('Q5.png')
scdb_subset.groupby('majVotes')['docketId'].nunique().plot(
        kind="bar") # majority of the votes go for the same side, it's not very divided which I think is interesting
plt.savefig('Q6.png')