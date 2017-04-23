# KeyStrokeLogger
Copyright (c) 2017, uzzal

All rights reserved.
Special thanks to  Aman Deep [https://github.com/hiamandeep], He is first owner of this, because I start writing this from his code.
I rewrite this code for my own use.  Feel free to rewrite and distribute maintaining GNU policy
A simple keylogger witten in python checking the platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key

Requirement:
python-xlib required. you can download and install it from
http://dl.fedoraproject.org/pub/epel/7/x86_64/p/

 OnKeyStrokeEvent is called everytime occurs a key event.
 Call a thread here to send shecdule mail at every 30 second
 After Initiate first threading , threading sleep 15 seconds
 
  96 is the ascii value of the grave key(`) we should use any value that is generally press by a ordinary user
  If you want to modify or reuse this code, chose this value wisely
 
 Email:
 """ If you want send mail using gmail then make change according to commected section bellow"""
 
 
  pyxhook -- an extension to emulate some of the PyHook library on linux.

    Copyright (C) 2008 Tim Alexander <dragonfyre13@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

    Thanks to Alex Badea <vamposdecampos@gmail.com> for writing the Record
    demo for the xlib libraries. It helped me immensely working with these
    in this library.

    Thanks to the python-xlib team. This wouldn't have been possible without
    your code.

    This requires:
    at least python-xlib 1.4
    xwindows must have the "record" extension present, and active.

    This file has now been somewhat extensively modified by
    Daniel Folkinshteyn <nanotube@users.sf.net>
    So if there are any bugs, they are probably my fault. :)
