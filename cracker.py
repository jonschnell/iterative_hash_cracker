'''
Created on 9/15/21

@author: Jonathon Schnell

@date: 9/15/21

@version: 1.0

'''
import argparse
import hashlib
import sys
import os.path
import base64
import crypt


if __name__ == "__main__":
	#argument parser
	parser = argparse.ArgumentParser()
	parser.add_argument("shadow", help="[shadow.txt] to be cracked")
	parser.add_argument("wordlist", help="[wordlist.txt] to use in cracking")


	args = parser.parse_args()
	
	shadow = args.shadow
	wordlist = args.wordlist
	
	
	#check to see if shadow can be opened
	def fileCheck(shadow):
		try:
			open(shadow, "r")
			return 1
		except IOError:
			sys.exit("Error: shadow file does not appear to exist.")
			
	#check to see if shadow can be opened
	def fileCheck(wordlist):
		try:
			open(wordlist, "r")
			return 1
		except IOError:
			sys.exit("Error: wordlsit file does not appear to exist.")
	

        #hashlib.sha1(string).hexdigest())
		
		
	#bruteforce searching.
	def bf(shadow, wordlist):
		sl = open(shadow, "r")
		
		#for each hash
		while 1:
			line = sl.readline()
			if not line :
				break;
			linep = line.split("$")
			salt = linep[2]
			chash = linep[3]
			uname = linep[0]
			
			#for each word
			wl = open(wordlist, "r")
			while 1:
				wline = wl.readline()
				passwd = wline.strip()
				algosalt = '$6$' + salt
				sha = crypt.crypt(passwd, algosalt)

				shaa = sha.split("$")
				chasha = chash.split(":")
				
				if shaa[3] == chasha[0]:
					print("gg--------------------------")
					print(uname + ' : ' + passwd)
					print("\n")
					break;

				if not wline :
					wl.close();
					break;
		sl.close()

	#call bruteforce function
	bf(shadow, wordlist)
		
