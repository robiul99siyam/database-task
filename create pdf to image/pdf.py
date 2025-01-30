from pdf2image import convert_from_path
popular_path = r"C:\\Users\\This PC\\Desktop\\development file\\pdf convert\\create pdf\\Release-24.08.0-0\\poppler-24.08.0\\Library\\bin"

pdf_path = "C:/Users/This PC/Desktop/development file/pdf convert/create pdf/demo.pdf"

images = convert_from_path(poppler_path=popular_path,pdf_path=pdf_path,first_page=25 , last_page=50)

# print(images)
for i, image in enumerate(images,start=25):
    image.save(f"page_{i+1}.jpg", "JPEG")

print("25 to 50 page create image successfully")