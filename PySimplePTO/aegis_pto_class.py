# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:54:37 2022

@author: dludwinski
"""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

class Employee(object):
    def __init__(self, name, pto=int(0), hrs_used=int(0),
                 lst_updt_day=None,
                 lst_updt_mnth=None,
                 lst_updt_yr=None):
        
        self.name = str(name)
        self.pto = float(pto)
        self.hrs_used = float(hrs_used)
        self.lst_updt_day = lst_updt_day
        self.lst_updt_mnth = lst_updt_mnth
        self.lst_updt_yr = lst_updt_yr
        
        import datetime as dt
        curr_date = dt.date.today()
        if self.lst_updt_day == None:
            self.lst_updt_day = curr_date.day
            self.lst_updt_mnth = curr_date.month
            self.lst_updt_yr = curr_date.year
            
        else:
            self.lst_updt_day = int(self.lst_updt_day)
            self.lst_updt_mnth = int(self.lst_updt_mnth)
            self.lst_updt_yr = int(self.lst_updt_yr)
        self.update_pto()
        
    def __str__(self):
        return f'\
Name => {self.name}\n\
PTO Available => {self.pto}\n\
PTO Used => {self.hrs_used}\n\
Last Updated => {self.lst_updt_mnth}/{self.lst_updt_day}\
\n\n\n'
               
    def update_pto(self):
        ernd_hrs = (1+(2/3))
        import datetime as dt
        curr_date = dt.date.today()
        
        if curr_date.year == self.lst_updt_yr:
            if curr_date.month == self.lst_updt_mnth:
                if self.lst_updt_day <= 15:
                    if curr_date.day > 15:
                        self.pto += ernd_hrs
                    else:
                        self.pto = self.pto
                else:
                    self.pto = self.pto
            else:
                self.pto += (
                    (curr_date.month-self.lst_updt_mnth)-1) * (ernd_hrs*2)
                if curr_date.day > 15:
                    self.pto += ernd_hrs*2 
                else:
                    self.pto += ernd_hrs
        else:
            self.pto += ((curr_date.year-self.lst_updt_yr)-1)*(ernd_hrs*24)
            self.pto += (12-self.lst_updt_mnth)*ernd_hrs*2
            self.pto += (curr_date.month-1)*ernd_hrs*2
            self.pto += ernd_hrs
            if curr_date.day > 15:
                self.pto += ernd_hrs
        self.pto = round(self.pto, 2)
        
        self.lst_updt_day = curr_date.day
        self.lst_updt_mnth = curr_date.month
        self.lst_updt_yr = curr_date.year
        
    def used_pto(self, hours_used=0):
        self.hrs_used += hours_used
        self.pto = self.pto - hours_used
        self.pto = round(self.pto, 2)
        self.create_employee_table()
        
    def used_4hrs_pto(self):
        self.hrs_used += 4
        self.pto = self.pto - 4
        self.pto = round(self.pto, 2)
        self.create_employee_table()
    
    def used_8hrs_pto(self):
        self.hrs_used += 8
        self.pto -= 8
        self.pto = round(self.pto, 2)
        self.create_employee_table()
        
            
        
    def print_stats(self):
        print(f'\n\
Name => {self.name}\n\
PTO Available => {self.pto}\n\
PTO Used => {self.hrs_used}\n\
Last Updated => {self.lst_updt_mnth}/{self.lst_updt_day}/{self.lst_updt_yr}\n'
)
        
    def create_employee_table(self):
        import pandas as pd
        import datetime as dt
        curr_date = dt.date.today()
        if curr_date.month != self.lst_updt_mnth:
            self.update_pto()
        emp_table = pd.DataFrame(
            {'Name': pd.Series(
                self.name, dtype='str'),
             'PTO Available': pd.Series(
                 self.pto, dtype='float'),
             'PTO Used': pd.Series(
                 self.hrs_used, dtype='float'),
             'Last Update Day': pd.Series(
                 self.lst_updt_day, dtype='float'),
             'Last Update Month': pd.Series(
                 self.lst_updt_mnth, dtype='float'),
             'Last Update Year': pd.Series(
                 self.lst_updt_yr, dtype='float')}
            )
        return emp_table
                


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        