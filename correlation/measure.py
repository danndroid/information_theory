import numpy as np
from sklearn.metrics import mutual_info_score

def mutual(x,y, bins):
    c_xy = np.histogram2d(x,y, bins)[0]
    mi = mutual_info_score(None, None, contingency=c_xy)
    return mi 




