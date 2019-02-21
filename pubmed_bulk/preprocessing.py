import xml.etree.ElementTree as ET
import pandas as pd
import os

def find_all_text(element):
    txt = ''
    sub_element = list(element.iter())
    for s in sub_element:
        if s.text and s.tail:
            txt += (s.text.strip('\n') + s.tail.strip('\n'))
    return txt

raw_dir = 'raw_data/'
out_dir = 'csv_files/'

for f in os.listdir(raw_dir):
    tree = ET.parse(raw_dir+f)
    root = tree.getroot()
    
    sample_df = pd.DataFrame(columns=["PMID", "Title", "Keywords","Abstracts"])
    for arti in root:
        try:
            pmid = arti.findall('MedlineCitation')[0].findall('PMID')[0].text
            title_element = arti.findall('MedlineCitation')[0].findall('Article')[0].findall('ArticleTitle')[0]
            abst_element = arti.findall('MedlineCitation')[0].findall('Article')[0].\
                findall('Abstract')[0].findall('AbstractText')[0]
            title = find_all_text(title_element)
            abst = find_all_text(abst_element)
        except:
            continue
        try:
            kws = ', '.join([i.text for i in arti.findall('MedlineCitation')[0].\
                             findall('KeywordList')[0].findall('Keyword')])
        except:
            kws = ''
        d = {
            "PMID": pmid,
            "Title": title,
            "Keywords": kws,
            "Abstracts": abst
        }
        sample_df = sample_df.append(d, ignore_index=True)
        d = {}
        
    sample_df.to_csv(out_dir+f , sep='\t')