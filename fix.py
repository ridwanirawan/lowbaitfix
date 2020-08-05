import os
while True:                                                                    
	b = os.path.isdir("$HOME/lowbait")
        if b == True:
		os.system("cd $HOME;rm -rf lowbait;git clone https://github.com/ridwanirawan/lowbait")
                print ("lowbait has fixed, thanks")
		break
	else:
		os.system("git clone https://github.com/ridwanirawan/lowbait")
		print ("lowbait has fixed")
		break
