try:
    __import__('pkg_resources').declare_namespace(__name__)
except:
    __path__ = __import__('pkg_util').extends_path(__path__, __name__)

