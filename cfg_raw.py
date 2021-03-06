import os
import time

#data config
input_dir = '/media/gtmeng/DataDisk2/Learning-to-See-in-the-Dark/short'
gt_dir = '/media/gtmeng/DataDisk2/Learning-to-See-in-the-Dark/long'
train_crop_size=256


#train config
input_channels=4
seed=0
train_batch_size=4
data_loader_num_workers=4
base_lr=1e-4
momentum=0.9
total_epochs=4000
lr_decay_epochs=[1000,2000]
lr_decay_rate=0.1
model_save_interval=50
model_save_path='./snapshots_raw'
vgg_output_layer_list=[2,7,16,25]
loss_c_ratio=0.1

if not os.path.exists(model_save_path):
    os.mkdir(model_save_path)

log_interval=4
time_str=time.asctime( time.localtime(time.time()))
log_dir=os.path.join('logs/runs_raw','-'.join(time_str.split()[1:-1]))

demosaic=True

start_epoch=1
for epoch in lr_decay_epochs:
    if epoch<=start_epoch:
        base_lr*=lr_decay_rate

if start_epoch>1:
    snapshot_path=os.path.join(model_save_path,'model_%05d.pth'%(start_epoch-1))
else:
    snapshot_path=None
