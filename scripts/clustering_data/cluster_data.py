
import enum
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_breast_cancer
from sklearn.cluster import AgglomerativeClustering
import umap
import json

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

def structure_data(cluster, key):
    labels = cluster.labels_
    for i, x in enumerate(labels):
        d[key].append({
            'cluster' : int(x),
            'coords' : normalised[i].tolist()
        })

digits = load_breast_cancer()

embedding = umap.UMAP(min_dist=0.01, n_neighbors=3).fit_transform(digits.data)
normalised = MinMaxScaler().fit_transform(embedding)

a = AgglomerativeClustering(n_clusters=2).fit(normalised)
b = AgglomerativeClustering(n_clusters=4).fit(normalised)
c = AgglomerativeClustering(n_clusters=8).fit(normalised)

d = {
    '2' : [],
    '4' : [],
    '8': [],
}

structure_data(a, '2')
structure_data(b, '4')
structure_data(c, '8')

write_json('data.json', d)    