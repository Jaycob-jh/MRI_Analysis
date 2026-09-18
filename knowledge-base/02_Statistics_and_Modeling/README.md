# 02 Statistics and Modeling

本模块的第一原则来自本知识库已收录的统计学习资料：

> **GLM/GAM/LMM 是模型；t/LRT/permutation 是推断方法；t/F/χ² 是统计量；df 描述参考分布或模型复杂度；β/r/R²/Cohen's d 是参数或效应量；FDR/FWER 是错误控制目标。**

这几层不能混为一谈。

原始学习材料：
- [brain_statistics_guide_zh.md](../References/Source_Materials/brain_statistics_guide_zh.md)
- 用户提供 PDF：《脑科学与神经影像研究中的统计方法与统计模型：从经典推断、GLM/GAM/LME 到脑网络与机器学习》

## 通用分析顺序

```
研究问题
  ↓
独立观测单位 / 数据结构
  ↓
因变量分布
  ↓
模型
  ↓
目标参数 / contrast
  ↓
SE / test statistic / uncertainty
  ↓
多重比较
  ↓
effect size
  ↓
validation / sensitivity analysis
  ↓
scientific interpretation
```

## A. 基础推断

### t 检验
核心思想：

`t = estimate / standard error`

重点不是机械检查“原始值正态”，而是：
- 独立性
- 配对结构
- 异常值
- 残差
- 方差结构

### ANOVA / ANCOVA
应理解成 general linear model 的特例，而不是另一套统计世界。

### correlation
- Pearson：线性关联
- Spearman：rank-based monotonic association
- partial correlation：控制协变量后的条件关联
- 相关不等于神经连接，更不等于因果

## B. General Linear Model

```
y = Xβ + ε
```

理解重点：
- design matrix
- intercept
- coding
- interaction
- nuisance regressors
- contrast vector / matrix
- residual covariance

fMRI 的大量经典统计都可写成：
```
design matrix + contrast + error model + multiple-comparison inference
```

## C. Generalized GLM
- logistic：binary
- Poisson / negative binomial：count
- Gamma 等：正偏连续结局

不要把连续 BOLD 强行套成 logistic/Poisson。

## D. LME / GLMM / GEE
适合：
- repeated scans
- sessions/runs
- longitudinal follow-up
- family/site clustering

核心：
```
y = Xβ + Zb + ε
```

同一受试者 3 次扫描 ≠ 3 个独立受试者。

## E. GAM / GAMM
用于 age、dose、recovery 等非线性轨迹。

关注：
- basis
- smoothness penalty
- edf
- REML/GCV
- gam.check
- concurvity
- derivative / simultaneous interval

smooth 显著 ≠ 已经证明“非线性部分显著”。

## F. Bayesian
- prior
- likelihood
- posterior
- credible interval
- posterior predictive check
- hierarchical partial pooling

## G. Resampling
### Bootstrap
回答估计量有多不确定/多稳定。

### Permutation
回答在指定 null 与 exchangeability 约束下，统计量有多异常。

置换不是“随便打乱”。

## H. Multiple Comparisons
- Bonferroni / Holm
- BH-FDR
- max-T / max-F
- RFT
- cluster inference
- TFCE
- NBS / TFNBS

必须先定义：
**family 是哪些 voxel / vertex / edge / contrast / frequency / time point？**

## I. Prediction
- train / validation / test
- nested CV
- group-aware splitting
- external validation
- calibration
- ROC-AUC / PR-AUC
- permutation significance

所有会“学习数据”的步骤都要封闭在 training fold：
- scaling
- PCA
- feature selection
- harmonization（若会估计参数）
- hyperparameter tuning

## J. 读论文时固定检查

1. outcome 是什么？
2. independent unit 是什么？
3. 模型是什么？
4. null hypothesis 是什么？
5. statistic 怎么来？
6. df 怎么来？
7. effect size 是什么？
8. multiplicity 如何处理？
9. model diagnostics 做了吗？
10. 如果是 prediction，是否真正 out-of-sample？
