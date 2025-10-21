import sys
try: #try loop to exit if the argument in command line does not suit
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif (sys.argv[1]).endswith(".py")==False:
        sys.exit("Not a Python File")
    #Making sure the argument is well formated even if there is no error
    else:
        with open(sys.argv[1],'r') as f: #opening the file specified in commmand line argument
            N=0
            for line in f:
                line=line.strip() #avoiding spaces lines
                if line and line.startswith("#")==False: #avoiding lines that begin with # = comments
                    N+=1
        print(N)

except FileNotFoundError:
    sys.exit("Not a Python file")

except IndexError:
    sys.exit("Too few command-line arguments")
#managing errors exceptions
