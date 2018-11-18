predicted1 = knn.predict_proba(X_test.iloc[:,:raw_data.shape[1]-1])
predicted1[:,1]
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

fpr,tpr,threshold = roc_curve(X_test.iloc[:,raw_data.shape[1]-1:], predicted1[:,1]) 
roc_auc = auc(fpr,tpr) ###计算auc的值
plt.figure()
lw = 2
plt.figure(figsize=(10,10))
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc) ###假正率为横坐标，真正率为纵坐标做曲线
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
