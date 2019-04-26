# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:31:07 2018

@author: paul_
"""


from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
import re
import glob

files = glob.glob(r'C:\Users\paul_\OneDrive\Documentos\TFM\Data\Data\2\tests/*.xml')



def run_for_one_file(f):    
    url = open(f, encoding="utf-8")

    soup = BeautifulSoup(url, 'lxml')
    
    
    items = soup.find_all('sentence')
    for index,items in enumerate(items):
        items['idd'] = str(index)   
    
    
    sentence_idd = []
    prev_sent_id = []
    entity_number = []
    context_sentence = []
    sentence_length = []
    sentence2length = []
    completion_sentence = []
    
    antecedent_noun = []
    antecedent_entityref = []
    antecedent_entity = []
    antecedent_category = []
    named_entity = []
    numerus_noun = []
    gender_noun = []
    satz_id = []
    prev_person = []
    prev_number = []
    prev_tense = []
    fst_v = []
    snd_v = []
    trd_v = []
    theta_role = []

    
    anaphora_id = []
    anaphora_entity = []
    anaphora_category = []
    anaphora_aux = []
    anaphora_v = []
    anaphora_inf = []
    anaphora_pronoun = []
    anaphora_number = []
    anaphora_gender = []
    anaphora_tense = []
    anaph_person = []
    anaph_number = []
    anaphora_det = []
    anaphora_type = []
    
    
    for item in soup.find_all("sn", { "entityref" : "spec" }, {"func" : "suj"}):
        entity_num = item.get('entity')
        if entity_num not in entity_number:
            entity_number.append(entity_num)
        sentence = item.find_previous('sentence')
        sentence_id = sentence['idd']
        sentence_idd.append(sentence_id)
        for item in soup.find_all('sentence', idd=int(sentence_id) - 1):
            sn = item.find_all("sn", entity=entity_number, elliptic=False)
            prev_sentence_id = item['idd']
            if prev_sentence_id not in prev_sent_id:
                prev_sent_id.append(prev_sentence_id)   
    
    
    entdict = []
    entlst = []
    b = {}
    for entity in soup.find_all("sn", entity=entity_number):
        entity = entity.get('entity')
        entlst.append(entity)           
    for item in entlst:
        b[item] = b.get(item, 0) + 1
        
             
    for item in soup.find_all('sentence', idd=prev_sent_id):      
        for sn in item.find_all("sn", entity=entity_number, elliptic=False):
            if sn.get('func') == "suj"  or sn.get('func') == "cd" or sn.get('func') == "ci":
                satz = str(item)
                words = re.findall(r'wd="(\w*)', satz)
                if len(words) > 0:
                    context_sentence.append(words)
                    sentence_length.append(len(words))
                category = sn.get('func')
                antecedent_category.append(category)
                entidad = sn.get('entity')
                antecedent_entity.append(entidad)
                entityref = sn.get('entityref')
                namedentity = sn.get("ne")
                named_entity.append(namedentity)
                antecedent_entityref.append(entityref)
                groupnom = sn.find_next('grup.nom')
                numerus = groupnom.get('num')
                numerus_noun.append(numerus)
                gender = groupnom.get('gen')
                gender_noun.append(gender)
                satzid = sn.find_previous('sentence')
                satz_idd = satzid.get('idd')
                satz_id.append(satz_idd)
                noun_node = groupnom.find('n') or groupnom.find('p')
                lemma_n = noun_node.get('lem')
                print(lemma_n)
                antecedent_noun.append(lemma_n)
            else:
                sn.get('func') == None
                try:
                    prev_sn = sn.find_parent("sn")
                    if prev_sn.get('entity') == entidad: 
                        continue
                except: pass
                sp = sn.find_previous("sp")
                if sp.get("func") != "creg" and sp.get("func") != "cc" and sp.get("func") != "ci": continue
                satz = str(item)
                words = re.findall(r'wd="(\w*)', satz)
                if len(words) > 0:
                    context_sentence.append(words)
                    sentence_length.append(len(words))
                category = sp.get('func')
                antecedent_category.append(category)
                entidad = sn.get('entity')
                antecedent_entity.append(entidad)
                entityref = sn.get('entityref')
                namedentity = sn.get("ne")
                named_entity.append(namedentity)
                antecedent_entityref.append(entityref)
                groupnom = sn.find_next('grup.nom')
                numerus = groupnom.get('num')
                numerus_noun.append(numerus)
                gender = groupnom.get('gen')
                gender_noun.append(gender)
                satzid = sn.find_previous('sentence')
                satz_idd = satzid.get('idd')
                satz_id.append(satz_idd)
                noun_node = groupnom.find('n') or groupnom.find('p')
                lemma_n = noun_node.get('lem')
                antecedent_noun.append(lemma_n)
            if sn.get('func') == "suj":
                VP = sn.find_next('grup.verb') 
            elif noun_node.get("case") == "accusative" and sn.get('func') == "cd":
                VP = sn.find_next('grup.verb')
            else:
                sn.get('func') == "cd" or sn.get('func') == "ci" or sp.get("func") == "creg" or sp.get("func") == "cc" or sp.get("func") == "ci"
                VP = noun_node.find_previous('grup.verb')
            for v in VP.find_all('v'):
              #  print(v)
                if v["mood"] == "indicative" or v["mood"] == "subjunctive": 
                    prevnum = v["num"]
                    prevper = v["person"]
                    prevtense = v["tense"]
                    prev_person.append(prevper)
                    prev_number.append(prevnum)
                    prev_tense.append(prevtense)
                    if v["postype"] == "auxiliary":
                        prevauxwd = v["lem"]
                        fst_v.append(prevauxwd)
                        nextv = v.find_next_sibling("v")
                        findde = v.find_next_sibling("s")
                        try:
                            if findde != None:
                                fstinfin = v.find_next_sibling("infinitiu")
                                fstinf = fstinfin.find_next("v")
                                infwd = fstinf["lem"]
                                snd_v.append(infwd)
                                trd_v.append("")
                                try:
                                    thetapart = fstinf["lss"]
                                    theta_role.append(thetapart)
                                except: pass
                            elif nextv["postype"] == "semiauxiliary":
                                nextv = nextv["lem"]
                                snd_v.append(nextv)
                                trd_v.append("")
                            elif nextv["postype"] == "main":
                                nextwd = nextv['lem']
                                snd_v.append(nextwd)
                                trd_v.append("")
                                try:
                                    thetapartII = nextv["lss"]
                                    theta_role.append(thetapartII)
                                except: pass
                            elif nextv["postype"] != "main":
                                nextnextv = nextv.find_next_sibling("v")
                                if nextnextv != None:
                                    nextnextwd = nextnextv["lem"]
                                    snd_v.append(nextnextwd)
                                    trd_v.append("")
                                    try:
                                        thetaIV = nextnextv["lss"]
                                        theta_role.append(thetaIV)
                                    except: pass
                            elif nextv["postype"] == "main":
                                infinitive = nextv.find_next_sibling("infinitiu")
                                if infinitive != None:
                                    infv = infinitive.find_next("v")
                                    infwd = infv["lem"]
                                    trd_v.append(infwd)
                                    try:
                                        thetaV = infv["lss"]
                                        theta_role.append(thetaV)
                                    except: pass
                                else: trd_v.append("")
                                    
                        except:
                            pass
                    elif v["postype"] == "semiauxiliary":
                        prevsemiaux = v["lem"]
                        try:
                            thetasemi = v["lss"]
                            theta_role.append(thetasemi)
                        except: pass
                        snd_v.append(prevsemiaux)
                        fst_v.append("")
                        trd_v.append("")
                    elif v["postype"] == "main":
                        prevmain = v["lem"]
                        fst_v.append("")
                        snd_v.append(prevmain)
                        try:
                            thetamain = v["lss"]
                            theta_role.append(thetamain)
                        except: pass
                        proxv = v.find_next_sibling('infinitiu')
                        try:
                            if proxv != None:
                                inf = proxv.find("v")
                                infini = inf["lem"]
                                trd_v.append(infini)
                                theta_inf = inf["lss"]
                                theta_role.append(theta_inf)
                            else:
                                trd_v.append("")
                        except: pass   
            else: pass               
    

    for entt in antecedent_entity:
        entdict.append(b[entt])
    
    for num in satz_id:
        ID = num
        for item in soup.find_all('sentence', idd=int(ID) + 1):
            sen_id = item['idd'] 
            anaphora_id.append(sen_id)
            anaph = item.find("sn", entity=entity_number, entityref="spec")
            anaph_entity = anaph.get('entity')
            anaphora_entity.append(anaph_entity)
            anaph_cat = anaph.get('func')
            anaph_noun = anaph.find_next("n")
            anaphora_category.append(anaph_cat)
            satz2 = str(soup.find_all('sentence', idd=sen_id))
            wds = re.findall(r'wd="(\w*)', satz2)
            if len(wds) > 0:
                sentence2length.append(len(wds))
                completion_sentence.append(wds)
            if anaph.get('func') == "suj":
                verbo = anaph_noun.find_next('grup.verb') 
            else:
                anaph.get('func') == "cd" or anaph.get('func') == "ci"
                verbo = anaph_noun.find_previous('grup.verb')
            for vb in verbo.find_all('v'):
                if vb["mood"] == "indicative" or vb["mood"] == "subjunctive": 
                    num = vb["num"]
                    per = vb["person"]
                    tense = vb["tense"]
                    anaph_person.append(per)
                    anaph_number.append(num),
                    anaphora_tense.append(tense)
                    if vb["postype"] == "auxiliary":
                        auxwd = vb["lem"]
                        anaphora_aux.append(auxwd)
                        nextv = vb.find_next_sibling("v")
                        findde = vb.find_next_sibling("s")
                        try:
                            if findde != None:
                                fstinfin = vb.find_next_sibling("infinitiu")
                                fstinf = fstinfin.find_next("v")
                                infwd = fstinf["lem"]
                                anaphora_v.append(infwd)
                                anaphora_inf.append("")
                            elif nextv["postype"] == "main":
                                nextwd = nextv['lem']
                                anaphora_v.append(nextwd)
                                anaphora_inf.append("")
                            elif nextv["postype"] != "main":
                                nextnextv = nextv.find_next_sibling("v")
                                if nextnextv != None:
                                    nextnextwd = nextnextv["lem"]
                                    anaphora_v.append(nextnextwd)
                                    anaphora_inf.append("")
                            elif nextv["postype"] == "main":
                                infinitive = nextv.find_next_sibling("infinitiu")
                                if infinitive != None:
                                    infv = infinitive.find_next("v")
                                    infwd = infv["lem"]
                                    anaphora_inf.append(infwd)
                                else: anaphora_inf.append("")
                        except:
                            pass
                    elif vb["postype"] == "semiauxiliary":
                        semiaux = vb["lem"]
                        anaphora_v.append(semiaux)
                        anaphora_aux.append("")
                        anaphora_inf.append("")
                    elif vb["postype"] == "main":
                        main = vb["lem"]
                        anaphora_aux.append("")
                        anaphora_v.append(main)
                        proxv = vb.find_next_sibling('infinitiu')
                        try:
                            if proxv != None:
                                inf = proxv.find("v")
                                infini = inf["lem"]
                                anaphora_inf.append(infini)
                            else:
                                anaphora_inf.append("")
                        except: pass
            
            try:
                if anaph.get('elliptic') == "yes":
                     anaphora_pronoun.append("elliptic")    
                     anaphora_number.append("")
                     anaphora_gender.append("")
                     anaphora_type.append("null")
                else:
                    if anaph.get('elliptic') != "yes":
                       grupnom = anaph.find_next('grup.nom')
                       noun = grupnom.find('n')
                       pronoun = grupnom.find('p')
                       demonstrative = grupnom.find('d')
                       determiner = anaph.find_next('spec')
                       det = determiner.find_next('d')
                       if noun != None:
                           noun_lem = noun['lem']
                           noun_num = noun['num']
                           noun_gen = noun['gen']
                           anaphora_pronoun.append(noun_lem) 
                           anaphora_number.append(noun_num)
                           anaphora_gender.append(noun_gen)
                       elif noun == None and pronoun == None:
                           det_wd = demonstrative['lem']
                           anaphora_pronoun.append(det_wd)
                           anaphora_number.append(noun_num)
                           anaphora_gender.append(noun_gen)
                           anaphora_type.append('demonstrative')
                       else:
                           if pronoun != None:
                               pronoun_lem = pronoun['lem']
                               anaphora_pronoun.append(pronoun_lem)
                               anaphora_type.append('pronoun')
                if anaph.get('elliptic') != "yes" and noun != None:
                   determiner = anaph.find('spec')
                   if determiner != None: 
                       det_wd = det['lem']
                       anaphora_det.append(det_wd)
                       anaphora_type.append('NP')
                   else:
                       anaphora_det.append("")
                       anaphora_type.append('named entity')
                else:
                   anaphora_det.append("")
                           
            except: pass



        
    d = [satz_id, sentence_length, antecedent_noun, gender_noun, numerus_noun, antecedent_category, \
         antecedent_entityref, antecedent_entity, named_entity, entdict, fst_v, snd_v, \
         trd_v, prev_number, prev_person, prev_tense, theta_role, anaphora_id, sentence2length, \
         anaphora_det, anaphora_pronoun, anaphora_gender, anaphora_number,\
         anaphora_category, anaphora_type, anaphora_entity, \
         anaphora_aux, anaphora_v, anaphora_inf, anaph_number, anaph_person, \
         anaphora_tense, context_sentence, completion_sentence] 
    export_data = zip_longest(*d, fillvalue = '')          
    with open("3.csv", 'a',encoding="utf-8", newline='') as f:
        writer = csv.writer(f, delimiter='\t')
       writer.writerow(("cont_id", "cont_count", "cont_noun", "cont_n_gen", "cont_n_num", \
                        "cont_cat", "entityref", "cont_entity", "NE","cont_entity_freq", "cont_aux", "cont_verb",\
                        "cont_inf", "cont_v_num", "cont_v_per", "cont_v_tense", "theta_role", \
                        "compl_id", "compl_count", "compl_det", "anaphora", "compl_gen", \
                        "compl_num", "compl_cat", "compl_type", "compl_entity", "compl_aux",\
                        "compl_verb", "compl_inf", "compl_v_num", "compl_v_per", "compl_v_tense",\
                        "cont_sentence", "compl_sentence"))
        writer.writerows(export_data)
    f.close()                       

for f in files:
    print("running for {0}".format(f))
    try:
        run_for_one_file(f)
    except:
        pass
                
    
    
