
import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
from config import main_token
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import re

class DataCleaning ():
  def __init__(self,data):
    self.data=data

  def preprocessing (self):
    def lower_text(text):
      df=text.lower()
      return df
    def remove_punctuations (text):
      #replace every punctuation with a whitespace to keep the words correct
      text = re.sub(r'[^\w\s]',' ',text)
      #remove the successive whitespaces
      _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
      no_punc = _RE_COMBINE_WHITESPACE.sub(" ", text).strip()
      return no_punc
    self.data['questions']=self.data['questions'].apply(lower_text)
    self.data['questions']=self.data['questions'].apply(remove_punctuations)
    return self.data


class GetAnswer ():
  def __init__(self,data,question,vectorizer):
    self.question=question
    self.data=data
    self.vectorizer=vectorizer
  def getAnswer(self):
    def vectorize(self):
      X_cv=self.vectorizer.transform(data['questions'].values)
      question_cv=self.vectorizer.transform(np.squeeze(self.question.values))
      return X_cv,question_cv
    def cosine_distance(self):
      cosine_dist=[]
      for item in self.X_cv:
        cosine_dist.append(cosine_similarity(item, self.question_cv[0])[0][0])
      return cosine_dist
    self.X_cv,self.question_cv=vectorize(self)
    self.cosine_dist=cosine_distance(self)
    return self.data['answers'].values[self.cosine_dist.index(max(self.cosine_dist))]


vk_sesssion=vk_api.VkApi(token=main_token)
longpoll=VkLongPoll(vk_sesssion)

def sender(id,text):
    vk_sesssion.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

vect=pickle.load(open('CountVect','rb'))
data = pd.read_csv('C:/ParserChatBot/datasetBotTest.csv')
data = data.drop('Unnamed: 0', axis=1)
DC=DataCleaning(data)
data_clean=DC.preprocessing()
for event in longpoll.listen():
    if event.type==VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg=event.text.lower()
                id = event.chat_id

                #if msg == 'привет':
                #    sender(id, 'Здарова ёптааа')
                #else:
                #    sender (id, 'ёптааа')
                msg_dict={'questions':[msg,' ']}
                msg_pd = pd.DataFrame(msg_dict)
                msg_clean = DataCleaning(msg_pd).preprocessing()
                G_A = GetAnswer(data_clean,msg_clean,vect)
                sender (id,f'{G_A.getAnswer()}')

