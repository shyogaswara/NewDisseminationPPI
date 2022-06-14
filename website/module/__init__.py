#!/usr/bin/env python

'''Provides a way to get earthquake parameters from BMKG short 
messages sourced from Geophysic Station of Padang Panjang (PPI),
Gunung Sitoli (GSI), and Kepahiang (KSI).'''

from .main_module import deter_origin, _if_PPI_or_GSI, _if_KSI

__author__ = 'Shandy Yogaswara'
__copyright__ = 'Copyright 2022, No Name Yet Project'
__license__= 'MIT'
__version_info__ = (2022, 6, 'aN (Alpha Release)')
__version__ = ".".join(map(str, __version_info__))
__email__ = 'sh.yogaswara@gmail.com'
__status__ = 'Development'


def _get_params(txt_str_or_short_msgs):

    _param, _origin = deter_origin(txt_str_or_short_msgs)

    if _origin == 'BMKG-PGR VI' or _origin == 'BMKG-GSI':
        _eq_params = _if_PPI_or_GSI(_param)
    elif _origin =='BMKG-KSI':
        _eq_params = _if_KSI(_param)

    return _eq_params