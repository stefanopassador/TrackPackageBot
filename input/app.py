import time
import private_config as private_cnf

from sqlalchemy import create_engine
import telepot

bot = telepot.Bot(private_cnf.telegram_bot_token) 

db_string = "postgres://tracker_db:secret@db:5432/tracker_db"
db = create_engine(db_string)
TABLE_NAME = 'telegram_message_received'

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: {}'.format(command))

    db.execute("INSERT INTO telegram_message_received ("+\
            "message_id,"+\
            "from_id,"+\
            "from_is_bot,"+\
            "from_first_name,"+\
            "from_last_name,"+\
            "from_username,"+\
            "from_language_code,"+\
            "chat_id,"+\
            "chat_first_name,"+\
            "chat_last_name,"+\
            "chat_username,"+\
            "chat_type,"+\
            "date,"+\
            "text)"+\
        "VALUES ("+\
            str(msg['message_id']) + "," + \
            str(msg['from']['id']) + "," + \
            str(msg['from']['is_bot']) + "," + \
            "'" + str(msg['from']['first_name']) + "'" + "," + \
            "'" + str(msg['from']['last_name']) + "'" + "," + \
            "'" + str(msg['from']['username']) + "'" + "," + \
            "'" + str(msg['from']['language_code']) + "'" + "," + \
            str(msg['chat']['id']) + "," + \
            "'" + str(msg['chat']['first_name']) + "'" + "," + \
            "'" + str(msg['chat']['last_name']) + "'" + "," + \
            "'" + str(msg['chat']['username']) + "'" + "," + \
            "'" + str(msg['chat']['type']) + "'" + "," + \
            str(msg['date']) + "," + \
            "'" + str(msg['text']) + "'" + ");")


    

if __name__ == '__main__':

    bot.message_loop(handle)
    print('I am listening...')
    while True:
        time.sleep(3)


