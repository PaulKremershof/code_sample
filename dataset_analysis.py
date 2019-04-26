
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import csv


# In[3]:


df = pd.read_csv('Set_1.csv', sep='\t')


# In[4]:


df = df[(df["cont_v_tense"] == "present") & (df["compl_v_tense"] == "present")]


# In[4]:


#df = df[(df["compl_v_per"] == 3.0) ]
#df = df[(df["cont_v_per"] == 3.0) ]
df = df[(df["compl_cat"] == "suj") ]


# In[6]:


SUJ = df[(df["cont_cat"] == "suj")]


# In[7]:


OBJ = df[(df["cont_cat"] == "obj")]


# In[8]:


SPEC = df[(df["entityref"] == "spec")]


# In[9]:


NE = df[(df["entityref"] == "ne")]


# In[10]:


NULL = df[(df["compl_type"] == "null")]


# In[11]:


NP = df[(df["compl_type"] == "NP")]


# In[12]:


#Taking the strongest biased verbs that occur BOTH in the 720 verb list 
#and in forms part of the complete set.

ICV_obj = ["optar", "descartar", "assignar", "confiar", "escollir", "condemnar", "acusar", "preferir",            "agradar", "amagar", "colpejar", "denunciar", "prohibir", "respectar", "sortir", "voler", "encarregar",            "matar", "criticar", "contractar", "detenir", "esmentar", "estrenar", "incloure", "injectar"]


# In[13]:


lst = []
b = {}
with open('Set_1.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        lst.append(row[11])
    for item in lst:
        b[item] = b.get(item, 0) + 1
        


# In[14]:


ICV2 = df[df["cont_verb"].isin(ICV_obj)]


# In[15]:


ICV2.to_csv("ICV2_set.csv", sep='\t', encoding='utf-8', index=False)


# In[16]:


IVC_two = {}
lste = []

with open('ICV2_set.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        lste.append(row[11])
    for item in lste:
        IVC_two[item] = IVC_two.get(item, 0) + 1


# In[17]:


print(IVC_two)


# In[18]:


ICV_suj = ["superar", "preocupar,", "afectar", "beneficiar", "controlar", "rebre", "crear", "localitzar", "recuperar",           "valorar", "assegurar", "estimar", "dominar", "patir", "curar", "portar", "transformar", "confirmar","entendre", "suposar",           "aconseguir", "convertir", "escapar", "dissenyar", "fallar"]


# In[19]:


ICV1 = df[df["cont_verb"].isin(ICV_suj)]


# In[20]:


ICV1.to_csv("ICV1_set.csv", sep='\t', encoding='utf-8', index=False)


# In[21]:


IVC_two = {}
lste = []

with open('ICV1_set.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        lste.append(row[11])
    for item in lste:
        IVC_two[item] = IVC_two.get(item, 0) + 1


# In[22]:


print(IVC_two)
len(IVC_two)


# In[23]:


ICV1 = []
t = list(b.items())
for k,v in t:
    for verb in ICV_suj:
       # print(verb)
        try:
            if verb in k:
                print(k,v)
        except: pass
         #   


# In[5]:


TPV_1 =  ['portar', 'passar', 'entregar', 'enviar', 'donar', 'regalar', 'servir', 'retornar', 'proporcionar', 'vendre',         'portar', 'cedir', 'deixar', 'acostar', 'facilitar',' subministrar']


# In[6]:


TPV1 = df[df["cont_verb"].isin(TPV_1)]


# In[7]:


TPV1.to_csv("TPV1_set.csv", sep='\t', encoding='utf-8', index=False)


# In[9]:


pd.crosstab(TPV1["cont_cat"], TPV1["compl_type"], margins=True, normalize=True)


# In[10]:


pd.crosstab(TPV1["cont_cat"], TPV1["compl_type"], margins=True)


# In[11]:


TPV_one = {}
lste = []

with open('TPV1_set.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        lste.append(row[11])
    for item in lste:
        TPV_one[item] = TPV_one.get(item, 0) + 1


# In[12]:


print(TPV_one)


# In[13]:


TPV_2 = ['agafar', 'obtenir', 'adquirir', 'agafar', 'prendre',' rebre', 'recollir', 'admetre', 'comprar']


# In[14]:


TPV2 = df[df["cont_verb"].isin(TPV_2)]


# In[15]:


TPV2.to_csv("TPV2_set.csv", sep='\t', encoding='utf-8', index=False)


# In[16]:


pd.crosstab(TPV2["cont_cat"], TPV2["compl_type"], margins=True)


# In[34]:


TPV_two = {}
lste = []

with open('TPV2_set.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        lste.append(row[11])
    for item in lste:
        TPV_two[item] = TPV_two.get(item, 0) + 1


# In[35]:


print(TPV_two)


# In[36]:


df.compl_type.value_counts()


# In[37]:


pd.crosstab(df["cont_cat"], df["compl_type"], margins=True, normalize=True)


# In[38]:


pd.crosstab(df["cont_cat"], df["compl_type"], margins=True)


# In[39]:


pd.crosstab(df["cont_cat"], df["entityref"], margins=True)


# In[40]:


pd.crosstab(df["cont_cat"], df["entityref"], margins=True, normalize=True)


# In[41]:


pd.crosstab(ICV1["cont_cat"], ICV1["compl_type"], margins=True, normalize=True)


# In[ ]:


pd.crosstab(ICV1["cont_cat"], ICV1["compl_type"], margins=True)


# In[ ]:


pd.crosstab(ICV2["cont_cat"], ICV2["compl_type"], margins=True, normalize=True)


# In[ ]:


pd.crosstab(ICV2["cont_cat"], ICV2["compl_type"], margins=True)


# In[ ]:


pd.crosstab(ICV1["cont_cat"], ICV1["entityref"], margins=True, normalize=True)


# In[ ]:


pd.crosstab(ICV2["cont_cat"], ICV2["entityref"], margins=True, normalize=True)


# In[ ]:


sns.countplot(x="cont_cat", data=ICV1, palette="hls")
plt.show()
plt.savefig("countplot")


# In[ ]:


#complete dataframe 
#(a/b)
null_counts = df.compl_type.value_counts()["null"]
compl_type_counts = sum(df.compl_type.value_counts())

#c/d
null_freq_in_suj = df.groupby("cont_cat")['compl_type'].value_counts()["suj"]["null"]
compl_type_in_suj = sum(df.groupby("cont_cat")['compl_type'].value_counts()["suj"])

#e/f
suj_counts = df.cont_cat.value_counts()["suj"]
total_cat_counts = sum(df.cont_cat.value_counts())


# In[ ]:


#ICV1
null_counts1 = ICV1.compl_type.value_counts()["null"]
compl_type_counts1 = sum(ICV1.compl_type.value_counts())

#c/d
null_freq_in_suj1 = ICV1.groupby("cont_cat")['compl_type'].value_counts()["suj"]["null"]
compl_type_in_suj1 = sum(ICV1.groupby("cont_cat")['compl_type'].value_counts()["suj"])

#e/f
suj_counts1 = ICV1.cont_cat.value_counts()["suj"]
total_cat_counts1 = sum(ICV1.cont_cat.value_counts())


# In[ ]:


#ICV2
null_counts2 = ICV2.compl_type.value_counts()["null"]
compl_type_counts2 = sum(ICV2.compl_type.value_counts())

#c/d
null_freq_in_suj2 = ICV2.groupby("cont_cat")['compl_type'].value_counts()["suj"]["null"]
compl_type_in_suj2 = sum(ICV2.groupby("cont_cat")['compl_type'].value_counts()["suj"])

#e/f
suj_counts2 = ICV2.cont_cat.value_counts()["suj"]
total_cat_counts2 = sum(ICV2.cont_cat.value_counts())


# In[ ]:


#Bayes function
#1. P(null)
#2. p(null/suj)
#3. p(suj)
#4. p(suj/null) = P(null/suj) * P(suj)/P(null)

def expectancy_model(a,b,c,d,e,f):
    p_anaphora = float(a) / b
    p_anaphora_cat = float(c) / d
    p_cat = float(e) / f
    p_cat_anaphora = p_anaphora_cat * p_cat / p_anaphora 
    return(p_anaphora, p_anaphora_cat, p_cat, p_cat_anaphora)


# In[ ]:


#DF Results of Bayes Function; in  order 1 - 4
#According to Stevenson et al. (1994)... occurrence of a pronoun (or null) contributes to a subject bias
#though the difference is very slight:
#Also, the production bias is also reflected here. Pronouns are the prefered way to refer to subjects
#We find a weak product bias towards pronominalizing subjects
expectancy_model(null_counts,compl_type_counts,null_freq_in_suj,compl_type_in_suj,suj_counts,total_cat_counts)


# In[ ]:


#ICV1 Results of Bayes Function; in  order 1 - 4
#choosing ICV verbs the occurrence of a pronoun has greater impact on the subject bias:
#this form-specific "bottom-up" subject bias works in concert with but independently with the contextually
#driven, top-down thematic role bias (ICV)
expectancy_model(null_counts1,compl_type_counts1,null_freq_in_suj1,compl_type_in_suj1,suj_counts1,total_cat_counts1)


# In[ ]:


#ICV2 Results of Bayes Function; in  order 1 - 4
expectancy_model(null_counts2,compl_type_counts2,null_freq_in_suj2,compl_type_in_suj2,suj_counts2,total_cat_counts2)


# In[ ]:


df['cont_count'].mean()


# In[ ]:


df["compl_count"].mean()


# In[ ]:


df["cont_entity_freq"].mean()


# In[ ]:


ICV1["cont_entity_freq"].mean()


# In[ ]:


ICV2["cont_entity_freq"].mean()


# In[ ]:


df.cont_cat.value_counts()


# In[ ]:


df.groupby("cont_cat")["cont_entity_freq"].mean()


# In[ ]:


df.groupby("entityref")["cont_entity_freq"].mean()


# In[ ]:


df.groupby("cont_cat")["cont_count"].mean()


# In[ ]:


df.groupby("cont_cat")["compl_count"].mean()


# In[ ]:


df.groupby("entityref")["cont_count"].mean()


# In[ ]:


df.groupby("entityref")["compl_count"].mean()


# In[ ]:


df.groupby("compl_type")["compl_count"].mean()


# In[ ]:


df.groupby("compl_type")["cont_count"].mean()


# In[ ]:


df.groupby("compl_type")["cont_entity_freq"].mean()


# In[ ]:


#There is no difference in the completion type between NE and SPEC (NP 42% / NULL 55%)
pd.crosstab(NE["cont_cat"], NE["compl_type"], margins=True, normalize=True)


# In[ ]:


#SPEC antecedents are more likely to be objects (38%) than NE antecedents (7%)
pd.crosstab(SPEC["cont_cat"], SPEC["compl_type"], margins=True, normalize=True)


# In[ ]:


pd.crosstab(NE["cont_cat"], NE["compl_type"], margins=True)


# In[ ]:


pd.crosstab(SPEC["cont_cat"], SPEC["compl_type"], margins=True)


# In[ ]:


#SPEC antecedents that have an NP referring expression are slighlty longer (39 tokens) 
#than NE with NP completion type (32 tokens)
SPEC.groupby("compl_type")["cont_count"].mean()


# In[ ]:


NE.groupby("compl_type")["cont_count"].mean()


# In[ ]:


#Especially SPEC object mentions are longer than NE objects 
SPEC.groupby("cont_cat")["cont_count"].mean()


# In[ ]:


NE.groupby("cont_cat")["cont_count"].mean()


# In[ ]:


#When an ENTITY has an object position, it is generally a very salient entity (with many mentions)

SPEC.groupby("cont_cat")["cont_entity_freq"].mean()


# In[ ]:


NE.groupby("cont_cat")["cont_entity_freq"].mean()


# In[ ]:


#SPEC context sentences are slightly longer than NE context sentences
SPEC["cont_count"].mean()


# In[ ]:


NE["cont_count"].mean()


# In[ ]:


#Not so the completion sentences
SPEC["compl_count"].mean()


# In[ ]:


NE["compl_count"].mean()


# In[ ]:


#Similar to the context length, SPEC NP completion sentences are slightly longer than
#NE NP completion sentences
SPEC.groupby("compl_type")["compl_count"].mean()


# In[ ]:


NE.groupby("compl_type")["compl_count"].mean()


# In[ ]:


#Repeated mention theory: entities that have been focused on in the prior discourse 
#are more likely to be focused on in subsequent discourse, and hence references to 
#them are more likely to be pronominalized. 
#Also fits the Accessibility Theory (Ariel 2011) ????
#more marked, informative forms tend to retrieve less salient antecedents, 
#while unmarked, less informative forms tend to retrieve more salient antecedents. 
NULL.groupby("cont_cat")["cont_entity_freq"].mean()


# In[ ]:


#this data also supports the hypothesis rather Topics than Subjects are being pronominalized. We could say
#that higher occurrence rates of entites indicate a stronger topic and therefor are more used in null pronouns
NP.groupby("cont_cat")["cont_entity_freq"].mean()


# In[ ]:


NULL["cont_cat"].value_counts()


# In[ ]:


NP["cont_cat"].value_counts()


# In[ ]:


pd.crosstab(NULL["cont_cat"], NULL["entityref"], margins=True, normalize=True)


# In[ ]:


pd.crosstab(NP["cont_cat"], NP["entityref"], margins=True, normalize=True)


# In[ ]:


ICV2.groupby("compl_type")['cont_cat'].value_counts()


# In[ ]:


NP["compl_count"].mean()


# In[ ]:


NULL["compl_count"].mean()


# In[ ]:


NP["cont_count"].mean()


# In[ ]:


NULL["cont_count"].mean()


# In[ ]:


df.groupby("cont_cat")["cont_entity_freq"].mean()


# In[ ]:


df.groupby("compl_type")["cont_entity_freq"].mean()

