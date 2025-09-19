"""
tests/test_build_edges.py

Unit tests for adjacency detection in build_edges.py.
"""

import pytest
from src.build_edges import is_adjacent

def test_single_modification_loss_gain():
    assert is_adjacent("K9me1", "")        # removal
    assert is_adjacent("", "K9me1")        # addition

def test_residue_state_change():
    assert is_adjacent("K9me1", "K9me2")   # same residue, diff state
    assert is_adjacent("K27me2", "K27me3") # higher order methylation

def test_multiple_modifications():
    assert is_adjacent("K9me1 K14ac", "K9me1")   # loss of K14ac
    assert is_adjacent("K9me1", "K9me1 K14ac")   # gain of K14ac

def test_non_adjacent_cases():
    assert not is_adjacent("K9me1", "K14ac")     # different residues
    assert not is_adjacent("K9me1 K14ac", "K9me2 K14ac") # 2 changes
    assert not is_adjacent("K9me1", "K14me1")    # different residues

