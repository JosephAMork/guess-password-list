import argparse
import string
from random import *
print()
print ("  Geuss any Password with   joguess.py  version 1.0  ") 
print ("                                "    )
print("                                            ")

print ("    *   * ")
print ("   *** ***    *")
print ("  ***** ***  ***")
print (" ******* ********")
print ("******************")
print()
print("by:joseph A Marcus")
print("Youtube: ")
print("github: ")
print()
print()
print("Usage: joguess.py  -option  [ path in current folder ] ")
print("example : ")
print("joguess.py --word=alex --n=9999")
print("joguess.py --word=alex ")
print()
print("--n             default 1M word")
print("--word          you can help with guess word about target   ")
print()
print()
print()
print("                                      ~/.   Good Luke                                     ")


# guess letters and digits and symbols + word given
def guess_general_word(word,number):
	num=number
	f1=open("joguessList.txt","+w")
	for _ in range(num):
		charjo=string.ascii_letters + string.digits + string.punctuation
		n=16-len(word)
		
		passjo="".join(choice(charjo) for v in range(randint(0,n)))
		print(choice([(word+passjo)]))
		f1.write(choice([(word+passjo+'\n')]))
		




if __name__=="__main__":
	parser=argparse.ArgumentParser(description="guess any password ")
	parser.add_argument('--word',action="store",dest="word",default="root")
	parser.add_argument('--n',action="store",dest="n",type=int,default=1000000)
	given_args=parser.parse_args()
	word=given_args.word
	n=given_args.n
	guess_general_word(word,n)

