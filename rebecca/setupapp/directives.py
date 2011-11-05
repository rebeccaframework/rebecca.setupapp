from .interfaces import ISetupCommand

def add_setup(self, name, setup):
    self.registry.registerUtility(setup, ISetupCommand, name=name)
