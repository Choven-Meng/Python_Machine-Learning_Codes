import matplotlib.pyplot as plt
plt.plot(k_range,scores)
plt.xlabel('value of k for KNN')
plt.ylabel('Testing Accuracy')
plt.savefig('test_set_feature_relations.png',dpi=1000) #more dpi more size of the image
plt.clf() #to flush out plt from memory so that new plot can be created
