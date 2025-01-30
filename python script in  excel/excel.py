# import the module 
from docx import Document
import pandas as pd
import re


docx = Document("data.docx")


text_value = []

for value in docx.paragraphs:
    text = value.text.strip()

    match = re.match(r"\[(\d+)\]\s*(.*)",text)

    if match:
        Value_id = match.group(1)
        Value_content =  match.group(2).strip()

        text_value.append([Value_id,Value_content])


df = pd.DataFrame(text_value,columns=['ID',"CONTENT"])
df.to_excel("hadis.xlsx",index=False)