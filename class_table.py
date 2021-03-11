import json
from icalendar import Calendar, Event
from datetime import date, datetime, time, timedelta, timezone
from uuid import uuid1

# load the json file from https://jw.ustc.edu.cn/ws/schedule-table/datum
file_name = 'datum.json'
class_info = json.load(open(file_name, 'r+'))
class_info = class_info['result']
print(class_info)

# id to Class name
id_name = dict()
for lesson in class_info['lessonList']:
    id_name[lesson['id']] = lesson['courseName']

cal = Calendar()
cal['version'] = '2.0'
cal['prodid'] = '-//CQUT//Syllabus//CN'  # *mandatory elements* where the prodid can be changed, see RFC 5445

for schedule in class_info['scheduleList']:
    # step1: create a new event
    evnt = Event()

    # step2: parser some value in schedule
    # class name
    evnt_name = id_name[schedule['lessonId']]

    # date
    ev_date = datetime.strptime(schedule['date'], '%Y-%m-%d')

    # start time
    start_hour = int(schedule['startTime'] / 100)
    start_min  = int(schedule['startTime'] % 100)
    ev_start_time = time(start_hour, start_min)
    ev_start = datetime.combine(ev_date, ev_start_time)

    # end time
    end_hour = int(schedule['endTime'] / 100)
    end_min  = int(schedule['endTime'] % 100)
    ev_end_time = time(end_hour, end_min)
    ev_end = datetime.combine(ev_date, ev_end_time)

    # location
    ev_location = schedule['room']['nameZh']

    # step3: add events
    evnt.add('uid', str(uuid1()) + '@CQUT')
    evnt.add('summary', evnt_name)
    evnt.add('dtstamp', datetime.now())
    evnt.add('dtstart', ev_start)
    evnt.add('dtend', ev_end)
    evnt.add('location', ev_location)

    cal.add_component(evnt)

# step4: export calular
with open('output.ics', 'w+', encoding='utf-8') as file:
    file.write(cal.to_ical().decode('utf-8'.replace('\r\n', '\n').strip()))
