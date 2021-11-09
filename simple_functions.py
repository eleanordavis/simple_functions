#Eleanor Davis - eleanor.davis@centre.edu - Lab 11: Intro to Functions

#defining a function to compute a ceiling of a number
    #with parameter of num
    #including a doc string
def find_ceiling(num):
    '''
    Computes:
        the ceiling of a number (next highest integer), unless that
        number is already an integer
    Parameters:
        num: [int or float] No interpretation, just a number
    Returns:
        ceiling: [int] the next highest int, unless the num is already an int
    '''
    #if the number is already an int, then the ceiling is that int
    if num == int(num):
        ceiling = num
        
    #if the number is not an int, calculate the ceiling
    else:
        ceiling = int(-1 * num // 1 * -1)

    #the return value is the ceiling calculated in the conditional statements
    return ceiling

#defining a function to compute a floor of a number
    #with parameter of num
    #including a doc string
def find_floor(num):
    '''
    Computes:
        the floor of a number (next smallest int), unless that number
        is already an int
    Parameters:
        num: [int or float] No interpretation, just a number
    Returns:
        floor: [int] next smallest int, unless that number
        is already an int
    '''
    #if the number is already an int, then the floor is that int
    if num == int(num):
        floor = num

    #if the number is not an int, calculate the floor
    else:
        floor = int(num // 1)

    #the return value is the floor calculated in the conditional statements
    return floor

#defining a function to compute a ceiling of a number
    #with parameter of r
    #including a doc string
def find_area_circle(r):
    '''
    Computes:
        the area of a circle
    Parameters:
        r: [int or float] the radius of the circle
    Returns:
        area: [int or float] the area of the circle with radius r
    '''
    #compute the are of the cirlce by taking r and using the area formula A = πr^2
    area = 3.14 * (r ** 2)

    #return value is the area calculated in the function
    return area
    
#defining a function to compute a ceiling of a number
    #with parameter of r
    #including a doc string
def find_vol_sphere(r):
    '''
    Computes:
        the volume of a sphere
    Parameters:
        r: [int or float] the radius of the sphere
    Returns:
        volume: [int or float] the volume of the sphere with radius r
    '''
    #compute the volume of the sphere by taking r and using the volume formula V=4/3πr^3
    volume = (4 / 3) * (3.14) * (r ** 3)

    #the return value is the volume calculated in the function
    return volume

#defining a function to compute a ceiling of a number
    #with parameters of l and w
    #including a doc string
def area_rect(l, w):
    '''
    Computes:
        the area of a rectangle
    Parameters:
        l: [int or float] the length of the rectangle
        w: [int or float] the width of the rectangle
    Returns:
        area: [int or float] the area of the rectangle given the
        length (l) and width (w) of the rectangle
    '''
    #compute the area of the rect by taking l and w and multiplying them together
    area = l * w

    #the return value will be the area calculated in the function
    return area

#defining a function to compute a ceiling of a number
    #with parameters of l, w, and h
    #including a doc string
def vol_box(l, w, h):
    '''
    Computes:
        the volume of a box
    Parameters:
        l: [int or float] the length of the box
        w: [int or float] the width of the box
        h: [int or float] the height of the box
    Returns:
        vol: [int or float] the volume of the box given then length (l),
        height (h), and width (w) of the box
    '''
    #compute the volume of the box by taking l, w, and h and multiplying them togehter
    vol = l * w * h

    #the return value will be the volume calculated in the function
    return vol

#defining a function to compute a ceiling of a number
    #with parameter of string
    #including a doc string
def censor(string):
    '''
    Computes:
        'censors' the given string
    Parameters:
        string: [str] the string which we want to censor
    Returns:
        new_string: [str] the new, cesnored string where every character
        except the first and last is replaced with an *
    '''
    #create an empty string
    new_string = ''

    #for each index in the range of the length of the parameter string
        #if it is the first index in the string
            #add the character of that index to the empty string
        #elif it is the last index in the string
            #add the character of that index to the empty string
        #else it is any other index in the string
            #add an * to the emtpy string
    for i in range(len(string)):
        if i == 0:
            new_string += string[0]
        elif i == len(string)- 1:
            new_string += string[len(string)-1]
        else:
            new_string += '*'

    #the return value is the new, censored string 
    return new_string
