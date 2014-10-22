"""
	This is the file with your answer, and is located at ~/work/answer.py.
	Write your code in it, and save it before submitting your answer.
	"""
	
	class Window:
	    """Auxiliary class representing a window.
 Attributes:
	        x: An integer representing the X coordinate of the window's 
	            lower-left corner, in pixels.
	        y: An integer representing the Y coordinate of the window's 
	            lower-left corner, in pixels.
	        w: An integer representing the width of the window, in pixels.
	        h: An integer representing the height of the window, in pixels.
	    """
	    x=0
	    y=0
	    w=0
	    h=0
	    def __init__(self, window_string):
	        """Initialize window from a string of properties.
	
	        Args:
	            window_string: A string with the properties of the window, 
	                eg, 'X=10 Y=20 W=30 H=40'.
	        """
length=len(window_string)
	    value=[]
	
	    param=''
	        for x in range (0,length):
	        if window_string[x].isalpha():
	            param=window_string[x]
	
	        elif window_string[x].isdigit():
	            value.append(window_string[x])
	        
	        if (x==length-1) or (window_string[x] == " ") :
	            value_1 = (''.join(value))
	            if param == 'X' :
	                self.x=int(value_1)
	
	            elif param == 'Y':
	                self.y=int(value_1)
	
	            elif param == 'W':
	                self.w=int(value_1)
	
	            elif param == 'H':
	                self.h=int(value_1)
	
	            value=[]
def get_enclosing_rectangle(windows):
	    """Obtain the smallest window that encloses all the provided 
	    windows. This function declaration must be kept unmodified. 
	    
	    Args:
	        windows: A list of strings, each one representing a window, 
	            eg, ['X=10 Y=20 W=30 H=40', 'W=50 H=60 X=70 Y=80'].
	    Returns: 
	        A string representing the smallest window that encloses the 
	        provided windows.
	    """
	    # write your implementation here
 length = len(windows)
	    win=[]
	
	
	    for j in range(0,length):
	    inp = str(windows[j])
	    win.append(Window(inp))
	
	    min_val_x=win[0].x
	    for p in range(0,length):
	    min_val_x=min(win[p].x,min_val_x)
	    min_val_y=win[0].y
	    for p in range(0,length):
	    min_val_y=min(win[p].y,min_val_y)
	    max_val_h=win[0].h+win[0].y
	    for p in range(0,length):
	    max_val_h=max(win[p].h+win[p].y,max_val_h)
	    max_val_w=win[0].w+win[0].x
	    for p in range(0,length):
	    max_val_w=max(win[p].w+win[p].x,max_val_w)
	    max_val_w=max_val_w-min_val_x
	    max_val_h=max_val_h-min_val_y
	    ret= 'X='+str(min_val_x)+' '+'Y='+str(min_val_y)+' '+'W='+str(max_val_w)+' '+'H='+str(max_val_h)
	   
	    return ret
	
	# This tests your code with the examples given in the question, 
	# and is provided only for your convenience.
	if __name__ == '__main__':
	    for windows in [['X=5 Y=9 W=10 H=40', 'X=16 Y=9 W=10 H=40'],
	                       ['X=0 Y=0 W=1 H=5', 'X=0 Y=8 W=1 H=9']]:
        print get_enclosing_rectangle(windows)
