import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self):
        self.connection = None
        self.db_file = 'static/Database/control.db'

    def database_connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            return self.connection
        except Error as e:
            print e
        return None

    def create_table(self):
        cur = self.connection.cursor()
        cur.execute('''create table direction_control (arm_dir int, base_dir int)''')
        cur.execute('insert into direction_control values (0, 0)')
        dta = cur.execute('select * from direction_control')
        for row in dta:
            print row
        self.connection.commit()

    def update_direction(self, device, value):
        cur = self.connection.cursor()
        if device == 'arm':
            cur.execute('update direction_control set arm_dir = '+value)
        elif device == 'bot':
            cur.execute('update direction_control set base_dir = '+value)
        else:
            print 'Can not update the database'

    def get_direction_state(self):
        cur = self.connection.cursor()
        dta = cur.execute('select * from direction_control')
        for row in dta:
            print row
        return dta

    def close_connection(self):
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    db = Database()
    db.database_connect()
    db.get_direction_state()
    #db.create_table()
