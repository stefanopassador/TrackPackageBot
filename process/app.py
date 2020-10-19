from time import sleep
from scraper import scraper, upsscraper

from sqlalchemy import create_engine

db_string = "postgres://tracker_db:secret@db:5432/tracker_db"
db = create_engine(db_string)
    
def get_trackers_from_db():
    d = dict()
    d['currier'] = 'ups'
    d['tracker_id'] = "1Z3746A36802537112%0D%0A"
    return [d]

def update_tracker(tracker_id, timestamp, location):
    # TODO: Save into db
    print(f'tracker_id: {tracker_id}')
    print(f'timestamp: {timestamp}')
    print(f'location: {location}')
    

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