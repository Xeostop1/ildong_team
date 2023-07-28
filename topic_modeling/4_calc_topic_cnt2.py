from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora
import gensim
from nltk.tokenize import RegexpTokenizer

def main():
    tokenizer = RegexpTokenizer('[\w]+')
    stop_words = stopwords.words('english')
    p_stemmer = PorterStemmer()

    doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
    doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
    doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
    doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
    doc_e = "Health professionals say that brocolli is good for your health."
    doc_f = "Big data is a term used to refer to data sets that are too large or complex for traditional data-processing application software to adequately deal with."
    doc_g = "Data with many cases offer greater statistical power, while data with higher complexity may lead to a higher false discovery rate"
    doc_h = "Big data was originally associated with three key concepts: volume, variety, and velocity."
    doc_i = "A 2016 definition states that 'Big data represents the information assets characterized by such a high volume, velocity and variety to require specific technology and analytical methods for its transformation into value'."
    doc_j = "Data must be processed with advanced tools to reveal meaningful information."

    doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e, doc_f, doc_g, doc_h, doc_i, doc_j]

    texts = []

    for w in doc_set:
        raw = w.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in stop_words]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        texts.append(stemmed_tokens)

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary)

    from gensim.models import CoherenceModel
    print('\nPerplexity: ', ldamodel.log_perplexity(corpus))
    coherence_model_lda = CoherenceModel(model=ldamodel, texts=texts,
                                         dictionary=dictionary, topn=10)
    coherence_lda = coherence_model_lda.get_coherence()
    print('\nCoherence Score: ', coherence_lda)

    import matplotlib.pyplot as plt
    perplexity_values = []

    for i in range(2, 10):
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=i, id2word=dictionary)
        perplexity_values.append(ldamodel.log_perplexity(corpus))

    x = range(2, 10)
    plt.plot(x, perplexity_values)
    plt.xlabel("Number of topics")
    plt.ylabel("Perplexity score")
    plt.show()

    coherence_values = []
    for i in range(2, 10):
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=i,
                                                   id2word=dictionary)
        coherence_model_lda = CoherenceModel(model=ldamodel, texts=texts,
                                             dictionary=dictionary, topn=10)
        coherence_lda = coherence_model_lda.get_coherence()
        coherence_values.append(coherence_lda)
    x = range(2, 10)
    plt.plot(x, coherence_values)
    plt.xlabel("Number of topics")
    plt.ylabel("coherence score")
    plt.show()

if __name__ == "__main__":
    main()