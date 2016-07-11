#!/usr/bin/env python

import clr
clr.AddReferenceByPartialName('UnityEngine')
import UnityEngine

import sys
sys.path.append('C:/Python34/Lib')
sys.path.append('C:/Python34/Lib/site-packages')

import requests

def print_message():
    UnityEngine.Debug.Log('Test message from Python!')


print_message()