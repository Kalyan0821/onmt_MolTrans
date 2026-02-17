"""Attention and normalization modules"""

from moltrans_onmt.modules.util_class import LayerNorm, Elementwise
from moltrans_onmt.modules.gate import context_gate_factory, ContextGate
from moltrans_onmt.modules.global_attention import GlobalAttention
from moltrans_onmt.modules.conv_multi_step_attention import ConvMultiStepAttention
from moltrans_onmt.modules.copy_generator import CopyGenerator, CopyGeneratorLossCompute
from moltrans_onmt.modules.multi_headed_attn import MultiHeadedAttention
from moltrans_onmt.modules.embeddings import Embeddings, PositionalEncoding
from moltrans_onmt.modules.weight_norm import WeightNormConv2d
from moltrans_onmt.modules.average_attn import AverageAttention

__all__ = [
    "LayerNorm",
    "Elementwise",
    "context_gate_factory",
    "ContextGate",
    "GlobalAttention",
    "ConvMultiStepAttention",
    "CopyGenerator",
    "CopyGeneratorLossCompute",
    "MultiHeadedAttention",
    "Embeddings",
    "PositionalEncoding",
    "WeightNormConv2d",
    "AverageAttention",
]
