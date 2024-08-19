import pandas as pd
import os
import glob
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Process TPM data for HC and UC samples.")
parser.add_argument('--data_info', type=str, required=True, help='Path to the CSV file containing sample information')
parser.add_argument('--data_dirs', type=str, nargs='+', required=True, help='List of directories containing TPM data files')
parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the combined data')

args = parser.parse_args()
data_info_path = args.data_info
data_dirs = args.data_dirs
output_dir = args.output_dir

# 输出目录
os.makedirs(output_dir, exist_ok=True)

# 读取CSV文件(所有样本的信息)
data_info = pd.read_csv(data_info_path)

# 根据样本的特征分组
hc_samples = data_info[data_info['Sample_Character_2'] == 'diagnosis: Control']
uc_samples = data_info[data_info['Sample_Character_2'] == 'diagnosis: Ulcerative Colitis']
print(f"HC samples: {len(hc_samples)}")
print(f"UC samples: {len(uc_samples)}")

# 读取TPM文件
def read_tpm_file(gsm_id, data_dirs):
    for data_dir in data_dirs:
        file_pattern = f"{gsm_id}_*.txt"
        matched_files = glob.glob(os.path.join(data_dir, file_pattern))
        if matched_files:
            file_path = matched_files[0]  # 假设只有一个匹配文件
            return pd.read_csv(file_path, sep="\t", index_col=0, header=None)
    print(f"No files found for GSM ID: {gsm_id} in provided directories")
    return None

# 合并HC组
hc_samples_data = []
for gsm_id in hc_samples['Sample_geo_accession']:
    sample_data = read_tpm_file(gsm_id, data_dirs)
    if sample_data is not None:
        sample_data.columns = [gsm_id]  # 使用GSM作为列名
        hc_samples_data.append(sample_data)
    else:
        print(f"Failed to read data for GSM ID: {gsm_id}")

combined_hc_data = pd.concat(hc_samples_data, axis=1)

hc_output_path = os.path.join(output_dir, 'combined_hc_data.csv')
combined_hc_data.to_csv(hc_output_path)
print(f"Combined HC data saved to {hc_output_path}")

# 合并UC组
uc_samples_data = []
for gsm_id in uc_samples['Sample_geo_accession']:
    sample_data = read_tpm_file(gsm_id, data_dirs)
    if sample_data is not None:
        sample_data.columns = [gsm_id]  # 使用GSM作为列名
        uc_samples_data.append(sample_data)
    else:
        print(f"Failed to read data for GSM ID: {gsm_id}")

combined_uc_data = pd.concat(uc_samples_data, axis=1)

uc_output_path = os.path.join(output_dir, 'combined_uc_data.csv')
combined_uc_data.to_csv(uc_output_path)
print(f"Combined UC data saved to {uc_output_path}")

print(combined_hc_data.head())
print(combined_uc_data.head())