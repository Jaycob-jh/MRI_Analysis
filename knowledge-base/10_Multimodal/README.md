# 10 Multimodal

多模态的目标不是把多个数据简单拼接，而是明确每种模态提供的独立信息与共同潜变量。

## 典型组合
- EEG + fMRI
- MEG + MRI
- dMRI + fMRI
- iEEG + fMRI
- TMS + EEG
- TMS + fMRI
- tES + EEG
- tPBM + EEG/fMRI

## 关键问题

### 1. 时间与空间尺度
- EEG/MEG：毫秒级
- fMRI：秒级血流动力学
- dMRI：结构约束
- stimulation：干预变量

### 2. Registration
不同模态如何映射到同一 anatomical space。

### 3. Feature alignment
ROI、source、tract、network、time window 是否同一科学单位。

### 4. Fusion
- correlation / regression
- CCA / PLS
- joint ICA
- multimodal latent variable
- graph neural network
- Bayesian hierarchical model

### 5. Multiple testing
跨模态与多个 contrast 的 joint correction。

### 6. Causality
刺激 + 测量可以加强机制证据，但仍需设计、对照和中介识别条件。
