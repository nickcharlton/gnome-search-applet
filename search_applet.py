#!/usr/bin/env python

# standardlib imports
import sys

# gtk
import gtk
import pygtk
import gnomeapplet

# project imports
pygtk.require('2.0')

def applet_factory(applet, iid):
    label = gtk.Label('It works!')
    applet.add(label)
    applet.show_all()
    print 'Factory started.'
    
    return True

if __name__ == '__main__':
    print 'Starting factory.'
    gnomeapplet.bonobo_factory('OAFIID:SearchApplet_Factory',
                                gnomeapplet.Applet.__gtype__,
                                'Sample Applet', '0.1',
                                applet_factory)

