from pycaret.datasets import get_data
data = get_data('jewellery')

print(data)

from pycaret.clustering import *
s = setup(data, normalize = True)

kmeans = create_model('kmeans')

evaluate_model(kmeans)