import json
import os
from pathlib import Path
from doc_sim.exceptions import ConfigException


class Config(object):
    """This `singleton' class represents the entire config.json file.

    However, end-users should not directly use `Config` class. Instead
    we provide a set of classes such as `Database`, `Logging`, and etc.
    to represent sub-sections of the config.json file.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if not cls._instance:
            cls._instance = object.__new__(cls)
            path = Path(__file__)
            parents = path.parents
            file = os.path.join(parents[2], 'config.json')
            with open(file) as config_file:
                cls._instance.root = json.load(config_file)
        return cls._instance

    class Database(object):
        """ Database class represents the `DATABASE` section of the config.json

            Use `read` method of the `Database` class to read
            config parameters of the `DATABASE` section of the
            `config.json` file.
        """

        _instance = None

        def __new__(cls, *args, **kwargs):
            """

            :param args:
            :param kwargs:
            :return:
            """
            if not cls._instance:
                cls._instance = object.__new__(cls)
            return cls._instance

        @staticmethod
        def _read_database_configs():
            if Config().root['DATABASE'] is None:
                raise ConfigException('DATABASE key is in config.json file')
            return Config().root['DATABASE']

        def read(self, config):
            configs = self._read_database_configs()
            if config not in configs:
                raise ConfigException(
                    'DATABASE/{} is not in config.json file'.format(config))
            return configs[config]

    class Logging(object):
        """Logging class represents the `LOGGING` section of the config.json

            Use `read` method of the `Logging` class to read
            config parameters of the `LOGGING` section of the
            `config.json` file.
        """
        _instance = None

        def __new__(cls, *args, **kwargs):
            """

            :param args:
            :param kwargs:
            :return:
            """
            if not cls._instance:
                cls._instance = object.__new__(cls)
            return cls._instance

        @staticmethod
        def _read_logging_configs():
            if not Config().root['LOGGING']:
                raise ConfigException(
                    'LOGGING top-level group is not in config.json file')
            return Config().root['LOGGING']

        def read(self, config_name):
            configs = self._read_logging_configs()
            if config_name not in configs:
                raise ConfigException(
                    'LOGGING/{} is not in config.json file'.format(config_name))
            return configs[config_name]

    class Models:
        """Logging class represents the `MODELS` section of the config.json

            Use `read` method of the `Models` class to read
            config parameters of the `MODELS` section of the
            `config.json` file.
        """
        _instance = None

        def __new__(cls, *args, **kwargs):
            """

            :param args:
            :param kwargs:
            :return:
            """
            if not cls._instance:
                cls._instance = object.__new__(cls)
            return cls._instance

        @staticmethod
        def _read_model_configs():
            if not Config().root['MODELS']:
                raise ConfigException(
                    'MODELS top-level group is not in config.json file')
            return Config().root['MODELS']

        def read(self, config_name):
            configs = self._read_model_configs()
            if config_name not in configs:
                raise ConfigException(
                    'MODELS/{} is not in config.json file'.format(config_name))
            return configs[config_name]
