#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2013 Philip Schmiegelt
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import random
import os

import xbmcaddon
import xbmcgui
import xbmc

import controller, star


addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_path = addon.getAddonInfo('path')
image_dir = xbmc.translatePath( os.path.join( addon_path, 'resources', 'skins', 'default', 'media' ,'').encode("utf-8") ).decode("utf-8")

numberOfStars = 100

scriptId   = 'screensaver.starfield'



class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback, log_callback):
            self.exit_callback = exit_callback
	    self.log_callback = log_callback

        def onScreensaverDeactivated(self):
            #self.log_callback('sending exit_callback')
            self.exit_callback()
        def onAbortRequested(self):
	    #self.log_callback('abort requested')
	    self.exit_callback()


        
    
           

    def onInit(self):
	self.log("Screensaver starting")
	
	
        
        self.addon      = xbmcaddon.Addon(scriptId)
        
        
        self.centerX = self.getWidth() /2
        self.centerY = self.getHeight() /2
        #used to be sure that stars are really outside of the screen before they are deleted
        self.safeMargin = 100
        self.image_dir = xbmc.translatePath( os.path.join( addon_path, 'resources', 'skins', 'default', 'media' ,'').encode("utf-8") ).decode("utf-8")

        
#        if (self.addon.getSetting('setting_show_seconds') in ['false', 'False']):
#            self.showSeconds = False
#        else:
#	    self.showSeconds = True
#        self.redrawInterval = int(self.addon.getSetting('setting_redraw_interval'))
	self.monitor = self.ExitMonitor(self.exit, self.log)
	self.allStars = list()
        self.populateStars()
        
        #self.log(addon_path)

        self.cont = controller.Controller(self.log, self.drawStars)
        self.cont.start() 
        #self.showClock()
        
        
        
    def populateStars(self):
      for i in range(1, numberOfStars):
           self.star = star.Star(self.log, self)
           self.allStars.append(self.star)

    def drawStars(self):
        for star in self.allStars[:]:
          star.advance()
                
    

    def exit(self):
        self.log('Exit requested')
	self.cont.stop()
	del self.monitor
	del self.cont
	for star in self.allStars[:]:
	    star.removeControl()
        del self.allStars[:]
        self.close()
    
    def log(self, msg):
        xbmc.log(u'Starfield Screensaver: %s' % msg)

