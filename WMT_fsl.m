% 加载扩散张量成像数据
dti_file = 'dti_file.nii.gz';
bvec_file = 'bvec_file.txt';
bval_file = 'bval_file.txt';

% 运行FSL的dtifit命令进行扩散张量拟合
dtifit_cmd = sprintf('dtifit -k %s -o dti -m mask_file.nii.gz -r %s -b %s', ...
    dti_file, bvec_file, bval_file);
system(dtifit_cmd);

% 运行FSL的bedpostx命令进行纤维束追踪
bedpostx_cmd = 'bedpostx bedpostx_input';
system(bedpostx_cmd);

% 运行FSL的probtrackx2命令进行纤维束追踪和重构
probtrackx2_cmd = sprintf('probtrackx2 -s bedpostx_input.bedpostX/merged -m mask_file.nii.gz -x seed_mask.nii.gz --dir=output_dir');
system(probtrackx2_cmd);
