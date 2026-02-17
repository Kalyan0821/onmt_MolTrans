"""Module defining encoders."""

from moltrans_onmt.encoders.encoder import EncoderBase
from moltrans_onmt.encoders.transformer import TransformerEncoder
from moltrans_onmt.encoders.rnn_encoder import RNNEncoder
from moltrans_onmt.encoders.cnn_encoder import CNNEncoder
from moltrans_onmt.encoders.mean_encoder import MeanEncoder

__all__ = [
    "EncoderBase",
    "TransformerEncoder",
    "RNNEncoder",
    "CNNEncoder",
    "MeanEncoder",
]
