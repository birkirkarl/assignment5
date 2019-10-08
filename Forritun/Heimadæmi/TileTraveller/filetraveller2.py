def safe_input(x,y):
    try:
        except:
        if y(x)==x:
    except ValueError:
        if int(x)==x:
            a_type=int
        elif float(x)==x:
            a_type=float
        else:
            a_type=str
    print("Error: please enter a value of ", a_type)

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))