# 🔐 Database Management Task
## Description

This project is a database management utility that includes features for converting PDF files to images and extracting data from MS Word files to Excel sheets. It is designed to streamline document processing tasks

## Technologies Used
- Python: Core programming language for scripting
- Excel: For storing extracted data in a structured format
- MS Word: For reading and processing document content.

## Libraries
- pdf2image: For converting PDF pages to images.
- python-docx: For reading MS Word files.
- pandas: For handling data and exporting to Excel.

  
⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


## 📁 Installation
```
Clone the repository:
git clone <repository-url>
cd <repository-folder>
Create a virtual environment:
```

```
python -m venv venv
venv\Scripts\activate
```

``` 
pip install -r requirements.txt
```

``` 
Run the Scripts file 
```



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📄 PDF to Image Conversion Script
This script converts specific pages of a PDF file into JPEG images.

- pdf.py
```

from pdf2image import convert_from_path
from pathlib import Path

base_dir = Path(__file__).resolve().parent

pdf_path = f"{base_dir}/demo.pdf"

images = convert_from_path(pdf_path=pdf_path,first_page=25 , last_page=50)

# print(images)
for i, image in enumerate(images,start=25):
    image.save(f"page_{i+1}.jpg", "JPEG")

print("25 to 50 page create image successfully")
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


# 📑 Insert Data from MS Word to Excel Sheet
This script extracts data from an MS Word file and inserts it into an Excel sheet.

- excel.py
```

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

```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 🛠️ Requirements

```
pdf2image
python3-docx
pandas
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
