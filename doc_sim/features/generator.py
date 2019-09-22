import spacy
import numpy as np
from doc_sim.models import Model
from doc_sim.utilities import Logger


class Generator:
    def __init__(self):
        """
        Load vectors directly from the file
        """
        self._model = Model()
        self._nlp = spacy.load('en_core_web_sm')

    def description_vector(self, sentence: str):
        """
        vectorize the input sentence
        :param sentence:
        :return:
        """
        Logger().info('tokenizing the sentence : {}'.format(sentence))
        target_vector = [0] * 300

        # tokenize the sentence into words
        for word in self._nlp(sentence):
            if word.pos_ == 'NUM' or word.pos_ == 'SPACE' or word.pos_ == 'PUNCT' or word.pos_ == 'SYM':
                continue
            word2vec = self._model.word2vec(word.lemma_.lower())
            target_vector = np.add(target_vector, word2vec)

        return target_vector
