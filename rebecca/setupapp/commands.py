import sys
from argparse import ArgumentParser
from pyramid.paster import bootstrap

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

def make_parser():
    parser = ArgumentParser()
    parser.add_argument('ini')
    parser.add_argument('-l', '--list',
        action='store_true',
        help="list command names")
    parser.add_argument('command_name',
        default='main')
    return parser

def main(args=sys.argv[1:]):
    parser = make_parser()
    args = parser.parse_args(args)
    app = bootstrap(args.ini)
    setup_app = SetupApp(app['registry'])
    if args.list:
        print setup_app.command_names
    else:
        setup_app(args.command_name)

if __name__ == '__main__':
    main()
