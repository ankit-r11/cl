st = 'Print only the words that start with s in this sentence'
print(st.split())

for word in st.split():
    if word[0]=='s':
      print(word)
