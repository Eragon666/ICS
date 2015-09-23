#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app
from glumpy.graphics.collections import PointCollection
from glumpy.transforms import LinearScale, Position, Viewport

window = app.Window(1024,1024, color=(1,1,1,1))

@window.event
def on_draw(dt):
    window.clear()
    points.draw()

@window.event
def on_mouse_scroll(x,y,dx,dy):
    if dy < 0:
        transform["domain"] = 1.1*transform["domain"]
    else:
        transform["domain"] = transform["domain"]/1.1


transform = Position(LinearScale())
points = PointCollection("agg", transform = transform)
points.append( P = np.random.normal(0,.5,(10000,3)) )

window.attach(points["transform"])
window.attach(points["viewport"])
app.run()
