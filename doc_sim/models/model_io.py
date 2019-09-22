from gensim.models import KeyedVectors
from doc_sim.utilities import Logger
from doc_sim import config
from doc_sim.utilities import Config


class Model:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        pass

    @staticmethod
    def load_model():
        """
        Load vectors directly from the file
        :return:
        """
        model = KeyedVectors.load_word2vec_format(Config().Models().read('word2vec'), binary=True)

        return model

    @staticmethod
    def word2vec(word):
        """
        return the vector of each word
        :param word:
        :return:
        """
        vector = [0] * 300
        try:
            vector = config.model[word]
        except KeyError:
            Logger().info("{} not found in the vocabulary".format(word))

        return vector
