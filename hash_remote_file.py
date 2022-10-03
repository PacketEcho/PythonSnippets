import hashlib
import requests


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names"
filestream = requests.get(url, stream=True)

md5 = hashlib.md5()
for chunk in filestream.iter_content(chunk_size=1024): 
    md5.update(chunk)

print(md5.hexdigest())
