#!/usr/bin/python
import sqlite3

def dbPopulate():
    conn = sqlite3.connect('faimdata.db')

    conn.executescript(
        ''' 
        INSERT INTO clinic VALUES ("一个诊所");

        INSERT OR IGNORE INTO patient VALUES ("三", "张");        
        INSERT OR IGNORE INTO patient VALUES ("四", "李");        
        INSERT OR IGNORE INTO patient VALUES ("Tom", "Wang");        

        INSERT OR IGNORE INTO provider VALUES ("一", "张");        
        INSERT OR IGNORE INTO provider VALUES ("二", "李");        
        INSERT OR IGNORE INTO provider VALUES ("Mike", "Zhao");        

        INSERT OR IGNORE INTO time_slot VALUES ("一", "张", datetime("2022-06-01 08:15:00"), datetime("2022-06-01 08:30:00"), NULL, NULL, datetime("2022-06-01 08:15:00"));  
        INSERT OR IGNORE INTO time_slot VALUES ("一", "张", datetime("2022-06-01 08:30:00"), datetime("2022-06-01 08:45:00"), "Tom", "Wang", datetime("2022-06-01 08:15:00"));  
        INSERT OR IGNORE INTO time_slot VALUES ("一", "张", datetime("2022-06-01 09:30:00"), datetime("2022-06-01 09:45:00"), NULL, NULL, datetime("2022-06-01 08:15:00"));  

        INSERT OR IGNORE INTO time_slot VALUES ("Mike", "Zhao", datetime("2022-06-01 08:15:00"), datetime("2022-06-01 08:30:00"), NULL, NULL, datetime("2022-06-01 08:15:00"));  
        INSERT OR IGNORE INTO time_slot VALUES ("Mike", "Zhao", datetime("2022-06-01 08:30:00"), datetime("2022-06-01 08:45:00"), "四", "李", datetime("2022-06-01 08:15:00"));  
        INSERT OR IGNORE INTO time_slot VALUES ("Mike", "Zhao", datetime("2022-06-01 09:30:00"), datetime("2022-06-01 09:45:00"), NULL, NULL, datetime("2022-06-01 08:15:00"));  
        ''') 

    conn.close()


if __name__ == "__main__":
    dbPopulate()

    conn = sqlite3.connect('faimdata.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from time_slot;")
    print(cursor.fetchall())
    conn.close()