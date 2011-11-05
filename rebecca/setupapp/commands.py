import sys
from argparse import ArgumentParser
from pyramid.paster import bootstrap
import inspect

from .util import get_setup_commands, get_setup_command

class SetupApp(object):
    def __init__(self, registry):
        self.registry = registry

    @property
    def command_names(self):
        return list(c[0] for c in get_setup_commands(self.registry))


    def __call__(self, command_name):
        command = get_setup_command(self.registry, command_name)
        command()

    def make_parser(self):
        parser = ArgumentParser()
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

        return parser

def main(args=sys.argv[1:]):
    inifile, args = args[0], args[1:]
    app = bootstrap(inifile)
    setup_app = SetupApp(app['registry'])
    parser = setup_app.make_parser()
    args = parser.parse_args(args)
    setup_app(args.command_name)

if __name__ == '__main__':
    main()
