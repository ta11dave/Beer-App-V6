#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel_gui
import databases

def main(args):
	#load databases
	databases.update_data_on_load()
    eel_gui

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
