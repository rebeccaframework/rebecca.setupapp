from .directives import add_setup

def includeme(config):
    config.add_directive('add_setup', add_setup)
