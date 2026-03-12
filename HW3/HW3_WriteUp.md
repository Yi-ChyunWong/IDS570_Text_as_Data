## Baseline Script L2

### Confusion Matrix

|                       | Predicted Negative  | Predicted Core  |
|----------             |:----------:         |:----------:     |
| **Actual Negative**   | 1906                | 75              |
| **Actual Core**       | 131                 | 1798            |

### Classification Report

| Class             | Precision | Recall | F1-score | Support |
|------             |-----------|--------|----------|---------|
| 0                 | 0.94      | 0.96   | 0.95     | 1981    |
| 1                 | 0.96      | 0.93   | 0.95     | 1929    |
| **Accuracy**      |           |        | **0.95** | 3910    |
| **Macro Avg**     | 0.95      | 0.95   | 0.95     | 3910    |
| **Weighted Avg**  | 0.95      | 0.95   | 0.95     | 3910    |

### ROC AUC: 0.987

### Number of non-zero coefficients: 16198

### Top 15 positive-weight words (most predictive of CORE = 1)
- trade: 27.556
- merchants: 22.286
- merchant: 17.624
- marchants: 13.415
- marchant: 8.709
- factor: 5.189
- staple: 4.985
- commodities: 4.328
- ship: 3.149
- buy: 2.995
- chapman: 2.957
- exchange: 2.949
- goods: 2.933
- ships: 2.726
- money: 2.701

### Top 15 negative-weight words (most predictive of NEG = 0)
- god: -3.122
- power: -1.928
- pope: -1.897
- rome: -1.888
- christ: -1.767
- spirit: -1.650
- enemies: -1.645
- gods: -1.627
- forces: -1.600
- faith: -1.593
- against: -1.571
- vertue: -1.506
- that: -1.434
- de: -1.353
- armie: -1.349

## Script L1

### Confusion Matrix

|                       | Predicted Negative  | Predicted Core  |
|----------             |:----------:         |:----------:     |
| **Actual Negative**   | 1981                | 0               |
| **Actual Core**       | 6                   | 1923            |

### Classification Report

| Class             | Precision | Recall | F1-score | Support |
|------             |-----------|--------|----------|---------|
| 0                 | 1.00      | 1.00   | 1.00     | 1981    |
| 1                 | 1.00      | 1.00   | 1.00     | 1929    |
| **Accuracy**      |           |        | **1.00** | 3910    |
| **Macro Avg**     | 1.00      | 1.00   | 1.00     | 3910    |
| **Weighted Avg**  | 1.00      | 1.00   | 1.00     | 3910    |

### ROC AUC: 1.0

### Number of non-zero coefficients: 28

### Top 15 positive-weight words (most predictive of CORE = 1)
- trade: 174.931
- merchants: 148.667
- merchant: 123.939
- marchants: 90.009
- marchant: 66.278
- staple: 57.439
- factor: 56.940
- adventurers: 42.912
- chapman: 36.522
- adventurer: 31.384
- purser: 28.667
- venturers: 12.074
- ship: 3.073
- have: 1.823
- william: 1.700

### Top 15 negative-weight words (most predictive of NEG = 0)
- god: -2.722
- that: -2.560
- it: -0.856
- christ: -0.341
- not: -0.281
- 00: 0.000
- 000: 0.000
- 10: 0.000
- 1000: 0.000
- 10000: 0.000
- 100000: 0.000
- 101: 0.000
- 102: 0.000
- 103: 0.000
- 104: 0.000

### Performance: Did L1 improve or reduce test-set performance relative to L2? Use at least two metrics (e.g., F1 and ROC AUC) to justify your claim.
- Based on the metrics I got from my models, the L1 model did improve my test-set performance relative to the L2 model. The accuracy and ROC AUC scores of the L1 model are higher than those of the L2 model. For the L2 model, the accuracy is 0.95, and the ROC AUC is 0.987. For the L1 model, the accuracy is 1.0, and the ROC AUC is 1.0. From an accuracy perspective (recall Accuracy = (TP + TN) / (TP + TN + FP + FN)), the high accuracy for L1 compared to L2 shows that the L1 had more correct classifications than the L2 (using the 0.5 threshold). From a ROC AUC perspective, the high AUC for L1 compared to L2 shows that the L1 was better at differentiating the two classes than the L2 (regardless of the classification threshold). 

### Sparsity and interpretability: How many coefficients are non-zero in L1 vs. L2? Does L1 give you a more “readable” model? Why or why not?
- For the L2 model, there are 16198 non-zero coefficients. For the L1 model, there are only 28 non-zero coefficients. In my opinion, I think L1 gave me a more readable model. The weights are more sparse in the L1 model compared to those in L2, and thus when we examine all the weights in the models, we can see that for the L1, the largest weights have the most impact on the model, and for the L2, the weights are more spread out. More specifically, the difference between the top weights in L1 is more significant than the difference between the top weights in L2. L1 is more readable because I am more certain which weights made the more noticeable contributions. For the L2, there are multiple weights that had some contribution to the model, but it was difficult to pinpoint which weights had the most contribution, and thus making it less readable. 

### Stability and feature correlation (conceptual): TF–IDF features are often correlated (e.g., ship, ships, shipping; or words that co-occur in the same rhetorical formula). Based on your results, does L1 seem to “choose winners” among correlated features? What might be the downside of that?
- Based on the top weights that is observed for the L1 model, the L1 seem to choose winners among correlated features / tokens / words. For the base word "merchant," the highest weight of them was for "merchants," which got a weight of 148.667, and the lowest weight of them was for "marchant," which got a weight of 66.278. Here are the weights in order:

    - merchants: 148.667
    - merchant: 123.939
    - marchants: 90.009
    - marchant: 66.278

    For the L2 model, the difference between the weights are a lot less:
    
    - merchants: 22.286
    - merchant: 17.624
    - marchants: 13.415
    - marchant: 8.709

    When comparing the two models, it is apparent that the L1 model does choose winners among correlated features. The potential downside to this is that the L1 model may be too rigid and not very adaptable. In a different document where one of the words is used more often, it might not be able to classify it as well. In other words, the L1 model may be more prone to overfitting than the L2 model. This may also mean that the L1 model is less stable when applied to different inputs.

### Weak supervision + label noise: Your CORE/NEG labels come from a weak-supervision workflow, so some labels may be wrong. Which penalty (L1 or L2) seems more robust to this—based on what you see? Be explicit about what evidence you’re using and what you’re inferring.
- While we cannot really know how well the initial CORE/NEG labeling was done without human validation, we can observe from how "stable" a model is to determine if it is robust against errors in labeling. The main metric for stability we have is how sparse the weights are. The L1 model has much sparser weights than the L2 model (26 vs 16198 non-zero weights). This, like we said in the previous question, tells us that the L1 model is more prone to overfitting than the L2 model. There are a lot less features that contribute to the model, and thus when there are mislabelings, the effects could be compounded. For example, if some of the chunks containing the word "merchant" are classified as NEG, there would be a more significant impact on the final weight in the L1 model than in the L2 model as it is one of the few big contributers for the L1 model, while the overall contribution of it is less significant in the L2 model. In other words, an overfitted model is susceptible to the effects of noisy labels.

### Historical interpretation payoff: If your goal is to extract historically meaningful “signals” (keywords or rhetorical markers) that distinguish CORE from NEG, which model would you pick and why?
- From what we answered for the question of interpretability, I think the L1 model is the one I would pick. It is more clear from the weights of the L1 models which features really drove the distinction between a CORE chunk versus a NEG chunk, whereas there were some candidates from the L2 model weights that contributed to the classification, but it was difficult for us to pinpoint which features distinguishes CORE from NEG. For the goal of extracting meaningful signals, I would pick the L1 model. For a prediction task, however, I would want to train my model on the L2 model for better stability and flexibility to tolerate noisy labels, especially with limited human-validated labels.