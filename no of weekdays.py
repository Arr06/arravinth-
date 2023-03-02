import numpy
yearmonth=input("enter the yearmonth:")
date=numpy.busday_offset(yearmonth,0,roll='forward',weekmask='Mon')
print("1st monday of the given month:",date)
date2=numpy.busday_count('2017-03','2017-04')
print("no.of weekdays:",date2)
