# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:06:06 2022

@author: dludwinski
"""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


import pandas as pd
import aegis_db_reset as reset
from sqlalchemy import create_engine
from aegis_employee_class import Employee


import sqlalchemy
import sqlite3
import sqlalchemy.dialects.sqlite


def check_db_table(db_name):   
    try:
        pto_db = pd.read_sql(f'{reset.db_name.upper()}',
                             reset.sqlite_connection)
    except:
        reset.aegis_db_create()
        print('\nA NEW DATABASE HAS BEEN CREATED\n')
        pto_db = pd.read_sql(f'{reset.db_name.upper()}',
                             reset.sqlite_connection)
    print(pto_db)
    return pto_db
 
def get_display_table(db_name):
    try:
        pto_db = pd.read_sql(f'{reset.db_name.upper()}',
                             reset.sqlite_connection)
    except:
        pass
    return pto_db

       
def sql_to_employee(df):
    from aegis_db_reset import aegis_db_reset
    from aegis_db_reset import create_full_table
    df = df.copy()
    data = []
    for row in df.values:
       data.append(row)
    employd = []
    for i in range(len(data)):
        emp = Employee(data[i][0], data[i][1], data[i][2],
                       data[i][3], (data[i][4]), data[i][5])
        emp.update_pto()
        employd.append(emp)
    aegis_db_reset(create_full_table(employd)) 
    return employd    

def used_four_hrs(emp_name):
    table = check_db_table(reset.db_name)
    table = sql_to_employee(table)
    for i in range(len(table)):
        emp = table[i]
        if emp.name == emp_name.title():
            emp.used_4hrs_pto()
            print(f'\n\n{emp.name} used 4.0 hours of PTO\n\n')
    new_df = reset.create_full_table(table)
    reset.aegis_db_reset(new_df)
    return table

def used_eight_hrs(emp_name):
    table = check_db_table(reset.db_name)
    table = sql_to_employee(table)
    for i in range(len(table)):
        emp = table[i]
        if emp.name == emp_name.title():
            emp.used_8hrs_pto()
            print(f'\n\n{emp.name} used 8.0 hours of PTO\n\n')
    new_df = reset.create_full_table(table)
    reset.aegis_db_reset(new_df)
    return table

def used_any_hrs(emp_name, hrs=float(0)):
    if hrs:
        table = check_db_table(reset.db_name)
        table = sql_to_employee(table)
        for i in range(len(table)):
            emp = table[i]
            if emp.name == emp_name.title():
                emp.used_pto(hrs)
                print(f'\n\n{emp.name} used {hrs} hours of PTO\n\n')
        new_df = reset.create_full_table(table)
        reset.aegis_db_reset(new_df)
        return table
    else:
        pass

if __name__ == '__main__':
    check_db_table(reset.db_name)
    used_any_hrs('mia', 0)
    check_db_table(reset.db_name)

    
    