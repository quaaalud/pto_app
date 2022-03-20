# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:38:03 2022

@author: dludwinski
"""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import setuptools
import copy
import pickle
from distutils.core import setup
import py2exe

import importlib
import Aegis_PTO_APP
import aegis_emp_db_update
import aegis_db_reset
import aegis_employee_class
import quitter
import pandas
from sqlalchemy import *
import sqlalchemy.engine.default
import sqlite3
import sqlalchemy.dialects.sqlite


from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askfloat, askstring
import tkinter.messagebox as tkmb

setup(
    options = {'py2exe': {'bundle_files': 0, 'compressed': True}},
    windows=[{'script': 'Aegis_PTO_APP.py'}],
    zipfile = None,)