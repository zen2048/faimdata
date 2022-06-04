#!/usr/bin/python
import sqlite3
from datetime import datetime

def getClinicName():
    conn = sqlite3.connect("faimdata.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM clinic")
    rows = cur.fetchall()
    conn.close()   
    return rows[0][0]

def searchProviders(pattern):
    conn = sqlite3.connect("faimdata.db")
    cur = conn.cursor()
    if pattern == "":
        pattern = " "
    pattern = "%" + pattern.replace(" ", "%") + "%"
    cur.execute("SELECT first_name, last_name FROM provider WHERE first_name || ' ' || last_name LIKE ?",  (pattern,))
    rows = cur.fetchall()
    #print(rows)
    conn.close()   
    return rows

def checkProviderAvailability(provider_first_name, provider_last_name, start_time, end_time):
    conn = sqlite3.connect("faimdata.db")
    #print(update_time)
    cur = conn.cursor()
    cur.execute("SELECT start_time, end_time FROM time_slot WHERE provider_first_name = ? AND provider_last_name = ? AND start_time >= ? AND end_time <= ? AND patient_first_name IS NULL AND patient_last_name IS NULL",  (provider_first_name, provider_last_name, start_time, end_time,))
    rows = cur.fetchall()
    conn.close()   
    return rows    

def bookAppointment(provider_first_name, provider_last_name, start_time, patient_first_name, patient_last_name, update_time):
    conn = sqlite3.connect("faimdata.db")
    #print(update_time)
    cur = conn.cursor()
    cur.execute("UPDATE time_slot SET patient_first_name = ? AND patient_last_name = ? WHERE provider_first_name = ? AND provider_last_name = ? AND start_time = ? AND update_time <= ?",  (patient_first_name, patient_last_name,provider_first_name, provider_last_name, start_time,  update_time,))
    conn.close()   
    return cur.rowcount    

def unbookAppointment(provider_first_name, provider_last_name, start_time, update_time):
    conn = sqlite3.connect("faimdata.db")
    #print(update_time)
    cur = conn.cursor()
    cur.execute("UPDATE time_slot SET patient_first_name = NULL AND patient_last_name = NULL WHERE provider_first_name = ? AND provider_last_name = ? AND start_time = ? AND update_time <= ?",  (provider_first_name, provider_last_name, start_time,  update_time,))
    conn.close()   
    return cur.rowcount  

if __name__ == "__main__":
    print(getClinicName())
    print(searchProviders(" "))
    print(searchProviders("i z"))

    print(checkProviderAvailability("一", "张", datetime(2022,6,1,7,14,00), datetime(2022,6,1,12,15,00)))
    print(checkProviderAvailability("Mike", "Zhao", datetime(2022,6,1,7,14,00), datetime(2022,6,1,12,15,00)))

    print(bookAppointment("Mike", "Zhao", datetime(2022,6,1,9,30,00), "四", "李", datetime.now()))
    print(checkProviderAvailability("Mike", "Zhao", datetime(2022,6,1,7,14,00), datetime(2022,6,1,12,15,00)))

    print(unbookAppointment("Mike", "Zhao", datetime(2022,6,1,9,30,00), datetime.now()))
    print(checkProviderAvailability("Mike", "Zhao", datetime(2022,6,1,7,14,00), datetime(2022,6,1,12,15,00)))


