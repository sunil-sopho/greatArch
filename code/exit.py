import sys
"""
	Author : Sunil Kumar
	Description : for default fault tolerance

"""
def fault(msg,errorCode):
	sys.stderr.write(msg)
	sys.exit(errorCode)