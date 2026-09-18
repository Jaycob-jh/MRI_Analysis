# Brain Research Knowledge Base — V1

这是一个面向长期科研训练的脑科学方法学知识库。目标不是收藏软件教程，而是建立一套可以解释 **“为什么这样分析、输入是什么、数学/生理依据是什么、输出代表什么、怎样验证、怎样报告”** 的知识体系。

## 研究范围

本知识库以人类脑结构与功能网络、发育与精神健康为主轴，并扩展到以下方向：

- MRI：结构 MRI、fMRI、dMRI、VBM、FreeSurfer、配准与质量控制
- EEG：采集、参考、滤波、伪迹、ERP、时频、源定位、连接与网络
- MEG：传感器物理、SSS/SSP、源重建、beamforming、时频和连接
- TMS：MEP、RMT/AMT、SICI/ICF、rTMS、TBS、TMS-EEG、E-field
- tES：tDCS、tACS、tRNS、montage、剂量、电场建模、sham/blinding
- 经颅光刺激 / tPBM：光学剂量、组织光学、1064 nm/NIR、Monte Carlo、EEG/fMRI endpoints
- 脑网络：结构/功能/有效连接、图论、NBS/TFNBS、空间零模型、动态网络
- 统计与机器学习：GLM、LME/GLMM、GAM/GAMM、Bayesian、permutation、FWE/FDR、CCA/PLS、预测与验证
- 多模态：EEG-fMRI、TMS-EEG、TMS-fMRI、TES-EEG、tPBM-EEG 等
- 科研设计：可重复性、数据泄漏、样本量、效应量、纵向/重复测量、规范模型和个体化分析

## 与 Cui Lab 方向的对应

Cui Lab（CIBR）公开研究方向强调：人类宏观结构/功能 connectome 的组织原则与行为意义、青少年脑网络发育及其在精神障碍中的异常，并结合神经影像、网络建模、机器学习、行为与实验设计。实验室还明确涉及 diffusion MRI、fMRI、MEG、iEEG、network control、青少年执行功能、ADHD，以及 tDCS/tPBM 干预。

- Lab: https://cuilab.cibr.ac.cn/
- Research overview: https://cuilab.cibr.ac.cn/Research/index.htm
- Brain network architecture: https://cuilab.cibr.ac.cn/Research/EnimRaesentElementum/index.htm
- Adolescence development: https://cuilab.cibr.ac.cn/Research/AdolescenceDevelopment/index.htm
- Selected publications: https://cuilab.cibr.ac.cn/Publications/Selected/index.htm

## 学习原则

每个知识单元尽量回答：

1. **是什么**：定义与术语边界。
2. **为什么需要**：它解决哪一个研究问题。
3. **原理**：生理/物理/数学依据。
4. **输入**：真正进入方法的数据是什么。
5. **计算**：核心模型、公式或算法流程。
6. **输出**：参数、图像、连接矩阵或统计量分别代表什么。
7. **假设**：独立性、分布、平稳性、exchangeability、线性等。
8. **QC/诊断**：如何判断结果是否可信。
9. **常见错误**：软件能跑但科学解释错误的情况。
10. **论文表达**：Methods/Results 应报告哪些信息。
11. **迁移**：它怎样用于 MRI、EEG/MEG、脑刺激和网络研究。

## 目录

- `00_Roadmap/`：知识地图、学习路线、掌握标准
- `01_Foundations/`：神经科学、数学、信号处理与实验设计基础
- `02_Statistics_and_Modeling/`：统计模型和推断主干
- `03_MRI/`：结构 MRI / fMRI / dMRI
- `04_EEG/`：EEG
- `05_MEG/`：MEG
- `06_TMS/`：TMS
- `07_TES/`：tES
- `08_Transcranial_Light_Stimulation/`：tPBM / 经颅光刺激
- `09_Brain_Networks/`：连接组与网络神经科学
- `10_Multimodal/`：多模态整合
- `11_Machine_Learning/`：预测、降维和验证
- `12_Tools/`：软件工具层
- `13_Paper_Reading/`：论文阅读、Cui Lab 文献体系
- `References/`：原始学习材料与来源索引

## V1 已纳入

- 用户提供的 `brain_statistics_guide_zh.md` 原文。
- 用户提供的《脑科学与神经影像研究中的统计方法与统计模型》PDF 的知识框架（PDF 为二进制源文件，本分支先以其可检索 Markdown 对应材料为主）。
- Cui Lab 研究方向和 Selected Publications 文献地图。
- MRI / EEG / MEG / TMS / tES / tPBM / 脑网络 / 多模态 / ML 的第一版知识骨架。
- 经典与近期核心论文的第一版学习卡片。

> V1 的定位是“搭好骨架并建立可持续扩展规范”，后续再逐篇论文、逐个方法做深度笔记。
