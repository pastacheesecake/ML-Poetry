import os,glob,pickle
from nltk import tokenize
folder_path = 'books' #Directory where our data is
container = [] # Contains tokenized books to be pickled into file, probably list ain't a good idea though
for filename in glob.glob(os.path.join(folder_path, '*')):  #Finds all files in  folder_path
  with open(filename, 'r',encoding='utf-8') as f: # utf-8 magic
    text = ' '.join(f.read().splitlines()) #strips newlines
    lines_list = tokenize.sent_tokenize(text) #nltk tokenization
    container.append(lines_list)
container = [item for sublist in container for item in sublist]
with open('results.txt','wb') as results:
    pickle.dump(container,results)
