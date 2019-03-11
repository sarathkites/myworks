#import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
#from nltk.corpus import names

class NaiveClassifier:
    
    def __init__(self):
        print("Naive Bayes Classifier")
        
    def word_feats(self,words):
        return dict([(word, True) for word in words])
    
    def train_classifier(self,ctypes,type_words):
    
        train_set = list()
        
        for ctype in ctypes:
            #print(type_words[type])
            
            word_features = [(self.word_feats(word), ctype) for word in type_words[ctype]]
            train_set = train_set + word_features
        
        #print(train_set)
        
        classifier = NaiveBayesClassifier.train(train_set) 
        return classifier

    def predict_result(self,ctypes,classifier,sentence):
        count = dict()
        result = dict()
        for ctype in ctypes:
            count[ctype] =0
        
        #sentence = "Awesome movie, I liked it"
        sentence = sentence.lower()
        words = sentence.split(' ')
        for word in words:
            classResult = classifier.classify(self.word_feats(word))
            count[classResult] = count[classResult] +1
        
        for ctype in ctypes:
            #print('{}: {}'.format(type, str(float(count[type])/len(words))))
            result[ctype] = float(count[ctype])/len(words)
        
        return result    
    def find_max_polarity(self,ctypes,result_set):
        polarity = ""
        val = 0
        for ctype in ctypes:
            tval = result_set[ctype]
            if tval >= val:
                polarity = ctype
                val =tval
                
        return polarity        