"""Neural Collaborative Filtering (NCF) model implementation using PyTorch.

This module implements the NCF framework combining:
1. Embedding layers for users and items (capturing latent factors)
2. Multi-layer perceptron (MLP) for non-linear interaction modeling
3. Output layer for rating prediction

Architecture:
    - User embedding + Item embedding → Concatenate
    - MLP layers (fully connected + ReLU activation)
    - Output layer (sigmoid for rating prediction)

Paper Reference: Neural Collaborative Filtering (He et al., 2017)
"""

import torch
import torch.nn as nn
from typing import Tuple, List, Optional


class NeuralCF(nn.Module):
    """Neural Collaborative Filtering model.
    
    Combines embedding layers and MLPs to learn user-item interactions
    in a non-linear fashion.
    
    Args:
        num_users: Number of unique users in the dataset
        num_items: Number of unique items in the dataset
        embedding_dim: Dimension of user and item embeddings (default: 32)
        mlp_hidden_dims: List of hidden layer dimensions for MLP (default: [128, 64, 32])
        dropout_rate: Dropout rate for regularization (default: 0.3)
    """
    
    def __init__(
        self,
        num_users: int,
        num_items: int,
        embedding_dim: int = 32,
        mlp_hidden_dims: Optional[List[int]] = None,
        dropout_rate: float = 0.3
    ):
        super(NeuralCF, self).__init__()
        
        self.num_users = num_users
        self.num_items = num_items
        self.embedding_dim = embedding_dim
        self.mlp_hidden_dims = mlp_hidden_dims or [128, 64, 32]
        self.dropout_rate = dropout_rate
        
        # ============ EMBEDDING LAYERS ============
        # TODO: Create user embedding layer using nn.Embedding
        # - num_embeddings: num_users
        # - embedding_dim: embedding_dim
        self.user_embedding = None
        
        # TODO: Create item embedding layer using nn.Embedding
        # - num_embeddings: num_items
        # - embedding_dim: embedding_dim
        self.item_embedding = None
        
        # TODO: Initialize both embeddings with normal distribution (std=0.01)
        # Hint: Use nn.init.normal_()
        
        # ============ MLP LAYERS ============
        # TODO: Build MLP layers dynamically using a loop
        # - Start with input_dim = embedding_dim * 2 (concatenated embeddings)
        # - For each hidden_dim in mlp_hidden_dims:
        #   * Add nn.Linear(input_dim, hidden_dim)
        #   * Add nn.ReLU() activation
        #   * Add nn.Dropout(dropout_rate)
        #   * Update input_dim = hidden_dim
        # - Store as self.mlp using nn.Sequential
        mlp_layers = []
        # YOUR CODE HERE
        self.mlp = None
        
        # ============ OUTPUT LAYER ============
        # TODO: Create output layer
        # - Maps from mlp_hidden_dims[-1] to 1 (single prediction)
        self.output = None
        
        # TODO: Create sigmoid activation layer
        self.sigmoid = None
    
    def forward(self, user_ids: torch.Tensor, item_ids: torch.Tensor) -> torch.Tensor:
        """Forward pass through the NCF model.
        
        Args:
            user_ids: Tensor of user indices (shape: [batch_size])
            item_ids: Tensor of item indices (shape: [batch_size])
        
        Returns:
            Predicted interaction scores (shape: [batch_size, 1])
        """
        # TODO: Step 1 - Get user embeddings from indices
        # Hint: user_embed = self.user_embedding(user_ids)
        user_embed = None
        
        # TODO: Step 2 - Get item embeddings from indices
        item_embed = None
        
        # TODO: Step 3 - Concatenate embeddings along dimension 1
        # Result should be [batch_size, 2*embedding_dim]
        x = None
        
        # TODO: Step 4 - Pass through MLP layers
        x = None
        
        # TODO: Step 5 - Apply output layer and sigmoid activation
        # Hint: sigmoid(output(x))
        output = None
        
        return output
    
    def get_user_embeddings(self) -> torch.Tensor:
        """Get all user embedding vectors.
        
        Useful for similarity computations and analysis.
        
        TODO: Return user embedding weights (detached from computation graph)
        """
        # YOUR CODE HERE
        pass
    
    def get_item_embeddings(self) -> torch.Tensor:
        """Get all item embedding vectors.
        
        Useful for similarity computations and analysis.
        
        TODO: Return item embedding weights (detached from computation graph)
        """
        # YOUR CODE HERE
        pass


class NCFTrainer:
    """Trainer class for Neural Collaborative Filtering models.
    
    Handles training loops, validation, and checkpointing.
    
    Args:
        model: NeuralCF model instance
        device: torch device (cpu or cuda)
        learning_rate: Learning rate for optimizer (default: 0.001)
        use_amp: Whether to use automatic mixed precision (default: False)
    """
    
    def __init__(
        self,
        model: NeuralCF,
        device: str = 'cpu',
        learning_rate: float = 0.001,
        use_amp: bool = False
    ):
        self.model = model.to(device)
        self.device = device
        self.use_amp = use_amp
        
        # TODO: Initialize Binary Cross-Entropy loss
        # Hint: self.criterion = nn.BCELoss()
        self.criterion = None
        
        # TODO: Initialize Adam optimizer
        # Hint: self.optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
        self.optimizer = None
        
        # Optional mixed precision support
        if use_amp:
            self.scaler = torch.cuda.amp.GradScaler()
        else:
            self.scaler = None
        
        # Training history
        self.train_losses = []
        self.val_losses = []
        self.best_val_loss = float('inf')
    
    def train_epoch(self, train_loader) -> float:
        """Train for one epoch.
        
        Args:
            train_loader: DataLoader with training batches (user_id, item_id, rating)
        
        Returns:
            Average training loss for the epoch
            
        TODO: Implement the training loop
        Steps:
        1. Set model to training mode (model.train())
        2. Loop through batches in train_loader
        3. For each batch (user_ids, item_ids, ratings):
           - Move tensors to device
           - Reshape ratings to [batch_size, 1]
           - Zero gradients (optimizer.zero_grad())
           - Forward pass (predictions = model(user_ids, item_ids))
           - Compute loss (loss = criterion(predictions, ratings))
           - Backward pass (loss.backward())
           - Update weights (optimizer.step())
           - Accumulate loss
        4. Return average loss
        """
        self.model.train()
        total_loss = 0.0
        num_batches = 0
        
        # YOUR CODE HERE
        
        avg_loss = total_loss / max(num_batches, 1)
        self.train_losses.append(avg_loss)
        return avg_loss
    
    def validate(self, val_loader) -> float:
        """Validate the model on validation set.
        
        Args:
            val_loader: DataLoader with validation batches
        
        Returns:
            Average validation loss
            
        TODO: Implement validation loop
        Steps:
        1. Set model to evaluation mode (model.eval())
        2. Use torch.no_grad() context to disable gradients
        3. Loop through validation batches
        4. Compute loss (same as training but NO weight updates)
        5. Return average loss
        """
        self.model.eval()
        total_loss = 0.0
        num_batches = 0
        
        # YOUR CODE HERE
        
        avg_loss = total_loss / max(num_batches, 1)
        self.val_losses.append(avg_loss)
        return avg_loss
    
    def fit(
        self,
        train_loader,
        val_loader,
        epochs: int = 10,
        early_stopping_patience: int = 3,
        verbose: bool = True
    ) -> Tuple[List[float], List[float]]:
        """Train the model with early stopping.
        
        Args:
            train_loader: Training data loader
            val_loader: Validation data loader
            epochs: Number of training epochs
            early_stopping_patience: Stop if validation loss doesn't improve for N epochs
            verbose: Print training progress
        
        Returns:
            Tuple of (train_losses, val_losses)
            
        TODO: Implement the main training loop with early stopping
        Steps:
        1. Initialize patience_counter = 0
        2. For each epoch:
           - Call train_epoch(train_loader) to get train_loss
           - Call validate(val_loader) to get val_loss
           - If val_loss < best_val_loss:
             * Update best_val_loss = val_loss
             * Reset patience_counter = 0
           - Else:
             * Increment patience_counter
             * If patience_counter >= early_stopping_patience: BREAK
           - (Optional) Print progress
        3. Return train_losses, val_losses
        """
        patience_counter = 0
        
        # YOUR CODE HERE
        
        return self.train_losses, self.val_losses
    
    def predict(self, user_ids: torch.Tensor, item_ids: torch.Tensor) -> torch.Tensor:
        """Make predictions in evaluation mode.
        
        Args:
            user_ids: Tensor of user indices
            item_ids: Tensor of item indices
        
        Returns:
            Predicted interaction scores
            
        TODO: Implement prediction
        Steps:
        1. Set model to evaluation mode (model.eval())
        2. Use torch.no_grad() context
        3. Get predictions from model
        4. Return predictions
        """
        self.model.eval()
        # YOUR CODE HERE
        pass
