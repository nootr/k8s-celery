#!/usr/bin/env python

from myapp.tasks import add
add.delay(4, 4)
