import io 
import os
from google.cloud import vison  # cloud client library
from google.cloud import types  

pic = "pic.jpg"  # picture 

client = vison.ImageAnnotatorClient() # instanteates a client 
file_name = os.path.join(os.path.dirname(__file__),pic)

with io.open(file_name,'rb') as image_file:
	content = image_file.read() #loads image into memory

image  = vison.types.Image(content=content)
responce = client.document_text_dectection(image=image)

for page in responce.full_text_annotation.pages:
	for block in page.blocks:
		print("\nBlocks confidnece: {}\n".format(paragraph.confidence))
		for word in paragraph.words:
			word_text =''.join([symbol.text for symbol in word.symbols])
			print("Word text: {} (condfidence: {}".format(word_text, word.confidence))
			for symbol in word.symbols:
				print('tSymbol: {} (confidence : {})'.format(symbol.text, symbol.confidence))

