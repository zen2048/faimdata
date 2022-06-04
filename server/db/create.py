#!/usr/bin/python
import sqlite3

def dbCreate():
    conn = sqlite3.connect('faimdata.db')

    conn.executescript(
        ''' CREATE TABLE IF NOT EXISTS clinic(
                name    TEXT    NOT NULL,
                CONSTRAINT PK_clinic PRIMARY KEY(name)
            );

            CREATE TRIGGER IF NOT EXISTS clinic_one_row
                BEFORE INSERT ON clinic
                WHEN (SELECT COUNT(*) FROM clinic) >= 1
                BEGIN
                    SELECT RAISE(FAIL, 'only one row!');
                END; 
            
            CREATE TABLE IF NOT EXISTS patient(
                first_name  TEXT    NOT NULL,
                last_name   TEXT    NOT NULL,
                CONSTRAINT PK_patient PRIMARY KEY(first_name, last_name)
            );
            
            CREATE TABLE IF NOT EXISTS provider(
                first_name  TEXT    NOT NULL,
                last_name   TEXT    NOT NULL,
                CONSTRAINT PK_provider PRIMARY KEY(first_name, last_name)
            );
            
            CREATE TABLE IF NOT EXISTS time_slot(
                provider_first_name TEXT    NOT NULL,
                provider_last_name  TEXT    NOT NULL,
                start_time          TEXT    NOT NULL,
                end_time            TEXT    NOT NULL,
                patient_first_name  TEXT,
                patient_last_name   TEXT,
                update_time         TEXT    NOT NULL,
                FOREIGN KEY(provider_first_name, provider_last_name) REFERENCES provider(first_name, last_name)
                FOREIGN KEY(patient_first_name, patient_last_name) REFERENCES patient(first_name, last_name)
                CONSTRAINT PK_time_slot PRIMARY KEY(provider_first_name, provider_last_name, start_time, end_time)
            );
        ''') 

    conn.close()


if __name__ == "__main__":
    dbCreate()

    conn = sqlite3.connect('faimdata.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' or type='trigger';")
    print(cursor.fetchall())
    conn.close()
