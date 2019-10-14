import os, re, sys


def main():
    
    """  1. """
    
    dataDir = input()
    sequenceFile = input()
    dataDirAbsPath = os.path.abspath(dataDir)
    fileAbsPath = os.path.abspath(sequenceFile)
    
    languages = []
    i = 0
    mapLangBigrams = {}  # key is language, value is map that contains bigrams and number of their occurrences for given language
    
    languages = os.listdir(dataDirAbsPath)
    #numOfLanguages = len(languages)
    
    languagesDirs = [os.path.join(dataDirAbsPath, o) for o in os.listdir(dataDirAbsPath) 
                    if os.path.isdir(os.path.join(dataDirAbsPath,o))]
    
    for langDir in languagesDirs:
        
        mapBigramNum = {}  # key is bigram, value is number of occurrences of that bigram

        for thisDir, dirnames, filenames in os.walk(langDir):
            
            for filename in filenames:
                
                try:
                    f = open(os.path.join(os.path.abspath(thisDir), filename), mode = "r", encoding="utf-8")
                    
                    for line in f:
                        
                        bigramsInLine = re.findall(r'(?=([^\n\r]{2}))', line, re.U)
                        
                        for bigram in bigramsInLine:
                            if(bigram.lower() in mapBigramNum.keys()):
                                mapBigramNum[bigram.lower()] += 1
                            else:
                                mapBigramNum[bigram.lower()] = 1
                        
                except IOError:
                    sys.exit("file open failed")
        
        mapLangBigrams[languages[i]] = mapBigramNum
        i+=1
            

        
    for k1 in sorted(mapLangBigrams):
        # sort by value descending, then lexicographically by key ascending
        mostFrequent = sorted(mapLangBigrams[k1].items(), key = lambda kv: (-kv[1], kv[0]))[:5]
        for mf in mostFrequent:
            print("%s,%s,%d"%(k1, mf[0], mf[1]))
        
    
    """  2. """
    
    # P(Li|text) = (P(text|Li) * P(Li) ) / P(text)
    # text = [bg1, ..., bgn]
    # P(Li|text) = P(bg1|Li) * ... * P(bgn|Li) * P(Li) 
    # P(Li|text) = P(bg1|Li) * ... * P(bgn|Li) because Li are equally likely
    
    
    languages = sorted(languages)
    langProbabilities = {}
    
    
    try:
        f = open(sequenceFile, "r")
        
        for line in f:
            bigramsInLine = re.findall(r'(?=([^\n\r]{2}))', line, re.U)
            #numOfBigrams = len(bigramsInLine)
            
            for lang in languages:
                langProbabilities[lang] = 1
            
            for bigram in bigramsInLine:
                for lang in languages:
                    mapTmp = mapLangBigrams[lang]
                    if(bigram.lower() in mapTmp.keys()):
                        langProbabilities[lang] *= (mapTmp[bigram.lower()]/sum(mapTmp.values()))
                    else:
                        langProbabilities[lang] = 0
                        
            
            sumAllProbabilities = sum(langProbabilities.values())
            
            # normalize
            for lang in languages:
                if(sumAllProbabilities != 0):
                    langProbabilities[lang] /= sumAllProbabilities
            
            for lang in languages:
                print("%s, %.18f"%(lang, langProbabilities[lang]))
                
            
    except IOError:
        sys.exit("file open failed")
                    

if __name__ == '__main__':
    main()