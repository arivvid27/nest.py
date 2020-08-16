""" This is the "nest.py" module and it privides one function
called print_it() which prints lists that may or may not include nested lists."""

def print_it(the_list):
    for each_object in the_list:
        if isinstance(each_object, list):
            print_it(each_object)
        else:
            print(each_object)