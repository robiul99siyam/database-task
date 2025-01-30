# 🔐 Database Management Task
## Description
This task is a Database management . It includes features for pdt to convert image, ms word file to convert excel file
## Technologies Used
- Python , excel, ms word

  
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
``` pip install -r requirements.txt ```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# Create Pdf To Image convert Scripts

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
