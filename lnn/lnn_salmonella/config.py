"""
Global configuration file for LNN Salmonella Detection.

All hyperparameters and data paths are configured here.
Set environment variable LNN_DATA_DIR to override the default data directory.
"""
import os
from pathlib import Path

# === Project Paths ===
ROOT = Path(__file__).parent.parent  # Repository root

# Data directory: set via environment variable or place data alongside the repo
# export LNN_DATA_DIR=/path/to/your/data
DATA_DIR = Path(os.environ.get("LNN_DATA_DIR", ROOT / "data"))

# Raw genome directories (subdirectories of DATA_DIR)
SEROTYPE_DIR = DATA_DIR / "serotype_data"
NEGATIVE_DIR = DATA_DIR / "negative_species"
ZHENG_DIR = DATA_DIR / "zheng-yangpin"
FU_DIR = DATA_DIR / "fu-yangpin"

# Cache directory (pre-computed k-mer vectors)
CACHE_DIR = Path(__file__).parent / "data" / "cache"

# Results directory
RESULTS_DIR = Path(__file__).parent / "results"

# === k-mer Encoding ===
KMER_K = 4                        # k-mer length
KMER_DIM = 4 ** KMER_K            # k-mer feature dimension (256 for k=4)
SEQ_LENGTH = 1024                 # DNA sequence fixed length for one-hot encoding

# === Sequence Modeling ===
NUM_CHUNKS_PER_GENOME = 32        # Number of chunks per genome (time steps for CfC/LSTM/Transformer)

# === Training Parameters ===
BATCH_SIZE = 256
LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-4
DROPOUT = 0.1
EPOCHS = 100
EARLY_STOP_PATIENCE = 15
GRAD_CLIP_NORM = 1.0
WARMUP_STEPS = 500

# === Data Split ===
TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15
RANDOM_SEED = 42

# === Model Architecture ===
CFC_HIDDEN_SIZES = [128, 64, 32]  # CfC layer hidden state dimensions
LSTM_HIDDEN = 128
CNN_CHANNELS = [64, 128, 256]
TRANSFORMER_DIM = 128
TRANSFORMER_HEADS = 4
TRANSFORMER_LAYERS = 4

# === Device ===
import torch
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# === Class Mappings ===
SEROTYPE_CLASSES = [
    "dublin", "enteritidis", "heidelberg",
    "infantis", "newport", "typhimurium"
]
NEGATIVE_CLASSES = [
    "enterococcus_faecalis", "klebsiella_pneumoniae",
    "listeria_monocytogenes", "pseudomonas_aeruginosa",
    "shigella_flexneri", "staphylococcus_aureus"
]
NUM_SEROTYPES = len(SEROTYPE_CLASSES)
