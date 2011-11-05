from zope.interface import Interface


class ISetupCommand(Interface):
    def __call__():
        """ simple callable
        """
