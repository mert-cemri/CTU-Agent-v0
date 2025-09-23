#!/bin/bash

# Exit on any error
set -e

echo "Starting CTU Agent setup..."

# Download and install Miniconda
echo "Downloading Miniconda..."
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

echo "Installing Miniconda..."
bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda3

# Initialize conda
echo "Initializing conda..."
~/miniconda3/bin/conda init

# Source bashrc to make conda available
echo "Sourcing bashrc..."
source ~/.bashrc

# Accept conda terms of service
echo "Accepting conda terms of service..."
~/miniconda3/bin/conda config --set channel_priority strict
yes | ~/miniconda3/bin/conda install conda-build

# Clone the repository
echo "Cloning CTU-Agent repository..."
git clone https://github.com/test/CTU-Agent-v0.git

# Create conda environment
echo "Creating conda environment..."
~/miniconda3/bin/conda create -n ctu -y python=3.12

# Activate environment and install packages
echo "Activating environment and installing packages..."
source ~/miniconda3/bin/activate ctu

cd CTU-Agent-v0/SkyRL_mod/skyrl-train/

# Install packages
echo "Installing Python packages..."
pip install -e .
pip install vllm==0.10.0
pip install litellm

cd ../..

# Install tmux
echo "Installing tmux..."
sudo apt update
yes | sudo apt install tmux

echo "Setup completed successfully!"
echo "To activate the environment in future sessions, run:"
echo "conda activate ctu"
