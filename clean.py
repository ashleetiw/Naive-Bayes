#!/usr/bin/env python
import math
import re

# 5|23191|WHAT AN AWESOME MOVIE!! The best i've seen in a while. Dennis Quaid shows real talent in this movie.

t="WHAT AN AWESOME MOVIE!! The best i've seen in a while. Dennis Quaid shows real talent in this movie."
t=list(t)
t=[x.lower() for x in t]   # remove captilization
t=''.join(t)

t=re.sub(r'[^\w\s]','',t)# remove punctuations


stopwords=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each',
 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 
'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why',
 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 
 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

t=t.split(' ')
t=[x for x in t if x not in stopwords]

print(t)

# result after preprocessing
# ['awesome', 'movie', 'best', 'ive', 'seen', 'dennis', 'quaid', 'shows', 'real', 'talent', 'movie']

