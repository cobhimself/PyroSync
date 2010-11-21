#!/usr/bin/python

#PyrosyncPreset class used by the pyrosync.py script

class Preset():
    """Holds the information about each of the presets"""
    def __init__(self, name):
        """Initiate initial values"""
        self.name = name

    def __str__(self):
        return repr(self.value)

    def set_description(self, description):
        """Sets the description for this preset"""
        self.description = description

    def set_options(self, options):
        """Sets the options for this preset"""
        self.options = options

    def set_source(self, source):
        """Sets the source for this preset"""
        self.source = source

    def set_destination(self, destination):
        """Sets the destination for this preset"""
        self.destination = destination

    def get_description(self):
        """Returns the description of this preset"""
        return self.description

    def get_options(self):
        """Returns the options of this preset"""
        return self.options

    def get_source(self):
        """Returns the source of this preset"""
        return self.source

    def get_destination(self):
        """Returns the destination of this preset"""
        return self.destination