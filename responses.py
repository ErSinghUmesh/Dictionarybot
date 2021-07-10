#%%
from PyDictionary import PyDictionary
import json
dictionary=PyDictionary()



def sample_responses(input_text):
  user_message = str(input_text).lower()

  result = json.dumps(dictionary.meaning(user_message))
  return result



