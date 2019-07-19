import pickle
decision_tree_model_pkl = open('deci_tree.pkl', 'rb')
decision_tree_model = pickle.load(decision_tree_model_pkl)
print ("Loaded Decision tree model :: ", decision_tree_model)


import numpy as np
x=np.array([9.00,4092,2351,0.5]).reshape(1,-1)
labels_pred = decision_tree_model.predict(x)


