from calendar_source import CalendarSourceTemplate

class Cbtf(CalendarSourceTemplate):
    def extract_event_info(self, event, event_dictionary):
        event_dictionary['name'] = event['summary'][6:]

        event_dictionary['type'] = 'Exam/Quiz'
    
    def filter_event(self, event):
        return not 'Exam' in event['summary']

if __name__ == '__main__':
    my_cbtf_source = Cbtf('https://cbtf.engr.illinois.edu/sched/icalendar/4f8ea873-ffbd-4cb1-8eb1-ebc0781a0898', 'CBTF')
    print(my_cbtf_source.request())
