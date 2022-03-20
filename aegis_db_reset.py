# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:24:24 2022

@author: dludwinski
"""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


import pandas as pd
from aegis_employee_class import Employee
from sqlalchemy import create_engine

import sqlalchemy.dialects.sqlite
import sqlalchemy
import sqlite3

db_name = 'pto_table'

engine = create_engine(f'sqlite:///{db_name}.db',
                       echo=False, connect_args={'check_same_thread': False})
sqlite_connection = engine.connect()

mia = Employee('Mia', pto=19.47, hrs_used=0,
                lst_updt_day=3,
                lst_updt_mnth=3,
                lst_updt_yr=2022)

nikki = Employee('Nikki', pto=22.53, hrs_used=0,
                lst_updt_day=3,
                lst_updt_mnth=3,
                lst_updt_yr=2022)

christine = Employee('Christine', pto=41.65, hrs_used=0,
                lst_updt_day=3,
                lst_updt_mnth=3,
                lst_updt_yr=2022)

matt = Employee('Matt', pto=38.15, hrs_used=0,
                lst_updt_day=3,
                lst_updt_mnth=3,
                lst_updt_yr=2022)

employee_list = [mia, nikki, christine, matt]

def create_full_table(employee_list):
    table_lst = []
    for name in employee_list:
        table_lst.append(name.create_employee_table())
    temp_db = pd.concat(table_lst, axis=0, ignore_index=True)
    return temp_db

def aegis_db_create():
    new_db = create_full_table(employee_list)    
    new_db.to_sql(f'{db_name.upper()}',
                                            con=sqlite_connection,
                                            if_exists='fail', index=False)
    return new_db

def aegis_db_reset(database_df):    
    database_df.to_sql(f'{db_name.upper()}', con=sqlite_connection,
                     if_exists='replace', index=False)
    
if __name__ == '__main__':
    try:
        aegis_db_create()
        print('\nMANUAL RESET OF THE DATABASE HAS BEEN COMPLETED\n')
    except ValueError:
        inpt = input('Do you really want to reset the DB?\n\n')
        inpt = inpt.lower()
        if inpt == 'yes':
            aegis_db_reset(create_full_table(employee_list))
            print('\nMANUAL RESET OF THE DATABASE HAS BEEN COMPLETED\n')



    

