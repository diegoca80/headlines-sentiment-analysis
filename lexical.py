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
    
 # Class to provide data and methods to read LIWC dictionary
class LiwcReader(dict):

    """
    Dictionary format:
    %
    1	funct
    2	pronoun
    ...
    125	affect
    126	posemo
    127	negemo
    128	anx
    129	anger
    130	sad
    ...
    %
    a	1	2	3	6	7	9	10	17	121	131	138	252	463
    aba	146
    abafa	125	127	129
    abafad*	125	127	129
    abafada	125	127	129
    abafadas	125	127	129
    abafado	125	127	129
    abafados	125	127	129
    """


    # Constructor
    # dict_file: the path to dictionary file
    def __init__(self, dict_file='LIWC/LIWC2007_Portugues_win.dic'):
        self.inverted_index = {}
        self.meta = {}

        handle = codecs.open(dict_file, 'r', 'iso8859-15')
        line = handle.readline()

        if line.strip() != '%':
            raise ValueError('Dictionary file must start with %')

        # Build the MetaTable
        line = handle.readline()
        while line.strip() != '%':
            code, gloss = line.split()
            try:
                self.meta[int(code)] = gloss
            except IOError:
                raise ValueError('.dic file is not in LIWC format')
            self.inverted_index[gloss] = set()
            line = handle.readline()

        # Run until the end of the file
        line = handle.readline()
        while line:

            itens = line.split()
            word = itens[0]
            try:
                categories = [int(x) for x in itens[1:]]
            except IOError:
                raise ValueError('.dic file is not in LIWC format.')

            self[word] = categories

            for cat in categories:
                self.inverted_index[self.meta[cat]].add(word)

            line = handle.readline()

        handle.close()
        self.sorted_dict = sorted(self.keys())

    # returns the inverted index
    def inverted_index(self):
        return self.inverted_index

    # returns the vocabulary
    def vocabulary(self):
        return set(self.keys())

    # returns the polar vocabulary
    def vocabulary_polar(self):
        vocabulary = set()
        for key in self:
            if self.polarity(key) != 0:
                vocabulary.add(key)
        return vocabulary

    # returns the mata_table which stands for the LIWC word categories
    def meta_table(self):
        return self.meta

    # returns the polarity of a given word. It may be -1, 0 or 1
    def polarity(self,word):
        _word = self.find_word(word)
        if _word in self:
            if 126 in self[_word]:
                return 1
            elif 127 in self[_word]:
                return -1
            else:
                return 0
        else:
            return None

    # returns the sorted dictionary
    def sorted_dictionary(self):
        return self.sorted_dict

    # finds a word in the lexicon and returns it.
    # If the word in the lexicon
    # has the wildcard *, returns the lexicon entry with the wildcard
    # If the word is not found, returns None
    def find_word(self, word):
        import bisect
        closest_index = max(bisect.bisect(self.sorted_dict, word) - 1, 0)
        search = self.sorted_dict[closest_index]
        if search == word:
            return search
        # contains a wildcard *
        elif search[-1] == '*' and search[:-1] == word[:len(search[:-1])]:
            return search
        else:
            return None

    # prints some statistics
    def print_statistics(self):

        print (':: Meta Categories e number of entries ::')
        for cat in sorted(self.inverted_index.keys()):
            print (cat, (20 - len(cat)) * ' ', len(self.inverted_index[cat]))

        print

        posemo = self.inverted_index['posemo']
        negemo = self.inverted_index['negemo']

        print (len(posemo.intersection(negemo)))
        print ('posemo e negemo interserction: ')
        for word in sorted(posemo.intersection(negemo)):
            print (word)

    # returns the dictionary name. LIWC
    def get_name(self):
        return 'Liwc'   