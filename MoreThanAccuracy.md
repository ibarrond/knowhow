One sees "Validation and test accuracy" everywhere as a metric on how well does the model perform.
However, this is leaving out a substantial part of the information.

Four Outcomes of Binary Classification:
- _True positives_: data points labeled as positive that are actually positive.
- _False positives_: data points labeled as positive that are actually negative.
- _True negatives_: data points labeled as negative that are actually negative.
- _False negatives_: data points labeled as negative that are actually positive.

The most important metrics are:
- __precision__ = True positives / (True positives + True negatives)
- __recall/Sensitivity = True positives / (True positives + False negatives)
- __F1__ = 2*_precision_*_recall_/(_precision_+_recall_)

Visualizing Recall and Precision
- __Confusion matrix__: shows the actual and predicted labels from a classification problem
- __Receiver operating characteristic (ROC) curve__: plots the true positive rate (TPR) versus the false positive rate (FPR) as a function of the model’s threshold for classifying a positive
- __Area under the curve (AUC)__: metric to calculate the overall performance of a classification model based on area under the ROC curve
