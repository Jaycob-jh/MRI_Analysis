# 03 MRI

## A. MRI 基础
- proton / spin
- B0
- RF excitation
- T1 / T2 / T2*
- gradients
- k-space
- voxel / resolution
- SNR
- distortion / artifact

## B. 数据格式与空间
- DICOM
- NIfTI
- affine
- scanner/native space
- subject anatomical space
- template/MNI space
- BIDS

## C. Registration
- rigid / affine / nonlinear
- cost function
- interpolation
- transform composition
- inverse transform
- resampling
- QC

要能解释：**配准是估计变换；resampling 是应用变换后重新采样。**

## D. Structural MRI
- bias field correction
- skull stripping
- tissue segmentation
- cortical surface reconstruction
- cortical thickness
- volume / surface area
- FreeSurfer recon-all

## E. VBM / GMV
典型链条：

```
T1
→ bias correction
→ segmentation
→ GM probability map
→ spatial normalization
→ modulation
→ smoothing
→ voxel-wise GLM
→ multiple-comparison correction
```

重点问题：
- GM probability 和 GM volume 的区别
- Jacobian modulation
- native vs normalized space
- smoothing 对空间推断的意义

## F. fMRI
- BOLD / neurovascular coupling
- slice timing（何时需要）
- motion correction
- susceptibility distortion
- coregistration
- normalization
- nuisance regression
- filtering
- smoothing
- task GLM
- resting-state FC
- ICA
- individual-specific network topography

## G. dMRI
- diffusion sensitization
- b-value / b-vector
- tensor model
- FA / MD / AD / RD
- crossing fibers
- CSD
- tractography
- structural connectivity
- TBSS
- FBA

## H. 软件
- FSL
- FreeSurfer
- ANTs
- SPM
- AFNI
- MRtrix3
- DIPY

每个软件条目都应同时记录：
**算法原理、输入输出、关键参数、默认值、QC 和可重复性。**
