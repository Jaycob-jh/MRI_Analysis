# 05 MEG

MEG 测量神经电流产生的极弱磁场，和 EEG 共享许多神经生理基础，但传感器物理、噪声处理与 forward model 不同。

## 核心主题

### Sensors
- SQUID
- OPM
- magnetometer
- planar gradiometer

### Noise / preprocessing
- environmental noise
- head movement
- Signal Space Separation (SSS / tSSS)
- SSP
- ICA
- filtering
- epoching

### ERF 与时频
- evoked field
- induced oscillation
- wavelet / multitaper
- phase locking

### Source Reconstruction
- forward model
- cortical source orientation
- MNE/dSPM/sLORETA
- beamformer
- source leakage

### Connectivity
- coherence
- phase coupling
- amplitude envelope connectivity
- leakage correction
- dynamic connectivity

## EEG vs MEG 需要真正理解的差异
- 电场 vs 磁场测量
- 头皮/颅骨导电特性影响不同
- source orientation sensitivity 不同
- reference 问题：EEG 强、MEG 不同
- inverse problem 仍然存在
