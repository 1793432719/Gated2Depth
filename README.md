For running the evaluation and visualization code you need Python with the following packages:
- tensorflow
- numpy
- cv2
- matplotlib

Download the Gated2Depth dataset and the models from the [DENSE dataset webpage](https://www.uni-ulm.de/en/in/driveu/projects/dense-datasets). 
Check if you have downloaded all files. Then, you can unzip your downloaded files.
```
bash scripts/unzip_real.sh <your_real_data_download_folder>
bash scripts/unzip_syn.sh <your_syn_data_download_folder>
bash scripts/unzip_models.sh <your_models_download_folder>
```

After unzipping the files, your directory should look like this:
```
.
|-- data
    |-- real
        |-- depth_hdl64_gated_compressed
        |-- gated0_10bit
        |-- gated1_10bit
        |-- gated2_10bit
        |-- rgb_left_8bit
        |-- rgb_right_8bit
    |-- sim
        |-- depth_compressed
        |-- gated0_10bit
        |-- gated1_10bit
        |-- gated2_10bit
        |-- rgb_left_8bit
        |-- rgb_right_8bit
|-- example
        |-- depth_hdl64_gated_compressed
        	|-- example.npz
        |-- gated0_10bit
        	|-- example.png
        |-- gated1_10bit
        	|-- example.png
        |-- gated2_10bit
        	|-- example.png
        |-- rgb_left_8bit
        	|-- example.png
|-- models
	|-- gated2depth_real_day
	|-- gated2depth_real_night
	|-- gated2depth_syn_day
	|-- gated2depth_syn_night
|-- splits
	|-- example.txt
        |-- real_test_day.txt
        |-- real_test_night.txt
	|-- real_train_day.txt
        |-- real_train_night.txt
	|-- real_val_day.txt
        |-- real_val_night.txt
        |-- syn_test_day.txt
        |-- syn_test_night.txt
	|-- syn_train_day.txt
        |-- syn_train_night.txt
	|-- syn_val_day.txt
        |-- syn_val_night.txt
|-- src
```
## Quick Example
Infer the depth for a single example:
```
./run_example.sh
```
## Training
Train a model on real data from scratch with:
```
./run_train_real.sh
```
Train a model that has been pretrained on synthetic data (pretrained model weights and fixed discriminator):
```
./run_train_real_pretrained.sh
```
## Evaluation

Evaluate on real data:
```
./run_eval_real.sh
```
