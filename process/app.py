from time import sleep
from scraper import scraper, upsscraper

from sqlalchemy import create_engine

host = 'db'
host = '172.18.0.3'
db_string = "postgres://tracker_db:secret@{}:5432/tracker_db".format(host)
db = create_engine(db_string)
    
def get_trackers_from_db():
    query = "" + \
            "SELECT tracker_id, currier, last_update, last_location " + \
            "FROM tracked_packagess;"

    result_set = db.execute(query)
    for (tracker_id, currier, last_update, last_location) in result_set:  
        d = dict()
        d['currier'] = currier
        d['tracker_id'] = tracker_id
        return [d]


    

def update_tracker(tracker_id, timestamp, location):
    query = "" + \
            "SELECT last_update, last_location " + \
            "FROM tracked_packages " + \
            "WHERE tracker_id="+tracker_id+";"

    result_set = db.execute(query)
    previous_last_update = None
    previous_last_location = None
    for (last_update, last_location) in result_set:
        previous_last_update = last_update
        previous_last_location = last_location
    print(f'tracker_id: {tracker_id}')
    print(f'timestamp: {timestamp}')
    print(f'location: {location}')
    
    if previous_last_update != timestamp and \
        previous_last_location != location:
        print('Tracking updated. New location at {}, package is in {}'.format(timetamp, location))

    db.execute("UPDATE tracked_packages SET last_update = {}, last_location = {} WHERE tracker_id = {};".format(
            'TIMESTAMP ' + timestamp,
            location,
            tracker_id)
        )
    

if __name__ == '__main__':
    

    while True:
        trackers = get_trackers_from_db()

        for tracker in trackers:
            last_update = None
            if tracker['currier'] == 'ups':
                ups = upsscraper.UPSScraper()
                last_update = ups.scrape(tracker['tracker_id'])
                
            if last_update:
                update_tracker(tracker['tracker_id'], last_update['timestamp'], last_update['location'])

        sleep(10)