#!/usr/bin/env python

from NFTest import *

# specify interface configurations here
phy2loop0 = ('../connections/conn', [])

nftest_init([phy2loop0]) # pass list of interface configurations
nftest_start()

# test goes here

nftest_finish()
