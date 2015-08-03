#!/usr/bin/env python2

import pygtk,gtk
pygtk.require('2.0')
from blinkstick import blinkstick

class ledcube_dialog:

    def __init__(self):
        self.cube = blinkstick.find_first()
        self.drawingarea = gtk.DrawingArea()
        self.color = self.drawingarea.get_colormap().alloc_color(0, 255, 0)
        self.colorseldlg = gtk.ColorSelectionDialog("Select Cube Color")
        colorsel = self.colorseldlg.colorsel
        colorsel.set_previous_color(self.color)
        colorsel.set_current_color(self.color)
        colorsel.set_has_palette(True)
        colorsel.set_has_opacity_control(True)
        colorsel.connect("color_changed", self.update_cubecolor)
        colorsel.connect("delete_event", self.bye)
        self.colorseldlg.run()
        self.bye()

    def bye(self, widget=False, event=False):
        try:
			gtk.main_quit()
        except RuntimeError:
			quit()
        return True

    def update_cubecolor(self, widget):
        color = self.colorseldlg.colorsel.get_current_color()
        alpha = self.colorseldlg.colorsel.get_current_alpha()
        led_dim=self.range_convert(alpha)
        led_red=self.range_convert(color.red)
        led_green=self.range_convert(color.green)
        led_blue=self.range_convert(color.blue)
        self.cube.set_max_rgb_value(led_dim)
        self.cube.set_color(red=led_red,green=led_green,blue=led_blue)
        #print led_red,led_green,led_blue,led_dim

    def range_convert(self,value,old_min=0,old_max=65535,new_min=0,new_max=255):
		return (((value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

if __name__ == "__main__":
    ledcube_dialog()
