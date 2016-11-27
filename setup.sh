#!/usr/bin/env bash

# create and own the directories to store results locally
export save_dir='/var/lib/tfchatbot1127'
sudo rm -f -r $save_dir
sudo mkdir -p $save_dir'/data/'
sudo mkdir -p $save_dir'/nn_models/'
sudo mkdir -p $save_dir'/results/'
sudo chown -R "$USER" $save_dir

# copy train and test data with proper naming
export data_dir='tf_seq2seq_chatbot/data'
cp $data_dir'/chat.in' $save_dir'/data/chat.in'
cp $data_dir'/chat_test.in' $save_dir'/data/chat_test.in'