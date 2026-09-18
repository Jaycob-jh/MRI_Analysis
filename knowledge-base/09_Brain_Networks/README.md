# 09 Brain Networks

## 1. Network construction

### Nodes
- atlas parcels
- individualized parcels
- EEG/MEG sources
- white-matter tracts
- electrodes

### Edges
- structural connectivity
- Pearson FC
- partial correlation
- coherence
- phase synchronization
- effective connectivity

节点与边的定义决定后续所有图指标的解释。

## 2. Basic Metrics
- degree / strength
- clustering coefficient
- path length
- global/local efficiency
- betweenness
- participation coefficient
- modularity
- rich club

## 3. Threshold / Density
binary graph、weighted graph、fixed threshold、fixed density 会产生不同网络。

必须做 sensitivity analysis，并报告：
- negative weights 怎么处理
- disconnected graph 怎么处理
- weight→distance 怎么转换

## 4. Community
- modularity maximization
- Louvain / Leiden
- consensus clustering
- resolution parameter
- stochasticity

## 5. Network Inference

### Edge-wise
- FDR
- permutation max-T

### NBS
```
edge-wise statistic
→ primary threshold
→ connected components
→ component extent/intensity
→ permutation max component
→ component-level FWE
```

NBS 显著 ≠ component 中每条 edge individually FWE significant。

### TFNBS
将 TFCE 类思想移到 graph edges 上。

## 6. Spatial Null Models
- spin test
- Moran spectral randomization
- BrainSMASH

用于皮层图空间相关问题；不能把空间平滑 ROI 当独立样本。

## 7. Structure-Function Coupling
- edge/node-level coupling
- structural constraints on FC
- generative model
- graph neural networks

## 8. Network Control Theory
- state
- control input
- transition energy
- controllability
- structural connectome as dynamical constraint

## 9. Dynamic Networks
- sliding window
- HMM
- state-space model
- multilayer networks

## 10. 个体化网络
- NMF
- MS-HBM
- Infomap
- group atlas vs individual atlas
- reliability
- acquisition duration
- topographic variability

重点：个体化网络的“边界不同”会改变 FC 与认知/症状解释，不能把 atlas mismatch 当成真实 connectivity difference。
