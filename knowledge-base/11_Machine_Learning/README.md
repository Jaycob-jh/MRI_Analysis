# 11 Machine Learning

## 先分清目标
- **Inference**：某参数是否与 outcome 相关？
- **Prediction**：能否泛化到 unseen subjects？

二者都重要，但证据逻辑不同。

## 基础模型
- linear / logistic regression
- ridge / lasso / elastic net
- SVM / SVR
- random forest
- gradient boosting
- neural networks

## 降维
- PCA：最大化 X variance
- ICA：统计独立 source
- CCA：最大化两组变量投影相关
- PLS：最大化协方差结构

漂亮的 component/loading map ≠ 已完成 inference。

## Validation
- train/test split
- k-fold CV
- repeated CV
- nested CV
- group-aware CV
- leave-site-out
- external validation

## Data leakage
以下步骤只能在 training fold 内估计：
- scaling
- imputation
- PCA
- feature selection
- confound regression（取决于目标与实现）
- ComBat/harmonization（若参数依赖测试集）
- hyperparameter tuning

## Classification metrics
- sensitivity / specificity
- accuracy / balanced accuracy
- ROC-AUC
- PR-AUC
- calibration
- Brier score

## Regression metrics
- MAE
- RMSE
- out-of-sample R²
- prediction correlation（不能替代 R²）

## Neuroimaging 特有问题
- p >> n
- site effects
- family structure
- repeated measures
- spatial autocorrelation
- feature instability
- small-n optimism
