def abbreviate_full_name(name):
	#    name=raw_input("")
	    list_name=list(name)
	    length=len(list_name)
	    i=length-1
	    while(list_name[i]!= " "):
	        i=i-1
	    count=i
	    i=i+1
	  last_list=[]
 for x in range(i, length):
	        last_list.append(list_name[x])
	    last_name=''.join(last_list)
	    i=0
	    ab_name=[]
	    for x in range(i, count):
	        if x==0:
	            ab_name.append(list_name[x])
	        elif list_name[x]==" ": 
	            ab_name.append(list_name[x+1])
	    ab=". ".join(ab_name)
	    return ab + '. '+last_name
if __name__=='__main__':
	    for name in ['John Smith','Anna Maria Simpson','Bob Alan Faria Stewart']:
	        print abbreviate_full_name(name)
