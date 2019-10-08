


class Sentence():
    def __init__(self,the_sentence):
        self.the_sentence=the_sentence.split(' ')



    def get_first_word(self):
        first_word=self.the_sentence[0]
        return first_word
    def get_all_words(self):
        return self.the_sentence

    def replace(self,index, new_word):
        try:
            self.the_sentence[index]=new_word
            return self.the_sentence
        except:
            pass






sent = Sentence('Here we have a longer sentence')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(2, "find")
print(sent.get_all_words())
sent.replace(10,"bla")
print(sent.get_all_words())

assert str(sent.get_all_words()) == "['Here', 'we', 'find', 'a', 'longer', 'sentence']"
