#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provide simple netns operation.
"""

from subprocess import check_call
import subprocess



class Snetns(object):
    """Snetns is a representation of netns
    """

    def __init__(self, name=None):
        """initializer
        """
        self.name = name

    def create(self):
        """create netns
        """
        try:
            check_call(['sudo', 'ip', 'netns', 'create', self.name])

        except subprocess.SubprocessError as e:
            print e
        except subprocess.CalledProcessError as e:
            print e

    def destroy(self):
        """destroy netns
        """
        pass


Snetns('test').create()
