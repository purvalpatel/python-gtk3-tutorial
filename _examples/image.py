#!/usr/bin/env python3

from gi.repository import Gtk

class Image(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        image = Gtk.Image()
        image.set_from_file("../_resources/gtk.png")
        self.add(image)

window = Image()
window.show_all()

Gtk.main()
