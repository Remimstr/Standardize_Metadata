#!/usr/bin/env python

# Author: Remi Marchand
# Date: July 20, 2016
# Description: A wrapper to parse isolation_source information

import multilevel_parse

# Set default string processing to Unicode-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

keys = multilevel_parse.keys
# column_strs is a list of strings representing columns of interest
column_strs = ["isolation_source"]


def parse(isolation_source, iso_src_info):
    return multilevel_parse.parse(isolation_source, iso_src_info)
