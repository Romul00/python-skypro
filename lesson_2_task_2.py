years = [2000, 2025]
def is_year_leap(y):
    for y in range(years[0], years[-1]):
        if y % 4 == 0:
            print('год', y, True)
        else: print('год', y,False)
        
is_year_leap(1)