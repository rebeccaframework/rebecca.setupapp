
import inspect
from argparse import ArgumentParser

from .directives import add_setup
from .util import get_setup_commands, get_setup_command

class SetupApp(object):
    def __init__(self, registry):
        self.registry = registry

    @property
    def command_names(self):
        return list(c[0] for c in get_setup_commands(self.registry))


    def __call__(self, command_name, args):
        command = get_setup_command(self.registry, command_name)
        argspec = inspect.getargspec(command)
        defaults = {}
        if argspec[3] is not None:
            defaults = dict(zip(reversed(argspec[0]), reversed(argspec[3])))
        command_args = [(n, getattr(args, n) if hasattr(args, n) else defaults[n]) 
                for n in argspec[0]]
        command_args = dict(command_args)
        command(**command_args)

    def make_parser(self):
        parser = ArgumentParser()

        self.add_commands(parser)

        return parser

    def add_commands(self, parser):
        parsers = parser.add_subparsers()
        for name, c in get_setup_commands(self.registry):
            argspec = inspect.getargspec(c)
            defaults = {}
            if argspec[3] is not None:
                defaults = dict(zip(reversed(argspec[0]), reversed(argspec[3])))
            sub = parsers.add_parser(name, help=c.__doc__)
            for n in argspec[0]:
                if n not in defaults:
                    sub.add_argument(n)
                else:
                    sub.add_argument('--' + n, default=defaults[n])
            sub.set_defaults(command_name=name)

def includeme(config):
    config.add_directive('add_setup', add_setup)
