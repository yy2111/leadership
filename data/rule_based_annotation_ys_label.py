# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:54:47 2020

@author: saran
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:40:04 2020

@author: saran
"""

import pandas as pd
data=pd.read_excel(r'C:\New_partition\Dr_Yang\Doc\data_15.7.2020\closed_comment_annotated.xlsx')
df = pd.DataFrame(data)
print (df)
df['comment_content']=df['comment_content'].str.replace(r'\n','').str.strip()
df["comment_content"] = df["comment_content"].str.lower()
print (df)
df['Predicted_YY_label']=""
for i in range (0,18657):
    #if 'Could you' or 'you can use' or 'I would suggest' or 'you can use to' or 'could be' or 'it would be nice' or 'you need to' or 'you can check' or 'be careful' or 'you should' or 'you can work' or 'you can use the' in df['comment_content'].iloc[i]:
    if 'have you followed' in df['comment_content'].iloc[i] or \
       'you can always' in df['comment_content'].iloc[i] or\
       'try' in df['comment_content'].iloc[i] or\
       'it seems to be' in df['comment_content'].iloc[i] or\
       'looks like' in df['comment_content'].iloc[i] or\
       'you can check' in df['comment_content'].iloc[i] or\
       'you need to' in df['comment_content'].iloc[i] or\
       'i recommend' in df['comment_content'].iloc[i] or\
       'i solve ' in df['comment_content'].iloc[i] or\
       'a general idea' in df['comment_content'].iloc[i] or\
       'you can use' in df['comment_content'].iloc[i] or\
       'you can give...a try?' in df['comment_content'].iloc[i] or\
       'you can check ' in df['comment_content'].iloc[i] or\
       'pull request' in df['comment_content'].iloc[i] or\
       'you must' in df['comment_content'].iloc[i] or\
       'could you try' in df['comment_content'].iloc[i] or\
       'solved' in df['comment_content'].iloc[i] or\
       'you can reproduce this' in df['comment_content'].iloc[i]:
       if df['Predicted_YY_label'].loc[i] != '': 
         df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'IS3'
       else:
         df['Predicted_YY_label'].loc[i]='IS3' 

    if 'should' in df['comment_content'].iloc[i] or \
       'may be' in df['comment_content'].iloc[i] or\
       'introduce idea' in df['comment_content'].iloc[i] or\
       'suggestion' in df['comment_content'].iloc[i] or\
       'a much directer way' in df['comment_content'].iloc[i] or\
       'if you want to…then' in df['comment_content'].iloc[i] or\
       'i guess' in df['comment_content'].iloc[i] or\
       "i would't" in df['comment_content'].iloc[i] or\
       'in fact' in df['comment_content'].iloc[i] or\
       'perhaps' in df['comment_content'].iloc[i] or\
       'i disagree' in df['comment_content'].iloc[i] or\
       'no,' in df['comment_content'].iloc[i]:
       if df['Predicted_YY_label'].loc[i] != '': 
         df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'IS4'
       else:
         df['Predicted_YY_label'].loc[i]='IS4'  

    if 'bitcoin stackExchange' in df['comment_content'].iloc[i] or\
        'have a look on bitcoin' in df['comment_content'].iloc[i] or\
        'try the bitcoin stack exchange' in df['comment_content'].iloc[i] or\
        'please help to review' in df['comment_content'].iloc[i] or\
        'best directed to' in df['comment_content'].iloc[i] or\
        'this is not the place to get support' in df['comment_content'].iloc[i] or\
        'kind of questions to' in df['comment_content'].iloc[i] or\
        'please ask in' in df['comment_content'].iloc[i] or\
        'please ask in' in df['comment_content'].iloc[i] or\
        'https://bitcoin.stackexchange.com' in df['comment_content'].iloc[i] or\
        'please ask questions somewhere like' in df['comment_content'].iloc[i] or\
		'this is not a place to' in df['comment_content'].iloc[i] or\
        'please see' in df['comment_content'].iloc[i] or\
		'please ask your question somewhere like' in df['comment_content'].iloc[i] or\
		'cc @' in df['comment_content'].iloc[i] or\
		"you'd have to contact" in df['comment_content'].iloc[i] or\
		'unrelated' in df['comment_content'].iloc[i] or\
		'ping @' in df['comment_content'].iloc[i] or\
		'this isn’t the right place to discuss this' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC4'
        else:
            df['Predicted_YY_label'].loc[i]='SC4'
              
    if 'thanks' in df['comment_content'].iloc[i] or\
         'thank you so much' in df['comment_content'].iloc[i] or\
         'tnx' in  df['comment_content'].iloc[i] or\
         'Thanks' in  df['comment_content'].iloc[i] or\
         'thank you' in  df['comment_content'].iloc[i] or\
         'thanks alot' in df['comment_content'].iloc[i] or\
         'It would be nice if' in df['comment_content'].iloc[i]: 
         if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC8'
         else:
            df['Predicted_YY_label'].loc[i]='SC8'
          
          
    if 'This issue can be closed' in df['comment_content'].iloc[i] or\
         'closing for now' in df['comment_content'].iloc[i] or\
         'I will close the issue' in  df['comment_content'].iloc[i] or\
         'closing this' in df['comment_content'].iloc[i] or\
		 'closing' in df['comment_content'].iloc[i] or\
         'confirmed fixed' in df['comment_content'].iloc[i] or\
		 'this was fixed' in df['comment_content'].iloc[i]: 
         if df['Predicted_YY_label'].loc[i] != '': 
                df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC7'
         else: 
                df['Predicted_YY_label'].loc[i]='SC7'
          
    if 'this is the reason why' in df['comment_content'].iloc[i] or\
         'i suspect' in df['comment_content'].iloc[i] or\
         'looks like' in  df['comment_content'].iloc[i] or\
         'because' in df['comment_content'].iloc[i] or\
         'i mean' in df['comment_content'].iloc[i] or\
         'is just' in df['comment_content'].iloc[i] or\
         'link to related material' in df['comment_content'].iloc[i] or\
         'nonsense' in df['comment_content'].iloc[i] or\
         'it was not my intention to' in df['comment_content'].iloc[i] or\
         'keep in mind that' in df['comment_content'].iloc[i] or\
         'Please note that' in df['comment_content'].iloc[i] or\
         'just to clarify' in df['comment_content'].iloc[i] or\
         'just to add' in df['comment_content'].iloc[i] or\
         'as far as I know' in df['comment_content'].iloc[i] or\
         'the motivation for this is' in df['comment_content'].iloc[i] or\
         "you're confusing" in df['comment_content'].iloc[i] or\
         'please note' in df['comment_content'].iloc[i] or\
         'i received the following error' in df['comment_content'].iloc[i] or\
         'please note' in df['comment_content'].iloc[i] or\
         'i received the following error' in df['comment_content'].iloc[i] or\
         'i was just' in df['comment_content'].iloc[i]:
         if df['Predicted_YY_label'].loc[i] != '': 
                df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC2'
         else: 
             df['Predicted_YY_label'].loc[i]='SC2'
          
    if 'yeah,' in df['comment_content'].iloc[i] or\
        'agree with' in df['comment_content'].iloc[i] or\
        'yes you are right' in df['comment_content'].iloc[i] or\
        'i also agree' in df['comment_content'].iloc[i] or\
        'sounds good' in df['comment_content'].iloc[i] or\
        'as pointed out by' in df['comment_content'].iloc[i] or\
        'yes,' in df['comment_content'].iloc[i] or\
        'Yes' in df['comment_content'].iloc[i] or\
        'indeed' in df['comment_content'].iloc[i] or\
        'i agree' in df['comment_content'].iloc[i] or\
        'seems like a good idea' in df['comment_content'].iloc[i] or\
        'exactly' in df['comment_content'].iloc[i] or\
        'that makes perfect sense' in df['comment_content'].iloc[i] or\
        'everything seems to be working great' in df['comment_content'].iloc[i] or\
        'yup' in df['comment_content'].iloc[i] or\
        'indeed' in df['comment_content'].iloc[i] or\
        'will check' in df['comment_content'].iloc[i] or\
        'ah okay' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
                df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC1'
        else:
             df['Predicted_YY_label'].loc[i]='SC1'   
        
        
    if 'what to do next' in df['comment_content'].iloc[i] or\
        'can you tell me' in df['comment_content'].iloc[i] or\
        'are you sure' in df['comment_content'].iloc[i] or\
        'how did' in df['comment_content'].iloc[i] or\
        'have you' in df['comment_content'].iloc[i] or\
        'can you elaborate on' in df['comment_content'].iloc[i] or\
        'let me know what' in df['comment_content'].iloc[i] or\
        'should I do' in df['comment_content'].iloc[i] or\
        'should I' in df['comment_content'].iloc[i] or\
        'can you' in df['comment_content'].iloc[i] or\
        'have you' in df['comment_content'].iloc[i] or\
        'right?' in df['comment_content'].iloc[i] or\
        'did you?' in df['comment_content'].iloc[i] or\
        'right?' in df['comment_content'].iloc[i] or\
        'can you tell me' in  df['comment_content'].iloc[i] or\
        'please let us know' in df['comment_content'].iloc[i] or\
        'sounds like a solution' in df['comment_content'].iloc[i] or\
        'great' in df['comment_content'].iloc[i] or\
        'sounds great' in df['comment_content'].iloc[i] or\
        'seems like a good idea' in df['comment_content'].iloc[i] or\
        'this error pops up' in df['comment_content'].iloc[i] or\
        'now giving me this error' in df['comment_content'].iloc[i] or\
        'sorry' in df['comment_content'].iloc[i] or\
        'apologizes' in df['comment_content'].iloc[i] or\
        'sorry' in df['comment_content'].iloc[i] or\
        'i was' in df['comment_content'].iloc[i] or\
        'i have made a mistake' in df['comment_content'].iloc[i] or\
        'here is the output' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'N'
        else:
            df['Predicted_YY_label'].loc[i]='N'
        
    if 'see #' in df['comment_content'].iloc[i] or\
        'please see' in df['comment_content'].iloc[i] or\
        'possible fix in' in df['comment_content'].iloc[i] or\
        'here is the' in df['comment_content'].iloc[i] or\
        'should be fixed by' in df['comment_content'].iloc[i]:
        df['Predicted_YY_label'].loc[i]='SC4'
        
            
    if 'i did notice' in df['comment_content'].iloc[i] or\
        'feedback' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC3'
        else:
            df['Predicted_YY_label'].loc[i]='SC3' 
        
    if 'could you' in df['comment_content'].iloc[i] or\
        'please' in df['comment_content'].iloc[i] or\
        'Please' in df['comment_content'].iloc[i] or\
        'reopen this issue please' in df['comment_content'].iloc[i] or\
        'please include' in df['comment_content'].iloc[i] or\
        'could you please' in df['comment_content'].iloc[i] or\
        'please review' in df['comment_content'].iloc[i] or\
        'can you specify' in df['comment_content'].iloc[i] or\
        'what you mean' in df['comment_content'].iloc[i] or\
        'could you post' in df['comment_content'].iloc[i] or\
        'can you provide' in df['comment_content'].iloc[i] or\
        'are you getting' in df['comment_content'].iloc[i] or\
        'can you point to'in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC6'
        else:
            df['Predicted_YY_label'].loc[i]='SC6'
        
            
    if 'i have the same issue' in df['comment_content'].iloc[i] or\
        'tried...crashes' in df['comment_content'].iloc[i] or\
        'confirmed that the issuse still exists' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC9'
        else: 
            df['Predicted_YY_label'].loc[i]='SC9'
            
    if 'i would like to take a stab at this' in df['comment_content'].iloc[i] or\
        "i'll see if i can help" in df['comment_content'].iloc[i] or\
        'i will prepare' in df['comment_content'].iloc[i] or\
        'will open a pr' in df['comment_content'].iloc[i] or\
        'work on a pr' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'SC5'
        else: 
            df['Predicted_YY_label'].loc[i]='SC5'
            
    if 'as time permits' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'PA8'
        else: 
            df['Predicted_YY_label'].loc[i]='PA8'    
            
    if 'still not fixed' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'MA1'
        else: 
            df['Predicted_YY_label'].loc[i]='MA1'
 
    if 'i am happy with that fallback' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'CH1'
        else: 
            df['Predicted_YY_label'].loc[i]='CH1'
            
    if 'this seems urgent' in df['comment_content'].iloc[i] or\
        'sounds like a serious problem' in df['comment_content'].iloc[i] or\
        'this is worse than' in df['comment_content'].iloc[i] or\
        'reopen the issue,' in df['comment_content'].iloc[i] or\
        'could you re-open' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'CH12'
        else: 
            df['Predicted_YY_label'].loc[i]='CH12' 
            
    if 'alternative' in df['comment_content'].iloc[i] or\
        'you probably want' in df['comment_content'].iloc[i] or\
        'i feel' in df['comment_content'].iloc[i] or\
        'choose one of these' in df['comment_content'].iloc[i] or\
        'other ways' in df['comment_content'].iloc[i] or\
        'suppose that' in df['comment_content'].iloc[i] or\
        'a simpler way' in df['comment_content'].iloc[i] or\
        'if...if' in df['comment_content'].iloc[i] or\
        'one way' in df['comment_content'].iloc[i] or\
        'on the other hand' in df['comment_content'].iloc[i] or\
        'in current case' in df['comment_content'].iloc[i] or\
        'there are cases' in df['comment_content'].iloc[i] or\
        "that's assuming" in df['comment_content'].iloc[i] or\
        'a simpler way' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'IS1'
        else: 
            df['Predicted_YY_label'].loc[i]='IS1' 
    if 'do we want to do that?' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'IS2'
        else: 
            df['Predicted_YY_label'].loc[i]='IS2'
                
    elif 'i feel' in df['comment_content'].iloc[i] or\
        'i think' in df['comment_content'].iloc[i] or\
        'may be it was a' in df['comment_content'].iloc[i] or\
        'in my opinion' in df['comment_content'].iloc[i] or\
        'i believe' in df['comment_content'].iloc[i] or\
        'here is the snippet' in df['comment_content'].iloc[i] or\
        'for eg' in df['comment_content'].iloc[i] or\
        'for example' in df['comment_content'].iloc[i]:
        if df['Predicted_YY_label'].loc[i] != '': 
            df['Predicted_YY_label'].loc[i]=df['Predicted_YY_label'].loc[i]+', '+'IS1-IS4'
        else:
            df['Predicted_YY_label'].loc[i]='IS1-IS4'

        
#total number of counts        
df.groupby(['Predicted_YY_label'])['comment_content'].count()

#
df.to_csv(r'C:\New_partition\Dr_Yang\\Doc\label_closed_comments_yy.csv')
         