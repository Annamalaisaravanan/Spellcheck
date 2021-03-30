import pandas as pd
from spellchecker import SpellChecker
import operator
spell=SpellChecker()
spell.word_frequency.load_text_file('path/to/the/required/word/files')
code_data=pd.read_csv("path/to/the/dataset/csv format")
faa_data=code_data["faa"].unique()
country_code=code_data["CountryCode"].unique()
user_in=input()
print(user_in)

lis=user_in.split(" ")

for i,j in enumerate(lis):
    if j in faa_data:
        num_data={"airport_name":str(list(set(code_data.loc[code_data["faa"]==j,"name"]))),"city":str(list(set(code_data.loc[code_data["faa"]==j,"city"]))),"StateCode":str(list(set(code_data.loc[code_data["faa"]==j,"StateCode"]))),"CountryCode":str(list(set(code_data.loc[code_data["faa"]==j,"CountryCode"]))),"CountryName":str(list(set(code_data.loc[code_data["faa"]==j,"CountryName"])))}
        lis[i]=num_data["airport_name"]
    elif j in country_code:
        num_data={"airport_name":str(list(set(code_data.loc[code_data["CountryCode"]==j,"name"]))),"city":str(list(set(code_data.loc[code_data["CountryCode"]==j,"city"]))),"StateCode":str(list(set(code_data.loc[code_data["CountryCode"]==j,"StateCode"]))),"faa":str(list(set(code_data.loc[code_data["CountryCode"]==j,"faa"]))),"CountryName":str(list(set(code_data.loc[code_data["CountryCode"]==j,"CountryName"])))}
        lis[i]=num_data["CountryName"]
    else:
          
        o=process.extract(query=j,choices=h['city'].values.tolist(),limit=7)
        pair=dict()
        pair.clear()
        for i in o:
            l=fuzz.ratio(i[0].lower(),j.lower())
            
            if l>50:
                
                
                pair[i[0]]=int(l)
            else:
                pass
        sorted_list=dict(sorted(pair.items(),key=operator.itemgetter(1),reverse=True))
        sorted_list=list(sorted_list.items())
        lis[i]=sorted_list[0][0]
print(" ".join(lis))

