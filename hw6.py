# -*- coding: utf-8 -*-

def drawBoard(rows,columns):
	#resulting character fild have be 2*rows-1
	for rc in range(1,rows*2):
		if rc%2 == 0:
			print('-'*(columns*2-1))
		else:
			for cc in range(1,columns*2):
				if cc%2 == 0:
					print('|',end="")
				else:
					print(" ",end="")
				if cc>=(columns*2-1):
					print("")

drawBoard(3,7)
                    
                
                

