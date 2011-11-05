import sys
from pyramid.paster import bootstrap
from . import SetupApp

def main(args=sys.argv[1:]):
    inifile, args = args[0], args[1:]
    app = bootstrap(inifile)
    closer = app['closer']
    try:
        setup_app = SetupApp(app['registry'])
        parser = setup_app.make_parser()
        args = parser.parse_args(args)
        setup_app(args.command_name, args)
    finally:
        closer()

if __name__ == '__main__':
    main()
