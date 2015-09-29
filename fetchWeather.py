#!/usr/bin/env python
import datetime
import urllib2

def dateRange(startDate, endDate, step=datetime.timedelta(seconds=60)):
    """It's like range() only for dates"""
    startDate
    while startDate < endDate:
        yield startDate
        startDate = startDate + step

dates = dateRange(
    datetime.datetime(year=2006, month=7, day=12, hour=0, minute=0, second=0),
    datetime.datetime(year=2014, month=11, day=26, hour=0, minute=0, second=0),
    datetime.timedelta(seconds=60*60*24)
    )
for day in dates:
    print "Processing:", day
    url = ('http://www.wunderground.com/history/airport/KLRF/%(year)s/%(month)s/%(day)s/DailyHistory.html?format=1' %
           {'year': day.year,
            'month': day.month,
            'day': day.day
            }
           )
    outfile = open(('%(path)s%(year)s-%(month)s-%(day)s.csv' %
                   {'path': 'KLRF/',
                    'year': day.year,
                    'month': day.month,
                    'day': day.day
                    }
                   ),
                   'w'
                   )
    outdata = urllib2.urlopen(url).readlines()
    outdata = '\n'.join([x.replace('<br />', '').strip() for x in outdata][:-1])
    outfile.write(outdata)
    outfile.write('\n')
    outfile.close()
  
