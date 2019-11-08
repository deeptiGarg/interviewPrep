dates = ['01 May 2018','10 Jan 2015','02 May 2014','11 June 2018','11 July 2018']

dict = {'Jan':1, 'Feb':2, 'Mar':3, 'April':4,'May':5, 'June':6, 'July':7,'Aug':8, 'Sep':9}

def sortDates(val):
    dateParts = val.split(' ')
    if dateParts[1] in dict:
        return dateParts[2], dict[dateParts[1]], dateParts[0]

#for d in dates:
sortedList = dates.sort(key = sortDates)
    #sortDates(d)
print(dates)

