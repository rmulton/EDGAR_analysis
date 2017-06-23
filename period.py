def period(from_period, to_period):
    period = []

    for quarter in range(from_period[1], 4+1):
        period.append({"quarter": quarter, "year": from_period[0]})

    if from_period[0]!=to_period[0]:

        for year in range(from_period[0]+1, to_period[0]+1-1):
            for quarter in range(1,4+1):
                period.append({"quarter": quarter, "year": year})
        
        for quarter in range(1, to_period[1]+1):
            period.append({"quarter": quarter, "year": to_period[0]})
        
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
    print(period((2014, 2), (2016, 1))==period_test)
    period_test = [
        {"year": 2015, "quarter": 1},
        {"year": 2015, "quarter": 2},
        {"year": 2015, "quarter": 3},
        {"year": 2015, "quarter": 4},
    ]
    print(period((2015,1), (2015,4))==period_test)
    period_test = [
        {"year": 2015, "quarter": 2},
        {"year": 2015, "quarter": 3},
        {"year": 2015, "quarter": 4},
    ]
    print(period((2015,2), (2015,4))==period_test)
