from doc_sim.features import Generator
from doc_sim.models import Model
from doc_sim.utilities import cosine_similarity


class DocSimService(object):
    def __init__(self):
        self._generator = Generator()
        self._model = Model()

    def similarity(self, sent_1, sent_2):
        """
        similarity between two sentences
        :param sent_1:
        :param sent_2:
        :return:
        """
        return cosine_similarity(self._generator.description_vector(sent_1),
                                 self._generator.description_vector(sent_2)) * 5

    def doc_sim(self, doc_1, doc2):
        """
        similarity between two documents
        :param doc_1:
        :param doc2:
        :return:
        """
        pass
