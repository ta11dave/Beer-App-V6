#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel_gui
import databases

def main(args):
	#load databases
	databases.load_all()
	eel_gui

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
