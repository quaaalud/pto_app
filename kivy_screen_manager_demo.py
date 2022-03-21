#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:10:29 2022

@author: dale
"""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, BoundedNumericProperty

import aegis_db_reset as rset
from aegis_db_reset import db_name
import aegis_employee_class as emcl
import aegis_emp_db_update as adbu
 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
 
import time
import random

 
class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 5
        
        self.table = GridLayout()
        self.table.cols = 2
        dsply_tbl = get_pto_table_display()
        self.table.add_widget(Label(text=dsply_tbl)) 
        self.add_widget(self.table)
        
        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.rows = 2
        self.inside.add_widget(Label(text='Name of Rep:'))
        self.rep_name = TextInput(multiline=False)
        self.inside.add_widget(self.rep_name)
        self.inside.add_widget(Label(text='PTO hours used:'))
        self.pto_used = TextInput(multiline=False)
        
        self.inside.add_widget(self.pto_used)
        self.add_widget(self.inside)
        
        self.check_pto = Button(text='Check Current PTO Time', font_size=20)
        self.check_pto.bind(on_press=self.check_current_table)
        self.add_widget(self.check_pto)
        
        self.used_any = Button(text='Update PTO Used', font_size=20)
        self.used_any.bind(on_press=self.pressed_1)
        self.add_widget(self.used_any)
    
    def check_current_table(self, instance, **kwargs):
        rep_objs = adbu.sql_to_employee(adbu.check_db_table(db_name))        
        p = Popup(title='Current Data', **kwargs)
        for rep in rep_objs:
            rep_stats = str(rep.print_stats())
            p.content(Label(rep_stats))
        p.open()
                   
    
    def pressed_1(self, instance):
        rep_name = self.rep_name.text
        rep_name = rep_name.title()
        pto_used = self.pto_used.text
        pto_used = float(pto_used)
        rep_objs = adbu.sql_to_employee(adbu.check_db_table(db_name))
        for rep in rep_objs:
            if rep_name == rep.name:
                adbu.used_any_hrs(rep_name, hrs=pto_used)
                print(f'\n\n{rep.name}\'s PTO updated by {pto_used} hours\n\n')

        

def get_pto_table_display():
        reps = adbu.get_kivy_display(db_name)
        reps = reps.to_string()
        return reps
 
class ScreenManagerApp(App):
    def build(self):
        return MainScreen()
 
ScreenManagerApp().run()