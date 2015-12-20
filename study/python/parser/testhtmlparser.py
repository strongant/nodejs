from pyquery import PyQuery

doc = PyQuery(url='https://www.python.org/events/python-events/')

for event in doc('.list-recent-events li'):

    event = PyQuery(event)

    loc = event.find('.event-location').text()

    time = event.find('time').text()

    name = event.find('.event-title').text()

    print 'event:%s' % name

    print '\ttime:%s' % time

    print '\tlocation:%s' % loc
