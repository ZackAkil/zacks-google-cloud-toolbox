#!/bin/bash

# This script downloads a TensorFlow Lite AutoML model from Google Cloud Storage to a local file.

# Usage:
#   automl_tflite_downloader.sh <model_id> <bucket> <output_path>

# Arguments:
#   model_id: The ID of the AutoML model to download.
#   bucket: The name of the Google Cloud Storage bucket containing the model.
#   output_path: The path to the local file where the model will be saved.

# Example:
#   ./automl_tflite_downloader.sh 289029380890482 my-bucket model.tflite

# Exit codes:
#   0: The script completed successfully.
#   1: The specified model was not found.


model_id=$1
bucket=$2
output_path=$3

echo "Looking for model [$model_id] in bucket [$bucket] and save to [$output_path]"

gs_path="gs://$bucket/model-$model_id/**"

echo "🔎 Listing files in $gs_path"

model_path=$(gsutil ls $gs_path | head -n 1)

if [ -z "$model_path" ]; then
  echo "❌ No model found"
  exit 1
fi

echo "☑️ Found model $model_path"

echo "💾 Downloading $model_path --> $output_path..."

gsutil cp $model_path $output_path

echo "✅ Model downloaded and saved to $output_path"
