#!/usr/bin/env python
# coding: utf-8

# ## Implement a trie tree

# ### Theoretical pondering 

# In[ ]:


class Node:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """
    
    def __init__(self):
        self.children = {}
        self.end = False  
        
class Trie:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's __init__ are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    
    def __init__(self, word_list = None):
        """Creates the Trie instance, inserts initial words if provided.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node() #create a root node
        for word in word_list: #iterate though the input string to create a tier tree for each word
            self.insert(word)
            
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        node = self.root
        for char in word.lower(): #put the word into lower case to ignore capital letters
            if char not in node.children: #if a character not in the children list of the root node, create a new node for it
                node.children[char] = Node()
            node = node.children[char] #otherwise add the character to the children list under the node
        node.end = True
        
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        node = self.root #create a root node
        for char in word.lower(): 
            if char in node.children: #if all characters in the input word match one of the node's children, return true 
                node = node.children[char]
            else:
                return False #if there is no one missmatch return False
        return node.end
    
wordbank = "Ai! laurië lantar lassi súrinen, yéni unótimë ve rámar aldaron! Yéni ve lintë yuldar avánier mi oromardi lisse-miruvóreva Andúnë pella, Vardo tellumar nu luini yassen tintilar i eleni ómaryo airetári-lírinen. Sí man i yulma nin enquantuva? An sí Tintallë Varda Oiolossëo ve fanyar máryat Elentári ortanë, ar ilyë tier undulávë lumbulë; ar sindanóriello caita mornië i falmalinnar imbë met, ar hísië untúpa Calaciryo míri oialë. Sí vanwa ná, Rómello vanwa, Valimar! Namárië! Nai hiruvalyë Valimar. Nai elyë hiruva. Namárië!".replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace(";", "").split()

trie = Trie(wordbank)
assert trie.lookup('oiolossëo') == True
assert trie.lookup('an') == True
assert trie.lookup('ele') == False
assert trie.lookup('Mithrandir') == False


# ### Print a dictionary in alphabetical order

# In[ ]:


class Node:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, c = None,  word = None):
        self.children = []
        self.end = False 
        self.word = word #stores the whole word 
        self.c  = c    #sotres a single character in the word

class Trie:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's __init__ are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    
    def __init__(self):
        """Creates the Trie instance.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node()

    def setWords(self, words):
        """Inserts initial words.
        
        Parameters
        ----------
        words : list
            List of strings to be inserted into the trie upon creation.
        """
        for word in words:
            self.insert(word.lower())
            
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        node = self.root
        for c in word.lower():
            pos = self.find(node, c)
            if pos < 0:
                node.children.append(Node(c)) 
                node.children = sorted(node.children, key=lambda child: child.c)
                pos = self.find(node, c)
            node = node.children[pos]
        node.word = word
        
    def find(self, node, c):
        """Finds the position where the character is inserted 
        Parameters
        ----------
        node : str
            The word to be looked-up in the trie.
        
        c : str
            The character to find in the tree
         
        Returns
        -------
        int
            i, -1, 1
            
        """
        childs = node.children 
        _len   = len(childs)
        if _len == 0:
            return -1
        for i in range(_len):
            if childs[i].c == c:
                return i
        return -1
    
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        node = self.root
        for char in word.lower():
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.end

    def alphabetical_list(self, node):
        """Delivers the content of the trie in alphabetical order.

        You can create other methods if it helps you,
        but the tests should use this one.
        
        Returns
        ----------
        list
            List of strings, all words from the trie in alphabetical order.
        """
        results = []
        if node.word: # if node.word exist in the tree, append it to the array
            results.append(node.word)
        for child in node.children: #iterate through the node's children to recursively call the method and append elements to the array
            results.extend(self.alphabetical_list(child))
        return results      


# In[ ]:


wordbank = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis pulvinar. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos. Nunc dapibus tortor vel mi dapibus sollicitudin. Etiam quis quam. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien.".replace(",", "").replace(".", "").split()

trie = Trie()
trie.setWords(wordbank)

assert trie.alphabetical_list(trie.root) == ['a','ad','adipiscing','amet','aptent',
                                    'class','consectetuer','conubia',
                                    'curabitur','dapibus','dolor','duis',
                                    'elit','etiam','facilisis','hymenaeos',
                                    'inceptos','ipsum','ligula','litora',
                                    'lorem','mi','nostra','nunc','per',
                                    'pulvinar','quam','quis','sapien',
                                    'sit','sociosqu','sollicitudin','taciti',
                                    'torquent','tortor','vel','vestibulum'] 


# ### Find the k most common words in a speech

# In[ ]:


import heapq #import heapq module to use its functions

class Node:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, c = None,  word = None, frequency = None):
        self.children = []
        self.end = False 
        self.word = word 
        self.c  = c    

class Trie:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's __init__ are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    
    def __init__(self):
        """Creates the Trie instance, inserts initial words if provided.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node()

    def setWords(self, words):
        """Inserts initial words, creates a dictionary with all words and their frequencies.
        
        Parameters
        ----------
        words : list
            List of strings to be inserted into the trie upon creation.
        
        Returns 
        -------
        dictionary: dict
            dictionary with keys being individual words and values being their frequencies in the input
        """
        i = 0
        dictionary = {} #create a dictionary to store frequencies for unique and repetitive words
        for word in words:
            if word.lower() not in dictionary: #if a word it is not yet in the dictionary, append it and its frequency which is 1
                dictionary[word.lower()] = 1
                i += 1 #move on to the next word
            else:
                dictionary[word.lower()] += 1 #if it is already there, increase its frequency by one
            self.insert(word.lower()) #insert the word to the tree
        return dictionary #return the dictionary to use it further in k_most_common method
            
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        node = self.root
        for c in word.lower():
            pos = self.find(node, c)
            if pos < 0:
                node.children.append(Node(c))
                node.children = sorted(node.children, key=lambda child: child.c)
                pos = self.find(node, c)
            node = node.children[pos]
        node.word = word
        
    def find(self, node, c):
        """Finds the position where the character is inserted 
        Parameters
        ----------
        node : str
            The word to be seacrhed in the tree
        
        c : str
            The character to find in the tree
         
        Returns
        -------
        int
            i, -1, 1
        """
        childs = node.children
        _len   = len(childs)
        if _len == 0:
            return -1
        for i in range(_len):
            if childs[i].c == c:
                return i
        return -1
    
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        node = self.root
        for char in word.lower():
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.end

    def alphabetical_list(self, node):
        """Delivers the content of the trie in alphabetical order.

        You can create other methods if it helps you,
        but the tests should use this one.
        
        Returns
        ----------
        list
            List of strings, all words from the trie in alphabetical order.
        """
        results = []
        if node.word:
            results.append(node.word)
        for child in node.children:
            results.extend(self.alphabetical_list(child))
        return results      
            
    def k_most_common(self, words, k):
        """Finds k words inserted into the trie most often.

        You will have to tweak some properties of your existing code,
        so that it captures information about repeated insertion.

        Parameters
        ----------
        k : int
            Number of most common words to be returned.

        Returns
        ----------
        list
            List of tuples.
            
            Each tuple entry consists of the word and its frequency.
            The entries are sorted by frequency.

        Example
        -------
        >>> print(trie.k_most_common(3))
        [(‘the’, 154), (‘a’, 122), (‘i’, 122)]
        
        I.e. the word ‘the’ has appeared 154 times in the inserted text.
        The second and third most common words both appeared 122 times.
        """        
        my_dict = self.setWords(words) # my_dict is equal to the dictionary created in the setWords method
        heapq.heapify(list(my_dict.values())) # heapify the list taht includes keys in the dictionary
        highest = heapq.nlargest(k, my_dict, key = my_dict.get) #find the largest frequencies (values) using nlargest function from heapq module
        common_dict = {} # adictionary to store most common words andt their frequencies in a tuple form
        for val in highest:
            common_dict[val]= my_dict[val] #append words and their frequencies
        common_dict = dict(sorted(common_dict.items(), key=lambda t: t[::-1], reverse = True)) #sort the dictionary based on values aka frequencies 
        common_list = common_dict.items() #getting items from the dictionary
        common_list = list(common_list) #converting dictionary items to tuples in a list
        return common_list


# In[ ]:


from requests import get
speakers = ['Faruqi', 'Kennedy', 'King', 'Thunberg', 'Havel']
bad_chars = [';', ',', '.', '?', '!', '_', 
             '[', ']', ':', '“', '”', '"', '–', '-']

for speaker in speakers:
    # download and clean up the speech from extra characters
    speech_full = get(f'https://bit.ly/CS110-{speaker}').text
    just_text = ''.join(c for c in speech_full if c not in bad_chars)
    without_newlines = ''.join(c if (c not in ['\n', '\r', '\t']) else " " for c in just_text)
    just_words = [word.lower() for word in without_newlines.split(" ") if word != ""]
    
    trie = Trie()
    
    for word in just_words:
        if any(i.isdigit() for i in word) == True:
            just_words.remove(word)

    if speaker == 'Faruqi':
        
        print("Faruqi:", trie.k_most_common(just_words, 20))
        Faruqi = [('the', 60), ('and', 45), ('to', 39), ('in', 37), 
                  ('of', 34), ('is', 25), ('that', 22), ('this', 21), 
                  ('a', 20), ('people', 20), ('has', 14), ('are', 13), 
                  ('for', 13), ('we', 13), ('have', 12), ('racism', 12), 
                  ('black', 11), ('justice', 9), ('lives', 9), ('police', 9)]
        #assert trie.k_most_common(just_words, 20) == Faruqi
    
    elif speaker == 'Kennedy':

        print("Kennedy:", trie.k_most_common(just_words, 21))
        Kennedy = [('the', 117), ('and', 109), ('of', 93), ('to', 63), 
                   ('this', 44), ('in', 43), ('we', 43), ('a', 39), 
                   ('be', 30), ('for', 27), ('that', 27), ('as', 26), 
                   ('it', 24), ('will', 24), ('new', 22), ('space', 22), 
                   ('is', 21), ('all', 15), ('are', 15), ('have', 15), ('our', 15)]
        #assert trie.k_most_common(just_words, 21) == Kennedy
    
    elif speaker == 'Havel':
        
        print("Havel:", trie.k_most_common(just_words, 22))
        Havel = [('the', 34), ('of', 23), ('and', 20), ('to', 15), 
                 ('in', 13), ('a', 12), ('that', 12), ('are', 9), 
                 ('we', 9), ('have', 8), ('human', 8), ('is', 8), 
                 ('you', 8), ('as', 7), ('for', 7), ('has', 7), ('this', 7), 
                 ('be', 6), ('it', 6), ('my', 6), ('our', 6), ('world', 6)]
        #assert trie.k_most_common(just_words, 22) == Havel
    
    elif speaker == 'King':
        
        print("King:", trie.k_most_common(just_words, 23))

        King = [('the', 103), ('of', 99), ('to', 59), ('and', 54), ('a', 37), 
                ('be', 33), ('we', 29), ('will', 27), ('that', 24), ('is', 23), 
                ('in', 22), ('as', 20), ('freedom', 20), ('this', 20), 
                ('from', 18), ('have', 17), ('our', 17), ('with', 16), 
                ('i', 15), ('let', 13), ('negro', 13), ('not', 13), ('one', 13)]
        #assert trie.k_most_common(just_words, 23) == King
    
    elif speaker == 'Thunberg':
        
        print("Thunber:", trie.k_most_common(just_words, 24))

        Thunberg = [('you', 22), ('the', 20), ('and', 16), ('of', 15), 
                    ('to', 14), ('are', 10), ('is', 9), ('that', 9), 
                    ('be', 8), ('not', 7), ('with', 7), ('i', 6), 
                    ('in', 6), ('us', 6), ('a', 5), ('how', 5), ('on', 5), 
                    ('we', 5), ('all', 4), ('dare', 4), ('here', 4), 
                    ('my', 4), ('people', 4), ('will', 4)]
        #assert trie.k_most_common(just_words, 24) == Thunberg


# ### Implement an autocomplete with a Shakespearean dictionary

# In[ ]:


class Node:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, c = None,  word = None, frequency = None):
        self.children = {}
        self.last = False

class Trie:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's __init__ are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    
    def __init__(self):
        """Creates the Trie instance
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node()
        self.word_list = []

    def setWords(self, words):
        """Inserts initial words, creates a dictionary with all words and their frequencies.
        
        Parameters
        ----------
        words : list
            List of strings to be inserted into the trie upon creation.
        
        Returns 
        -------
        dictionary: dict
            dictionary with keys being individual words and values being their frequencies in the input
        """
        i = 0
        dictionary = {}
        for word in words:
            if word.lower() not in dictionary:
                dictionary[word.lower()] = 1
                i += 1
            else:
                dictionary[word.lower()] += 1 
            self.insert(word.lower())
        return dictionary
            
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        node = self.root
        for a in list(word):
            if not node.children.get(a):
                node.children[a] = Node()
            node = node.children[a]
        node.last = True
    
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        node = self.root
        found = True
 
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        return node and node.last and found     
        
    def suggestionsRec(self, node, word):
        """Recursively traverse the trie and returns a whole word.

        Parameters
        ----------
        node : str
            The first letter

        word : str
            The word to search
        Returns
        ----------
        list
            The whole word
        """
        if node.last: #if we reached the last letter/leaf, return the list with all complete words starting with the given prefix
            self.word_list.append(word)
 
        for a,n in node.children.items(): #iterate through all the children of node letter to increment a letter to the word 
            self.suggestionsRec(n, word + a)
            
    def autocomplete(self, prefix, words):
        """Finds the most common word with the given prefix.

        You might want to reuse some functionality or ideas from Q4.

        Parameters
        ----------
        prefix : str
            The word part to be “autocompleted”.

        Returns
        ----------
        str
            The complete, most common word with the given prefix.
            
        Notes
        ----------
        The return value is equal to prefix if there is no valid word in the trie.
        The return value is also equal to prefix if prefix is the most common word.
        """
        my_dict = self.setWords(words) #run setWords method to derive a dictionary with all the words and their frequencies
        node = self.root #initiate variables 
        not_found = False
        temp_word = ''
        
        for a in list(prefix): 
            if not node.children.get(a): # if at least one charcater is not found continue to the next iteration
                not_found = True
                break
            temp_word += a
            node = node.children[a]
        if not_found: #if not found is True and there is no word with such prefix, return the prefix
            return prefix
        
        self.suggestionsRec(node, temp_word) #recursively traverse the trie and returns a whole word and return the list containing al words with such a prefix
        
        max_frequency = 0 #initiate variables to find the most common word from the list 
        suggested = prefix #the prefix might be the most common word in the dictionary 
        for s in self.word_list:
            if my_dict.get(s) > max_frequency: #if the frequency if s is higher update variables
                suggested = s #update suggested word to s
                max_frequency = my_dict.get(s) #update maximum frequency to s's frequency from the dictionary
        return str(suggested) #the most common string


# In[ ]:


from requests import get
bad_chars = [';', ',', '.', '?', '!', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0', '_', '[', ']']

SH_full = get('http://bit.ly/CS110-Shakespeare').text
SH_just_text = ''.join(c for c in SH_full if c not in bad_chars)
SH_without_newlines = ''.join(c if (c not in ['\n', '\r', '\t']) else " " for c in SH_just_text)
SH_just_words = [word for word in SH_without_newlines.split(" ") if word != ""]


# In[ ]:


SH_trie = Trie()
assert SH_trie.autocomplete('hist', SH_just_words) == 'history'
assert SH_trie.autocomplete('en', SH_just_words) == 'enter'
assert SH_trie.autocomplete('cae', SH_just_words) == 'caesar'
assert SH_trie.autocomplete('gen',SH_just_words) == 'gentleman'

