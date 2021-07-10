#%%
from PyDictionary import PyDictionary
dictionary=PyDictionary()



def sample_responses(input_text):
  user_message = str(input_text).lower()

  result = dictionary.meaning(user_message)
  return result



