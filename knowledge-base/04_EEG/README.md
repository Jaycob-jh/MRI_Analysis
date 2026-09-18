# 04 EEG

## 1. EEG 测量的是什么？
头皮 EEG 记录的是电极之间的电势差，主要反映大规模同步突触电流经过体积传导后的场效应，而不是“单个神经元放电”。

## 2. Acquisition
- electrode montage
- impedance
- reference
- ground
- sampling rate
- analog/digital filtering
- trigger synchronization

### Reference 是核心概念
EEG 每个通道本质上都是相对参考电极的电位差，因此重新参考会改变全部通道数值与拓扑。

## 3. Preprocessing
- bad channel detection
- high/low-pass filter
- notch filter
- rereferencing
- artifact rejection
- ICA / SSP
- ocular / cardiac / muscle artifact
- epoching
- baseline correction

重点：
- filter edge artifact
- phase delay
- zero-phase 的含义
- ICA component removal 的可解释边界

## 4. ERP
```
event-locked epochs
→ baseline
→ artifact control
→ averaging
→ amplitude / latency
→ statistical inference
```

平均能提高 event-locked signal 的 SNR，但不会自动消除系统性伪迹。

## 5. Time-Frequency
- Fourier
- STFT
- Morlet wavelet
- induced vs evoked power
- baseline normalization
- ITPC
- theta / alpha / beta / gamma

理解核心：时间和频率分辨率存在 trade-off。

## 6. Connectivity
- correlation
- coherence
- PLV
- PLI / wPLI
- amplitude envelope correlation
- Granger（谨慎解释）
- cross-frequency coupling

必须处理：
- volume conduction
- common reference
- source leakage
- multiple comparisons

## 7. Source Localization
- head model
- forward solution
- inverse problem
- minimum norm
- beamformer
- regularization

## 8. Statistics
- sensor × time
- sensor × time × frequency
- cluster permutation
- ROI/source-space model
- LME for trials/subjects
