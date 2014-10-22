"""
	This is the file with your answer, and is located at ~/work/answer.py.
	Write your code in it, and save it before submitting your answer.
	"""
	
	def is_valid_socket_address(socket_address):
	    """Determine if the provided string is a valid socket address.
	    This function declaration must be kept unmodified.
	
	    Args:
	        socket_address: A string with a socket address, eg, 
	            '127.12.23.43:5000', to be checked for validity.
	    Returns:
	        A boolean indicating whether the provided string is a valid 
	        socket address.
	    """
	    # write your implementation here
 list_name=socket_address
	    length=len(list_name)
	    i=length-1
	    while(list_name[i]!=":"):
	    i=i-1
	    count=i
	    i=i+1
	    last_list=[]
	    
	    for x in range(i,length):
	        last_list.append(list_name[x])
	    last_name=''.join(last_list)
	    if (int(last_name)>65535) or (last_name.isalpha()):
	        return False
	    i=0
	    ab_name=[]
	    for x in range(i,count+1):
	        if (list_name[x]!= ".") and (list_name[x]!=":"):
	            ab_name.append(list_name[x])
	            print ab_name
	        else:
	            if ((''.join(ab_name)).isalpha()) or (int(''.join(ab_name))>255):
	                return False
	            ab_name=[]
	    return True
# This tests your code with the examples given in the question, 
	# and is provided only for your convenience.
	if __name__ == '__main__':
	    for socket_address in ["127.12.23.43:5000",
	                   "127.A:-12"]:
	        print is_valid_socket_address(socket_address)
