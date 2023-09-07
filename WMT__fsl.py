import numpy as np
import nibabel as nib
import dipy.reconst.dti as dti
import dipy.tracking.utils as ut
import dipy.tracking.streamline as sl
import dipy.tracking.streamlinespeed as spd

# 加载扩散张量成像数据
img = nib.load('dti_file.nii.gz')
data = img.get_fdata()
affine = img.affine

# 创建扩散张量模型
dti_model = dti.TensorModel(data, affine)

# 计算扩散张量
tensor_fit = dti_model.fit(data)

# 设置起点种子区域
seed_mask = data[..., 0] > 50

# 进行纤维束追踪
seeds = ut.seeds_from_mask(seed_mask, density=1)
streamlines = ut.track(tensor_fit, seeds, affine, step_size=0.5)

# 进行纤维束过滤
streamlines = sl.Streamlines(spd.compress_streamlines(streamlines, 0.1))

# 保存纤维束数据
tractogram = nib.streamlines.Tractogram(streamlines)
nib.streamlines.save(tractogram, 'output.trk')
