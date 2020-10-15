import time

import mysql.connector
from mysql.connector import errorcode
import private_config as private_cnf
import telepot


bot = telepot.Bot(private_cnf.telegram_bot_token) 
TABLE_NAME = 'counts'

# def checkTableExistance(cnx):
#     cursor = cnx.cursor()
#     try:
#         cursor.execute("CREATE TABLE {} ( counter INT DEFAULT 0;".format('homestead.'+TABLE_NAME))
#         print("Table {TABLE_NAME} created")
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     cursor.close()

# def get_hit_count(cnx):
#     cursor = cnx.cursor()
#     cursor.execute("SELECT max(counter) FROM {};".format(TABLE_NAME))
#     for (count) in cursor:
#         counter = int(count[0])
#     cursor.close()
    
#     cursor = cnx.cursor()
#     new_counter = counter + 1
#     cursor.execute("INSERT INTO {} ({}) VALUES ({});".format(TABLE_NAME, 'counter', new_counter))

#     cursor.close()
#     return counter


# @app.route('/')
# def hello():
#     # connect to database
#     cnx = mysql.connector.connect(user='homestead', 
#                                 password='secret',
#                                 host='mysql',
#                                 database='homestead')

#     checkTableExistance(cnx)
#     count = get_hit_count(cnx)

#     cnx.commit()
#     cnx.close()
#     return 'Hello World! I have been seen {} times.\n'.format(count)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: {}'.format(command))


if __name__ == '__main__':

    bot.message_loop(handle)
    print('I am listening...')

    while True:
        time.sleep(3)