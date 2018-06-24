#I just need a graphing import (matplotlib)
import matplotlib

def base(x):
	#this is just the actual equation x^2 for comparison
	return x*x
	
def get_next_val(h, x):
	return x +(h*(x*2))
	
def main():
	