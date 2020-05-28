#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

mapping = {
			u'\u2000' : u' ',
			u'\u2001' : u' ',
			u'\u2002' : u' ',
			u'\u2003' : u' ',
			u'\u2004' : u' ',
			u'\u2005' : u' ',
			u'\u2006' : u' ',
			u'\u2007' : u' ',
			u'\u2008' : u' ',
			u'\u2009' : u' ',
			u'\u200A' : u' ',
			u'\u200B' : u' ',
			u'\u200C' : u'',
			u'\u200D' : u'',
			u'\u200E' : u' ', #LRM
			u'\u200F' : u' ', #RLM
			u'\u2010' : u'-',
			u'\u2011' : u'-',
			u'\u2012' : u'-',
			u'\u2013' : u'-',
			u'\u2014' : u'-',
			u'\u2015' : u'-',
			u'\u2016' : u'||',
			u'\u2017' : u'=',
			u'\u2018' : u'\'',
			u'\u2019' : u'\'',
			u'\u201A' : u',',
			u'\u201B' : u'\'',
			u'\u201C' : u'"',
			u'\u201D' : u'"',
			u'\u201E' : u'"',
			u'\u201F' : u'"',
			u'\u2020' : u'', #cross
			u'\u2021' : u'', #double cross
			u'\u2022' : u'', #bulletpoint
			u'\u2023' : u'', #bullet arrow
			u'\u2024' : u'.', #dot
			u'\u2025' : u'..', #dot dot
			u'\u2026' : u'...', #dot dot dot
			u'\u2027' : u'.',
			u'\u2028' : u' ',#LSEP
			u'\u2029' : u' ',#RSEP
			u'\u202A' : u' ',#LRE
			u'\u202B' : u' ',#RLE
			u'\u202C' : u' ',#PDF
			u'\u202D' : u' ',#LRO
			u'\u202E' : u' ',#RLO
			u'\u202F' : u' ',
			u'\u2030' : u'%',
			u'\u2031' : u'%',
			u'\u2032' : u'\'',
			u'\u2033' : u'"',
			u'\u2034' : u'"',
			u'\u2035' : u'\'',
			u'\u2036' : u'"',
			u'\u2037' : u'"',
			u'\u2038' : u'^',
			u'\u2039' : u'<',
			u'\u203A' : u'>',
			u'\u203B' : u'*',
			u'\u203C' : u'!!',
			u'\u203D' : u'?',
			u'\u203E' : u'-',
			u'\u203F' : u'',
			u'\u2040' : u'',
			u'\u2041' : u'',
			u'\u2042' : u'',
			u'\u2043' : u'-',
			u'\u2044' : u'/',
			u'\u2045' : u'[',
			u'\u2046' : u']',
			u'\u2047' : u'??',
			u'\u2048' : u'?!',
			u'\u2049' : u'!?',
			u'\u204A' : u'',
			u'\u204B' : u'',
			u'\u204C' : u'',
			u'\u204D' : u'',
			u'\u204E' : u'*',
			u'\u204F' : u';',
			u'\u2050' : u'',
			u'\u2051' : u'',
			u'\u2052' : u'%',
			u'\u2053' : u'~',
			u'\u2054' : u'',
			u'\u2055' : u'*',
			u'\u2056' : u'',
			u'\u2057' : u'"',
			u'\u2058' : u'',
			u'\u2059' : u'',
			u'\u205A' : u':',
			u'\u205B' : u'',
			u'\u205C' : u'',
			u'\u205D' : u'',
			u'\u205E' : u'',
			u'\u205F' : u' ',
			u'\u2060' : u' ',
			u'\u2061' : u' ',
			u'\u2062' : u' ',
			u'\u2063' : u',',
			u'\u2064' : u' ',
			u'\u2065' : u' ',
			u'\u2066' : u' ',
			u'\u2067' : u' ',
			u'\u2068' : u' ',
			u'\u2069' : u' ',
			u'\u206A' : u' ',
			u'\u206B' : u' ',
			u'\u206C' : u' ',
			u'\u206D' : u' ',
			u'\u206E' : u' ',
			u'\u206F' : u' ',
			# Strip trademark, copyright, and registered symbols
			u'\u00ae' : u'',
			u'\u2122' : u'',
			u'\u00a9' : u'',
		}

def normalize(text):
	if type(text) == list:
		return [ normalize(t) for t in text ]
	for unicodeChar in mapping:
		text = re.sub(unicodeChar, mapping[unicodeChar], text, re.UNICODE)

	text = re.sub(r'\xa0', u' ', text)
	return re.sub(r'\s+', u' ', text)# Remove multiple white space

