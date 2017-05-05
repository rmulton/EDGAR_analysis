def period(starting_year, starting_quarter, ending_year, ending_quarter):
    period = []

    for quarter in range(starting_quarter, 4+1):
        period.append({"quarter": quarter, "year": starting_year})
    
    for year in range(starting_year+1, ending_year+1-1):
        for quarter in range(1,4+1):
            period.append({"quarter": quarter, "year": year})
    
    for quarter in range(1, ending_quarter+1):
        period.append({"quarter": quarter, "year": ending_year})
    
    return period

if __name__ == "__main__":
    period_test = [
        {"year": 2014, "quarter": 2},
        {"year": 2014, "quarter": 3},
        {"year": 2014, "quarter": 4},
        {"year": 2015, "quarter": 1},
        {"year": 2015, "quarter": 2},
        {"year": 2015, "quarter": 3},
        {"year": 2015, "quarter": 4},
        {"year": 2016, "quarter": 1},
    ]
    print(period(2014, 2, 2016, 1)==period_test)