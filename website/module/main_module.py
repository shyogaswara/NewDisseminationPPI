#!/usr/bin/env python

'''Provides a way to get earthquake parameters from BMKG short messages
sourced from Geophysic Station of Padang Panjang (PPI), Gunung Sitoli 
(GSI), and Kepahiang (KSI).

deter_origin will be used to determine the origin of short messages
between PGRVI, KSI, GSI, or HQ. The origin usually located at the end 
of messages after :: separator.

param_split method will return a list of string from short messages that
splitted using comma as separator. The list that returned will be used
in deter_mag_n_ot method as well as _if_PPI_or_GSI and _if_KSI.

deter_mag_n_ot method will return Magnitude and Origin Time parameter
of earthquake from param_split return value.

_if_PPI_or_GSI and _if_KSI method will be used to determine the 
remaining earthquake parameters from PPI, GSI, or KSI short messages 
that determined from deter_origin method.'''

from datetime import datetime

__author__ = 'Shandy Yogaswara'
__copyright__ = 'Copyright 2022, No Name Yet Project'
__license__= 'MIT'
__version_info__ = (2022, 6, 'aN (Alpha Release)')
__version__ = ".".join(map(str, __version_info__))
__email__ = 'sh.yogaswara@gmail.com'
__status__ = 'Development'

def deter_origin(txt_str):

    txt_split = txt_str.split('::')
    msg_param = txt_split[0]
    msg_origin = txt_split[1]

    return msg_param, msg_origin

def _if_PPI_or_GSI(txt_str_or_msg_param):

    txt_split = param_split(txt_str_or_msg_param)

    eq_mag, eq_ot = deter_mag_n_ot(txt_split)
    
    eq_lat = (txt_split[2].split(':')[1]).split(' ')
    if eq_lat[1] in ['LS','ls','Ls','lS']:
        eq_lat = -1*float(eq_lat[0])
    else:
        eq_lat = float(eq_lat[0])

    lon_n_pos = txt_split[3].split(' ',2)
    if lon_n_pos[1] in ['BT','Bt','bT','bt']:
        eq_lon = float(lon_n_pos[0])
    else:
        eq_lon = -1*float(lon_n_pos[0])
    eq_pos = lon_n_pos[2][1:-1]

    eq_dep = float((txt_split[4].split(':')[1]).split(' ')[0])

    return eq_mag, eq_ot, eq_lat, eq_lon, eq_pos, eq_dep

def _if_KSI(txt_str_or_msg_param):

    txt_split = param_split(txt_str_or_msg_param)

    eq_mag, eq_ot = deter_mag_n_ot(txt_split)

    location = txt_split[2].split(' ',6)
    
    if location[2] in ['LS','ls','Ls','lS']:
        eq_lat = -1*float(location[1])
    else:
        eq_lat = float(location[1])
    
    if location[5] in ['BT','Bt','bT','bt']:
        eq_lon = float(location[4])
    else:
        eq_lon = -1*float(location[4])
    eq_pos = location[6][1:-1]

    eq_dep = float((txt_split[3].split(':')[1]).split(' ')[0])

    return eq_mag, eq_ot, eq_lat, eq_lon, eq_pos, eq_dep

def param_split(txt_str_or_msg_param):

    try :
        param, origin = deter_origin(txt_str_or_msg_param)
        txt_str = param
    except:
        txt_str = txt_str_or_msg_param
    finally:
        txt_split = txt_str.split(',')

    return txt_split

def deter_mag_n_ot(txt_str):
    '''
    This method will return Magnitude from parameter that splitted
    using param_split method
    '''
    txt_split = txt_str

    try:
        eq_mag = float((txt_split[0].split(':')[1]).split(' ')[0])
    except:
        eq_mag = float(txt_split[0].split(':')[1])

    eq_ot = datetime.strptime(
        txt_split[1][1:-4],
        '%d-%b-%y %H:%M:%S'
        )

    return eq_mag, eq_ot
