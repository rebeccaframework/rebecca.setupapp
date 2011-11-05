from .interfaces import ISetupCommand


def get_setup_commands(registry):
    return registry.getUtilitiesFor(ISetupCommand)

def get_setup_command(registry, name):
    return registry.getUtility(ISetupCommand, name=name)

