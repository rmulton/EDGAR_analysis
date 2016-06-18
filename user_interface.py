# -*-coding:Latin-1 -*

'''
Module:     'user_interface'
Aim:        Asks the user for input
Functions:  - ask_input
'''

################################################################################

def ask_inputs():

    # input the time period
    print('Please choose the period for which you want to analyse the data from SEC:')
    from_year = int( input('From year: ') )
    from_quarter = int( input('From quarter: ') )
    to_year = int( input('To year: ') )
    to_quarter = int( input('To quarter: ') )

    return(from_year,from_quarter, to_year, to_quarter)
