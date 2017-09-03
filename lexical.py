import codecs
import re

class OpLexiconReader(dict):



    # Constructor
    # dict_file: the path to dictionary file
    def __init__(self, dict_file='oplexicon_v3.0/lexico_v3.0.txt'):

        handle = codecs.open(dict_file, 'r', 'utf-8')

        # Run until the end of the file
        line = handle.readline()
        line = line.strip()
        while line:
            if not line.startswith('#') and not len(line)==0:

                phrase,pos,pol,labeling = line.split(',')
                try:
                    pol = int(pol)
                except:
                    print ('Error parsing the line:\n',line,'\n\n')

                if phrase in self:
                    self[phrase].append((pos,pol))
                else:
                    self[phrase] = [(pos,pol)]

            line = handle.readline()
            line = line.strip()

        handle.close()

    def get_name(self):
        return 'Opinion Lexicon'


    def print_statistics(self):
        return None

    def vocabulary(self):
        return set(self.keys())

    def vocabulary_polar(self):
        vocabulary = set()
        for key in self:
            if self.polarity(key) != 0:
                vocabulary.add(key)
        return vocabulary

    def polarity(self,word):
        if word in self:
            # how to select the polarity most representative among different
            # PoS
            # I took the first PoS occurency
            return self[word][0][1]
        else:
            return None


class SentiLexReader(dict):


    # Constructor
    # dict_file: the path to dictionary file
    def __init__(self, dict_file='sentiLex_pt02/SentiLex-flex-PT02.txt'):
        handle = codecs.open(dict_file, 'r', 'utf-8')

        line = handle.readline()
        prog = re.compile(r'([^,]*),([^.]*)\.PoS=([^;]*);([^;]*);TG=([^;]*);(POL:.*);ANOT=(.*)',re.I)
        while line:

        # Retrieve only the word/phrase and PoS
            m = prog.match(line)
            if m:
                phrase = m.group(1)
                lemma = m.group(2)
                pos = m.group(3)
                flex = m.group(4)
                target = m.group(5)
                polarities = m.group(6)
                anot = m.group(7)
                polarities = re.findall('POL:(N[0-9])=(-?[0-9])',polarities)
                polarities = [(srl,int(value)) for srl,value in polarities]
                if phrase in self:
                    self[phrase].append((pos,polarities))
                else:
                    self[phrase] = [(pos,polarities)]
            else:
                print (line)


            line = handle.readline()

        handle.close()

    #return all matches for a sentence which consists in list of words
    def match_words(self, sentence):

        i = 0
        length = len(sentence)
        j = length
        matches = []

        # iterate over the words present in the sentence
        while i < len(sentence):
            # get a slide window
            phrase = ' '.join(sentence[i:j])
            if i == j:
                i +=1
                j = length
            elif phrase in self:
                pos,polarities = self[phrase]
                matches.append( (phrase,pos,polarities) )
                i = j
                j = length
            else:
                j = j - 1

        return matches

    def print_statistics(self):
        return None

    def vocabulary(self):
        return set(self.keys())

    def vocabulary_polar(self):
        vocabulary = set()
        for key in self:
            if self.polarity(key) != 0:
                vocabulary.add(key)
        return vocabulary

    def polarity(self,word):
        if word in self:
            # how to select the polarity most representative among different
            # PoS and SRL?
            # I took the first PoS occurency and the fist SRL always
            return self[word][0][1][0][1]
        else:
            return None

    def get_name(self):
        return 'SentiLex'