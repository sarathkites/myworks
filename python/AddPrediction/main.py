from variables import TRAINSET,FILENAME,get_words
from fileop import FileOp
from naive_classifier import NaiveClassifier
from s_reader import SpeechHandler

def naive_step(sentence):
    
    obj = FileOp()
    cdirs = obj.get_types(TRAINSET)
    type_words = dict()

    for cdir in cdirs:
        fpath = TRAINSET+"/"+cdir+"/"+FILENAME 
        content = str(obj.get_contents(fpath))
        #print(content)
        #print(get_words(content,','))
        type_words[cdir] = get_words(content,',')

    #print(type_words)

    obj2 = NaiveClassifier()
    classifier = obj2.train_classifier(cdirs, type_words)
    #sentence = "Awesome movie, I liked it"

    result = obj2.predict_result(cdirs, classifier, sentence)
    result = obj2.find_max_polarity(cdirs, result)
    return result


obj = SpeechHandler()
txt = obj.wavparser('audio/out.wav')
print(txt)
print("Done")



sentence = txt#"Awesome movie, I liked it"    
result = naive_step(sentence)
print("The identified video category is {} ".format(result))
    
