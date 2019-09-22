from numpy import dot
from numpy.linalg import norm


def cosine_similarity(x, y):
    return dot(x, y) / (norm(x) * norm(y))
