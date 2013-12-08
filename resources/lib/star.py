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



import xbmc
import xbmcgui
import random

maxCenterDistance = 5
maxSize = 4;
VmaxX = 5
VmaxY = 5

class Star():
  
    def __init__(self, log_callback, gui):
      self.log_callback = log_callback
      self.gui = gui   
      
      self.reset()
      
      self.image = xbmcgui.ControlImage(int(self.x),int(self.y),self.size,self.size, gui.image_dir+'star.png', 0)
      self.image.setVisible(True)
      #self.allImages.append(image)
      gui.addControl(self.image)
      
    def reset(self):
      self.size = random.randint(1, maxSize)
      
      self.vx = (random.random() - 0.5) * 2*VmaxX
      self.vy = (random.random() - 0.5) * 2*VmaxY
      

      self.x = self.gui.centerX + self.vx
      self.y = self.gui.centerY + self.vy
      
    def removeControl(self):
        self.gui.removeControl(self.image)
        
        
      
    def advance(self):
        if (self.x < 0 - self.gui.safeMargin or self.y < 0-self.gui.safeMargin or self.x > self.gui.getWidth() + self.gui.safeMargin or self.y > self.gui.getHeight() + self.gui.safeMargin):
	  self.reset()
	else:
          self.x = self.x + self.vx
          self.y = self.y + self.vy
          self.image.setPosition(int(self.x), int(self.y))
