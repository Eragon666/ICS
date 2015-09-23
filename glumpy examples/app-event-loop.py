#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
""" This example shows how to run the event loop manually """

from glumpy import app

window = app.Window()

@window.event
def on_draw(dt):
    window.clear()

backend = app.__backend__
clock = app.__init__(backend=backend)
count = len(backend.windows())
while count:
    count = backend.process(clock.tick())
