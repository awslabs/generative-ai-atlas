<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Traditional Evaluation Metrics

**Content Level: 200**

## Suggested Pre-Reading

* Introduction to Machine Learning
* Basic Statistics for Data Science

## TL;DR

Traditional evaluation metrics like accuracy, precision, recall, and F1-score are important for assessing the performance of classification models. While each metric has its strengths, understanding their limitations and knowing when to use which metric is important for making informed decisions about model performance.

## Confusion Matrix: The Foundation of Classification Metrics

Before diving into specific metrics, it's important to understand the confusion matrix, which forms the basis for many classification metrics. Given a binary classification task, with two labels: Positive and Negative, the confusion matrix is defined as:

|Actual \ Predicted	|Positive	|Negative	|
|---	|---	|---	|
|Positive	|True Positive (TP)	|False Negative (FN)	|
|Negative	|False Positive (FP)	|True Negative (TN)	|

Definitions:

* True Positive (TP): Correctly predicted positive instance
* True Negative (TN): Correctly predicted negative instance
* False Positive (FP): Incorrectly predicted positive instance (Type I error)
* False Negative (FN): Incorrectly predicted negative instance (Type II error)

## Common Evaluation Metrics

### 1. Accuracy

**Definition:** The proportion of correct predictions (both true positives and true negatives) among the total number of cases examined.

**Formula:** (TP + TN) / (TP + TN + FP + FN)

**Pros:**

* Simple to understand and calculate
* Works well for balanced datasets

**Cons:**

* Can be misleading for imbalanced datasets
* Doesn't provide information about the types of errors

**When to use:** Best for balanced datasets where all classes are equally important.


### 2. Precision

**Definition:** The proportion of correct positive predictions out of all positive predictions.

**Formula:** TP / (TP + FP)

**Pros:**

* Useful when the cost of false positives is high
* Indicates how reliable the positive predictions are

**Cons:**

* Doesn't consider false negatives
* Can be artificially inflated by predicting very few positives

**When to use:** When you want to minimize false positives, e.g., spam detection.


### 3. Recall (Sensitivity or True Positive Rate)

**Definition:** The proportion of actual positive cases that were correctly identified.

**Formula:** TP / (TP + FN)

**Pros:**

* Useful when the cost of false negatives is high
* Indicates how well the model identifies positive cases

**Cons:**

* Doesn't consider false positives
* Can be artificially inflated by predicting everything as positive

**When to use:** When you want to minimize false negatives, e.g., disease detection.


### 4. F1-Score

**Definition:** The harmonic mean of precision and recall, providing a single score that balances both metrics.

**Formula:** 2 * (Precision * Recall) / (Precision + Recall)

**Pros:**

* Balances precision and recall
* Works well for imbalanced datasets

**Cons:**

* Doesn't take true negatives into account
* May not be suitable when false positives and false negatives have very different costs

**When to use:** When you need a balanced measure between precision and recall, especially for imbalanced datasets.


### 5. Micro-Average F1

**Definition:** Calculate F1 globally by counting the total true positives, false negatives, and false positives across all classes.

**Pros:**

* Gives equal weight to each instance
* Suitable for multi-class classification with imbalanced classes

**Cons:**

* Can be dominated by the performance on common classes

**When to use:** When you want to weigh each instance equally, regardless of its class.


### 6. Macro-Average F1

**Definition:** Calculate F1 for each class independently and then take the unweighted mean of these metrics.

**Pros:**

* Gives equal weight to each class
* Suitable for multi-class classification when all classes are equally important

**Cons:**

* May not reflect overall performance well if classes are imbalanced

**When to use:** When you want to give equal importance to all classes, regardless of their frequency.


## Practical Considerations

* Dataset Characteristics:
    * For imbalanced datasets, consider precision, recall, and F1-score over accuracy.
    * For multi-class problems, use micro or macro-averaging depending on whether you want to weigh classes or instances equally.
* Problem Domain: Consider the problem domain in deciding which metrics matter the most, e.g.
    * In medical diagnosis, high recall might be more important to avoid missing positive cases.
    * In spam detection, high precision might be preferred to avoid flagging legitimate emails as spam.
* Cost of Errors: Consider the real-world impact of false positives vs. false negatives in your specific application.
* Model Comparison: Use the same metric(s) consistently when comparing different models or iterations.
* Threshold Adjustment: Remember that many metrics can be affected by adjusting the classification threshold.

### 6. Libraries for Evaluation Metrics

* Scikit-learn: It has comprehensive suite of evaluation metrics, and allows easy integration with machine learning workflows
* TensorFlow/Keras: Built-in metrics for deep learning models
* PyTorch: Torchmetrics library for PyTorch users

## Conclusion

Understanding and correctly applying evaluation metrics is important for developing effective machine learning models. While traditional metrics like accuracy, precision, recall, and F1-score provide valuable insights, it's important to consider the specific requirements of your problem and the characteristics of your dataset when choosing which metrics to use. By leveraging appropriate metrics and using available libraries, you can make informed decisions about model performance and guide your model development process effectively.


## Contributors

**Authors**

* Hari Prasanna Das - Applied Scientist 

**Primary Reviewer:**

* Samaneh Aminikhanghahi - Applied Scientist II 
