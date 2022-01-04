import math
import re

class Bayes_Classifier:

    def __init__(self):
        self.positive_reviews=0
        self.negative_reviews=0
        self.dict=[]
        self.noofwords_pos=0
        self.noofwords_neg=0
        self.pos_list=dict()
        self.neg_list=dict()

    def train(self, lines):
        for l in lines:
            line = l.split('|')
            value=line[0]
            text=line[2]

            # text pre-processing
            text=self.preprocess(text)

            # to calculate Probability of positivie reviews and Probability of negative reviews
            if value=='1':
                self.negative_reviews= self.negative_reviews+1
            else: 
                self.positive_reviews=self.positive_reviews+1
                
            #   create vocabolary dict  to get total number of words
            for word in text:
                if word not in self.dict:
                    self.dict.append(word)

           # Next, total number of words in class +ve & neg
            for word in text:
                if value=='1':
                    if word in self.neg_list:
                        self.neg_list[word]=self.neg_list[word]+1

                    else:
                        self.neg_list[word]=1

                else:
                    if word in self.pos_list:
                        self.pos_list[word]=self.pos_list[word]+1

                    else:
                        self.pos_list[word]=1
                    


    def classify(self, lines):
        predict = []

        prob_pos_review= float(self.positive_reviews)/( self.positive_reviews+self.negative_reviews)
        prob_neg_review=1-prob_pos_review

        unique_words=len(self.dict)

        total_words_pos=0
        for key, value in self.pos_list.items():
            total_words_pos=total_words_pos+value

        total_words_neg=0
        for key, value in self.neg_list.items():
            total_words_neg=total_words_neg+value
        


        for l in lines:
            line = l.split('|')
            value=line[0]
            text=line[2]
            text=self.preprocess(text)

            prob_good=0  
            prob_bad=0
            
            # #  now classify each line 
            for word in text:  # no point in classify the same word again 
                # print(word)  


                #  using laplace smoothing 
                # Prob= (wordcount+1)/ totalposword+unique words

                #  probability its a pos reivew 
                if word in self.pos_list:  # if that word has contributed in review before 

                        # conditional probability 
                        prob_good=prob_good+math.log(float(self.pos_list[word]+1)/float(unique_words+total_words_pos))

                else:
                        prob_good=prob_good+math.log(1/float(unique_words+total_words_pos))     
            
                #  probability its a neg reivew 
                if word in self.neg_list:
                        prob_bad=prob_bad+math.log(float(self.neg_list[word]+1)/float(unique_words+total_words_neg))

                else:
                        prob_bad=prob_bad+math.log(1/float(unique_words+total_words_neg))

            
            # print(line[2],prob_good,prob_bad)
            if (prob_good) < (prob_bad):
                predict.append('1')
            else:
                predict.append('5')

        # print(predict)

        return predict
       
        # print(prob_pos_review,prob_neg_review)
        # print(total_words_pos,total_words_neg)

            



    def preprocess(self,t):
        t=list(t)


        # remove captilization
        t=[x.lower() for x in t]   
        t=''.join(t)

        # remove punctuations
        t=re.sub(r'[^\w\s]','',t)

        # remove stopwords
        stopwords=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 
        'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
        'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each',
        'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 
        'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 
        'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 
        'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why',
        'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 
        'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 
        'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

        t=t.split(' ')
        t=[x for x in t if x not in stopwords]

        return t 
   

