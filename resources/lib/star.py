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

maxCenterMult = 50
maxSize = 4
Vmax = 1.4
Vmin = 0.5


maxGrowth = 1.005;

class Star():
  
    def __init__(self, log_callback, gui):
      self.log_callback = log_callback
      self.gui = gui   
      
      self.reset()
      
      self.x = self.gui.centerX + random.randint(1, 400)*self.vx
      self.y = self.gui.centerY + random.randint(1, 400)*self.vy
      
      self.image = xbmcgui.ControlImage(int(self.x),int(self.y),int(self.size),int(self.size), gui.image_dir+'star.png', 0)
      #self.image.setColorDiffuse('0x' + self.brightness + ' FFFFFFF')
      self.image.setVisible(True)
      #self.allImages.append(image)
      gui.addControl(self.image)
      
    def reset(self):
      self.size = random.randint(1, maxSize)
      
      self.v = (((random.random() * (Vmax-Vmin))+Vmin))
      
      
      self.fractionX = random.random()
      
      self.vx = self.v*self.fractionX
      self.vy = self.v*(1-self.fractionX)
      
      self.sign1 = random.random()
      if (self.sign1 > 0.5):
	self.vx = self.vx * (-1)
      self.sign2 = random.random()
      if (self.sign2 > 0.5):
	self.vy = self.vy * (-1)
      
      self.growth = (random.random() * (maxGrowth-1))+1

      self.x = self.gui.centerX + random.randint(10, maxCenterMult)*self.vx
      self.y = self.gui.centerY + random.randint(10, maxCenterMult)*self.vy
      
      self.brightness = '4'
      
    def removeControl(self):
        self.gui.removeControl(self.image)
        
        
      
    def advance(self):
        if (self.x < 0 - self.gui.safeMargin or self.y < 0-self.gui.safeMargin or self.x > self.gui.getWidth() + self.gui.safeMargin or self.y > self.gui.getHeight() + self.gui.safeMargin):
	  self.reset()
	else:
          self.x = self.x + self.vx
          self.y = self.y + self.vy
          self.image.setPosition(int(self.x), int(self.y))
          
          self.size = float(self.size * self.growth)
          self.image.setWidth(int(self.size))
          self.image.setHeight(int(self.size))
          
          self.vx = self.vx*self.growth*1.01
          self.vy = self.vy*self.growth*1.01
          oldBrightness = self.brightness
          if (self.size < 1.4):
	    self.brightness = '4'
	  elif (self.size < 1.6):
	    self.brightness = '5'
	  elif (self.size < 1.8):
	    self.brightness = '6'
	  elif (self.size < 2.0):
	    self.brightness = '7'
	  elif (self.size < 2.2):
	    self.brightness = '8'
          elif (self.size < 2.4):
	    self.brightness = '9'
	  elif (self.size < 2.6):
	    self.brightness = 'A'
	  elif (self.size < 3.0):
	    self.brightness = 'B'
	  elif (self.size < 3.4):
	    self.brightness = 'C'
	  elif (self.size < 3.8):
	    self.brightness = 'D'
	  elif (self.size < 4.5):
	    self.brightness = 'E'
	  else:
	    self.brightness = 'F'
	    
	  if (self.brightness != oldBrightness):
	    self.image.setColorDiffuse('0x' + self.brightness + 'FFFFFFF')
