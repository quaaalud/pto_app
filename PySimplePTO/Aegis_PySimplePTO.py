#!\Users\dluwinski\Anaconda3 python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:30:49 2022

@author: dludwinski
"""

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askfloat, askstring
import tkinter.messagebox as tkmb
import aegis_emp_db_update as ags_db
import aegis_db_reset as reset
from aegis_employee_class import *
from quitter import Quitter
import sqlalchemy
import sqlalchemy.sql.default_comparator
import sqlalchemy.engine.default
import sqlite3
import sqlalchemy.dialects.sqlite


class PtoApp(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Quitter(self).pack(fill=X, side=TOP, anchor=W)
        Button(self, text='Used 8 Hours',
               command=self.used_eight_hours).pack(side=BOTTOM, fill=X)
        Button(self, text='Used 4 Hours',
               command=self.used_four_hours).pack(side=BOTTOM, fill=X)
        Button(self, text='Get Table',
               command=self.get_pto_table).pack(side=BOTTOM, fill=X)
        Label(self,
              text='\n\nSELECT AN AGENT TO UPDATE PTO TIME MANUALLY\
\n\nOR CHOOSE AN OPTION BELOW:\n').pack(
                  side=TOP)
        self.repbuttons = RepButtons()
        self.repbuttons.pack(fill=Y, anchor=N)
        self.var = StringVar()
        
    def get_pto_table(event):
        reps = ags_db.get_display_table(reset.db_name)
        reps = ags_db.sql_to_employee(reps)
        r_data = [rep for rep in reps]
        tkmb.showinfo("Current PTO", r_data)

        
    def used_four_hours(self):
        var = askstring(self, 'Agent Name')
        if var == None:
            pass
        else:
            var = var.title()
            reps = ags_db.check_db_table(reset.db_name)
            rep_objs = ags_db.sql_to_employee(reps)
            for rep in rep_objs:
                if var == rep.name:
                    ags_db.used_four_hrs(rep.name)
                    tkmb.showinfo(f'{rep.name} UPDATED',
                                  f'{rep.name} used 4 PTO hours')

    def used_eight_hours(self):
        var = askstring(self, 'Agent Name')
        if var == None:
            pass
        else:
            var = var.title()
            reps = ags_db.check_db_table(reset.db_name)
            rep_objs = ags_db.sql_to_employee(reps)
            for rep in rep_objs:
                if var == rep.name:
                    ags_db.used_eight_hrs(rep.name)
                    tkmb.showinfo(f'{rep.name} UPDATED',
                                  f'{rep.name} used 8 PTO hours')
        
class RepButtons(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.var = StringVar()
        self.var.set(None)        
        pto_db = ags_db.check_db_table(reset.db_name)
        pto_db = pto_db[['Name', 'PTO Available']]
        pto_db.reset_index(inplace=True, drop=True)
        for name in pto_db['Name']:
            Radiobutton(self,
                        text=f'{name}:\n\
{(pto_db.loc[pto_db["Name"] == name])["PTO Available"].values} hours avaialable',
                        command=self.used_pto,
                        variable=self.var,
                        value=name).pack(fill=Y, side=TOP)
        self.used_pto
                        
    def used_pto(self):
        var = self.var.get()
        ent = askfloat(self, 'PTO HOURS USED')
        reps = ags_db.check_db_table(reset.db_name)
        rep_objs = ags_db.sql_to_employee(reps)
        for rep in rep_objs:
            if var == rep.name:
                ags_db.used_any_hrs(rep.name, hrs=ent)
                tkmb.showinfo(f'{rep.name} UPDATED',
                              f'{rep.name} PTO updated by {ent} hours')
        self.var.set(None)

      
if __name__ == '__main__':
    PtoApp().mainloop()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
