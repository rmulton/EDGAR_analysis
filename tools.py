# -*-coding:Latin-1 -*

'''
Module:     'tools'
Aim:        Provides some tools for the main program
Functions:  - year_quarter_list
'''

################################################################################

def year_quarter_list(from_year,from_quarter, to_year, to_quarter):
    '''
    Computes the list of quarter tuples for the required period.
    Output is as in the following example: [ (2014, 1), (2015, 2) ]
    '''
    output = []

    # computes the output for a single year required
    if from_year == to_year:

        output = [(from_year, quarter) for quarter in range(from_quarter, to_quarter+1)]

    # computes the output for several years required
    else:
        # the output is composed of the output for the first year, the last year
        # and the years between
        first_year = [(from_year,quarter) for quarter in range(from_quarter,5)]

        last_year = [(to_year,quarter) for quarter in range(1,to_quarter+1)]

        between_years = []
        for year in range(from_year+1, to_year):
            between_years += [(year, 1), (year, 2), (year, 3), (year,4)]

        output = first_year + between_years + last_year


    return(output)
