# Cui Lab Core Paper Notes — V1

说明：这是第一版“学习卡片”，不是替代全文的最终精读。内容只写入已从原文/公开摘要核实的信息；后续逐篇扩展为完整模板。

---

## 1. Cui et al., Neuron (2020)
**Individual Variation in Functional Topography of Association Networks in Youth**  
DOI: https://doi.org/10.1016/j.neuron.2020.01.029  
Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7182484/

### 核心问题
个体之间大尺度功能网络在皮层上的空间布局并不完全相同，这种 functional topography 在青少年时期如何变化？是否与执行功能有关？

### 设计与方法
- 693 名 8–23 岁青少年。
- 每人使用 27 min 高质量 fMRI。
- 以个体化网络拓扑作为核心表征。
- 论文主线使用机器学习/空间正则化 NMF 来刻画个体功能网络；研究还用其他个体化方法做稳健性验证。

### 主要发现
- association networks 的功能拓扑个体差异最大。
- association network topography 随年龄发生系统性 refinement。
- 网络拓扑可预测未见个体的 brain maturity。
- association/control network 的皮层表征与执行功能个体差异有关。
- variability 还与 evolutionary expansion、myelination、cerebral blood flow 等宏观属性相关。

### 学习意义
这篇是理解“group atlas 不等于每个人真实网络边界”的核心论文。对 dense sampling / individualized parcellation 的研究，必须先理解 acquisition duration、reliability 和 atlas mismatch。

---

## 2. Cui et al., eLife (2020)
**Optimization of energy state transition trajectory supports the development of executive function during youth**  
DOI: https://doi.org/10.7554/eLife.53060

### 核心问题
结构连接网络在发育中怎样改变，使大脑更容易进入支持执行功能的 frontoparietal activation state？

### 设计与方法
- 946 名 8–23 岁参与者。
- diffusion imaging 构建 structural connectome。
- 使用 linear dynamical network control theory 计算把系统驱动到 frontoparietal activation state 的理论能量成本。

### 主要发现
- 随发育，激活 frontoparietal system 所需理论能量下降。
- regional energetic cost 的空间模式能预测未见个体的 brain maturity。
- cingulate cortex 的 energetic requirements 与 executive performance 负相关，并部分解释年龄与执行功能发展的关系。

### 学习意义
network control 的“energy”是模型中的状态转移代价，不是直接测到的脑代谢能量。需要严格区分 dynamical model quantity 与生理能量。

---

## 3. Cui et al., Biological Psychiatry (2022)
**Linking Individual Differences in Personalized Functional Network Topography to Psychopathology in Youth**  
DOI: https://doi.org/10.1016/j.biopsych.2022.05.014

### 设计
- 790 名 8–23 岁青少年。
- 27 min 高质量 fMRI。
- 112 项临床症状用于构建 psychopathology dimensions。
- spatially regularized NMF 得到 17 个个体化功能网络。
- PLS regression + split-half cross-validation 测试网络拓扑能否预测未见个体的精神病理维度。

### 发现
- 个体化网络 topography 能预测 fear、psychosis、externalizing、anxious-misery 等维度。
- association network representation 的减少是多个维度的重要预测特征。
- overall psychopathology 的预测相关约为 r=0.16，并通过 permutation 评估。

### 学习意义
论文把 personalized topography 从“发育/认知”推向“精神病理”。预测结果是 association/prediction 证据，不应写成 causal biomarker。

---

## 4. Huang et al., Nature Communications (2023)
**Intracranial electrophysiological and structural basis of BOLD functional connectivity in human brain white matter**  
DOI: https://doi.org/10.1038/s41467-023-39067-3

### 核心问题
white-matter BOLD FC 是否具有电生理基础，而不只是 fMRI/预处理产生的现象？

### 设计
- 16 名药物难治性癫痫患者。
- SEEG + resting-state fMRI。
- 加入 diffusion spectrum imaging / structural connectivity。

### 发现
- white-matter BOLD FC 与 SEEG FC 相关。
- 该对应关系跨多个频段存在。
- SEEG 和 fMRI 的 white-matter FC 都与 white-matter structural connectivity 相关。

### 学习意义
这是典型 multimodal triangulation：fMRI、颅内电生理和结构连接从不同测量层面对同一 white-matter functional organization 提供证据。

---

## 5. Zhao et al., BMC Medicine (2024)
**Hierarchical individual variation and socioeconomic impact on personalized functional network topography in children**  
DOI: https://doi.org/10.1186/s12916-024-03784-3

### 设计
- ABCD，6001 名 9–10 岁儿童。
- spatially regularized NMF 得到 17 个 personalized networks。
- repeated random twofold CV 的 PLS regression 预测 income-to-needs、parental education、neighborhood disadvantage。

### 发现
- 个体化 topography variability 沿 sensorimotor-association hierarchy 组织。
- network topography 可以预测未见个体的三个 SES factors。
- association cortex 的关系更突出。

### 学习意义
要非常谨慎解释“SES influences brain”一类措辞：该研究主体是 observational association/prediction，并不因为 cross-validation 就自动获得因果解释。

---

## 6. Chen et al., Imaging Neuroscience (2024)
**Group-common and individual-specific effects of structure-function coupling in human brain networks with graph neural networks**  
DOI: https://doi.org/10.1162/imag_a_00378

### 核心问题
SC→FC coupling 到底主要是群体共享规律，还是具有显著个体特异性？

### 方法与发现
- 两个独立高质量数据集。
- graph neural network 从 structural connectivity 预测 unseen individuals 的 functional connectivity。
- coupling 主要受 network topology 驱动。
- group-common effects 占主导，但存在较弱而显著的 individual-specific effects。
- 区域层面沿 sensorimotor-association axis 呈层级组织：association cortex 的 group-common 较低、individual-specific 较高。

### 学习意义
“模型预测 FC 很好”不等于“模型已经揭示因果机制”；但它为结构约束功能提供可量化建模框架。

---

## 7. Li et al., Brain Stimulation (2024)
**Transcranial low-level laser stimulation in the near-infrared-II region (1064 nm) for brain safety in healthy humans**  
DOI: https://doi.org/10.1016/j.brs.2024.11.010

### 研究定位
1064 nm 近红外-II transcranial photobiomodulation 的健康人安全性。

### 安全评价维度
公开信息显示研究结合：
- NSE / S100β
- EEG
- MRI
- executive functions
- subjective questionnaire

### 学习意义
tPBM 的研究首先要建立明确 dose description、target、thermal/safety monitoring 和 sham/blinding；设备输出不能直接等价为脑内光剂量。

---

## 8. Yang et al., PNAS (2025)
**Connectional axis of individual functional variability: Patterns, structural correlates, and relevance for development and cognition**  
DOI: https://doi.org/10.1073/pnas.2420228122

### 核心问题
FC 的个体差异若放在“edge”层面，是否存在有组织的连续轴，而非随机散布？

### 发现
- edge-level FC variability 形成 connectional axis。
- variability 从 within-network 到 between-network、从 association-related connections 到 sensorimotor-association connections 呈连续变化。
- 该轴与 structural connectivity variability 的空间模式相关。
- 轴在 youth 中随发育 refinement，并与 higher-order cognition 有关。

### 学习意义
这是从 regional variability 走向 edge-level variability 的关键发展，也帮助理解 sensorimotor-association hierarchy 如何成为多个发育现象的共同坐标系。

---

## 9. Xu et al., Nature Communications (2026)
**Mapping the spatiotemporal continuum of structural connectivity development across the human connectome in youth**  
DOI: https://doi.org/10.1038/s41467-026-73072-6

### 设计
使用三个独立 developmental cohorts 的 diffusion MRI。

### 发现
- structural connectivity maturation 沿预定义 sensorimotor-association connectional axis 呈连续分化。
- 早期更多表现为 sensorimotor–sensorimotor connectivity 增强。
- 较晚青春期更多表现为 association–association connectivity 增强。
- 转换大约出现在 15 岁附近。
- 该轴还组织了 SC 与 higher-order cognition、general psychopathology 的关联。

### 学习意义
它为后续“developmental deviation”建立 normative reference：先理解正常发育连续体，再讨论 ADHD 偏离。

---

## 10. Cong et al., PNAS (2026)
**White-matter functional connectivity uniquely predicts brain age, cognition, and psychopathology beyond gray-matter connectivity**  
DOI: https://doi.org/10.1073/pnas.2604191123

### 设计与发现
- 四个独立 developmental cohorts，brain-age 分析总 n=2370。
- gray-white 与 white-white FC 能预测 brain age。
- 在控制 gray-gray FC 后仍保留独立预测信息。
- white-matter FC 也提供 cognition 与 ADHD symptom 的额外解释/预测信息。
- feature contributions 分布于 commissural、projection、superficial 和 association pathways。

### 学习意义
“beyond gray matter”必须理解成统计上的 nonredundant predictive information，不等于 white-matter FC 比 gray-matter FC 更重要。

---

## 11. Zhang et al., Science Bulletin (2026)
**Intracranial EEG reveals working memory-related dynamics and connectivity in human white matter**  
DOI: https://doi.org/10.1016/j.scib.2026.07.051

### 设计
- 20 名药物难治性癫痫患者。
- sEEG。
- N-back working-memory task。

### 发现
- working-memory load 引起 tract- and frequency-specific local-field-potential changes。
- frontal blade tract 的 gamma/high-gamma 增强，而部分 posterior white-matter regions 方向不同。
- within-frequency FC 对 task condition 较稳定。
- cross-frequency connectivity，尤其 theta–high-gamma coupling，随 memory load 增强。

### 学习意义
white-matter function 不能只用静态 BOLD FC 理解；时频和 cross-frequency interaction 提供更直接的快速神经动态证据。

---

## 12. Li et al., Nature Mental Health (2026)
**Developmental benchmarks of executive function reveal sensitive periods for adolescent mental health**  
DOI: https://doi.org/10.1038/s44220-026-00711-8

### 设计
- 33,622 名中国 11–18 岁青少年。
- 建立 inhibitory control 与 working memory 的 normative developmental trajectories。
- 在 11,549 名美国青少年中复现。

### 发现
- inhibitory control 持续成熟到青春期晚期。
- working memory 更早达到平台，并伴随个体差异下降。
- 低于年龄规范的 EF deviation 与更多 mental health difficulties 相关。
- 这种关系在早期青春期（约 11–13 岁）更突出。

### 学习意义
重点不是简单“年龄和 EF 的相关”，而是 norm-referenced deviation 与 age-sensitive vulnerability。

---

## 13. Xu et al., Nature Biomedical Engineering (2026)
**Developmental deviations of association-network structural connectivity in youths with ADHD predict symptom and treatment outcomes**  
DOI: https://doi.org/10.1038/s41551-026-01779-4

### 设计
建立 age-related white-matter SC normative trajectories，并量化个体 deviation。公开正式版摘要报告两套独立数据：一个大型纵向 developmental cohort，以及独立 ADHD cohort。

### 发现
- ADHD 的 SC deviations 更集中在 sensorimotor-association connectional axis 的 association end。
- 部分 higher-order association connections 的 deviation 随年龄出现 ADHD-specific reduction。
- deviation 的变化与年龄相关的症状减轻有关，并可在个体内两年变化中追踪 symptom improvement。
- baseline deviations 预测 atomoxetine 12-week response，但未显示对 methylphenidate 有相同预测。
- follow-up imaging 显示治疗相关 deviation reduction。

### 学习意义
这是“正常发育轨迹 → 个体偏离 → longitudinal symptom tracking → treatment stratification”的完整 precision-development framework。  
重要边界：预测特定药物 response 需要在独立前瞻性研究中继续检验；不能把单篇研究直接视为临床已验证 biomarker。

---

# 这组论文共同形成的知识主线

```
group connectome
→ individual-specific topography
→ developmental refinement
→ cognition
→ psychopathology
→ structure-function constraints
→ sensorimotor-association hierarchy
→ normative deviation
→ symptom trajectory / treatment prediction
```

这条主线也是后续知识库阅读 Cui Lab 文献的默认组织方式。
