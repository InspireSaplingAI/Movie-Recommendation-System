"""Training loop and experiment tracking (starter).

Add training orchestration, logging, checkpointing, and config handling here.
"""

from typing import Any, Dict, Optional
import torch
import torch.nn as nn
from torch.utils.data import DataLoader


def train(model: Any, train_loader: Any, epochs: int = 1, device: str = 'cpu') -> Dict[str, Any]:
    """Placeholder training loop for PyTorch models.

    Args:
        model: PyTorch model to train
        train_loader: DataLoader with training batches
        epochs: Number of training epochs
        device: torch device (cpu or cuda)
    
    Returns:
        Training history dict with losses
        
    TODO: Implement basic PyTorch training loop
    Steps:
    1. Move model to device
    2. Create loss function (nn.BCELoss)
    3. Create optimizer (torch.optim.Adam)
    4. Initialize history dict with empty loss list
    5. For each epoch:
       - Set model to training mode
       - For each batch in train_loader:
         * Unpack batch: user_ids, item_ids, ratings
         * Move to device
         * Zero gradients
         * Forward pass
         * Compute loss
         * Backward pass
         * Update weights
       - Append average loss to history
    6. Return history dict
    """
    model = model.to(device)
    # YOUR CODE HERE
    
    history = {'train_loss': []}
    return history


if __name__ == "__main__":
    print("trainer module — implement model-specific training logic.")
