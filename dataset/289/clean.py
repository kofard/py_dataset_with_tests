import string
from math import log10
"\n    tf-idf Wikipedia: https://en.wikipedia.org/wiki/Tf%E2%80%93idf\n    tf-idf and other word frequency algorithms are often used\n    as a weighting factor in information retrieval and text\n    mining. 83% of text-based recommender systems use\n    tf-idf for term weighting. In Layman's terms, tf-idf\n    is a statistic intended to reflect how important a word\n    is to a document in a corpus (a collection of documents)\n\n\n    Here I've implemented several word frequency algorithms\n    that are commonly used in information retrieval: Term Frequency,\n    Document Frequency, and TF-IDF (Term-Frequency*Inverse-Document-Frequency)\n    are included.\n\n    Term Frequency is a statistical function that\n    returns a number representing how frequently\n    an expression occurs in a document. This\n    indicates how significant a particular term is in\n    a given document.\n\n    Document Frequency is a statistical function that returns\n    an integer representing the number of documents in a\n    corpus that a term occurs in (where the max number returned\n    would be the number of documents in the corpus).\n\n    Inverse Document Frequency is mathematically written as\n    log10(N/df), where N is the number of documents in your\n    corpus and df is the Document Frequency. If df is 0, a\n    ZeroDivisionError will be thrown.\n\n    Term-Frequency*Inverse-Document-Frequency is a measure\n    of the originality of a term. It is mathematically written\n    as tf*log10(N/df). It compares the number of times\n    a term appears in a document with the number of documents\n    the term appears in. If df is 0, a ZeroDivisionError will be thrown.\n"

def term_frequency(term: str, document: str) -> int:
    """Return the number of times a term occurs within
    a given document.
    @params: term, the term to search a document for, and document,
            the document to search within
    @returns: an integer representing the number of times a term is
            found within the document

    @examples:"""
    document_without_punctuation = document.translate(str.maketrans('', '', string.punctuation)).replace('\n', '')
    tokenize_document = document_without_punctuation.split(' ')
    return len([word for word in tokenize_document if word.lower() == term.lower()])

def document_frequency(term: str, corpus: str) -> tuple[int, int]:
    """Calculate the number of documents in a corpus that contain a
    given term
    @params : term, the term to search each document for, and corpus, a collection of
             documents. Each document should be separated by a newline.
    @returns : the number of documents in the corpus that contain the term you are
               searching for and the number of documents in the corpus
    @examples :"""
    corpus_without_punctuation = corpus.lower().translate(str.maketrans('', '', string.punctuation))
    docs = corpus_without_punctuation.split('\n')
    term = term.lower()
    return (len([doc for doc in docs if term in doc]), len(docs))

def inverse_document_frequency(df: int, n: int, smoothing=False) -> float:
    """Return an integer denoting the importance
    of a word. This measure of importance is
    calculated by log10(N/df), where N is the
    number of documents and df is
    the Document Frequency.
    @params : df, the Document Frequency, N,
    the number of documents in the corpus and
    smoothing, if True return the idf-smooth
    @returns : log10(N/df) or 1+log10(N/1+df)
    @examples :"""
    if smoothing:
        if n == 0:
            raise ValueError('log10(0) is undefined.')
        return round(1 + log10(n / (1 + df)), 3)
    if df == 0:
        raise ZeroDivisionError('df must be > 0')
    if n == 0:
        raise ValueError('log10(0) is undefined.')
    return round(log10(n / df), 3)

def tf_idf(tf: int, idf: int) -> float:
    """Combine the term frequency
    and inverse document frequency functions to
    calculate the originality of a term. This
    'originality' is calculated by multiplying
    the term frequency and the inverse document
    frequency : tf-idf = TF * IDF
    @params : tf, the term frequency, and idf, the inverse document
    frequency
    @examples :"""
    return round(tf * idf, 3)