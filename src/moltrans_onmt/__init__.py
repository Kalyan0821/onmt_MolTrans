"""Main entry point of the ONMT library"""

from __future__ import division, print_function

import moltrans_onmt.inputters
import moltrans_onmt.encoders
import moltrans_onmt.decoders
import moltrans_onmt.models
import moltrans_onmt.utils
import moltrans_onmt.modules
from moltrans_onmt.trainer import Trainer
import sys
import moltrans_onmt.utils.optimizers

moltrans_onmt.utils.optimizers.Optim = moltrans_onmt.utils.optimizers.Optimizer
sys.modules["moltrans_onmt.Optim"] = moltrans_onmt.utils.optimizers

# For Flake
__all__ = [
    moltrans_onmt.inputters,
    moltrans_onmt.encoders,
    moltrans_onmt.decoders,
    moltrans_onmt.models,
    moltrans_onmt.utils,
    moltrans_onmt.modules,
    "Trainer",
]

__version__ = "0.4.1"
