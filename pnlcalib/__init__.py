"""Pip-installable shim re-exporting upstream PnLCalib symbols.

This module deliberately does NOT define a `PnLCalib` class. Downstream
consumers (e.g. futPuzzle's video pipeline) wrap the upstream surfaces in
their own adapter, so coupling the adapter to this fork's lifecycle would be
the wrong layering.

What you get from `import pnlcalib`:
    - `pnlcalib.inference`        — the upstream `inference()` function from
                                    `inference.py` (CLI script as a module).
    - `pnlcalib.FramebyFrameCalib` — calibration state machine.
    - `pnlcalib.get_cls_net`      — keypoint HRNet model loader.
    - `pnlcalib.get_cls_net_l`    — line HRNet model loader.

These imports are tolerant: if heavy upstream deps (torch, cv2, scipy) are
missing at import time, attribute access raises lazily so `import pnlcalib`
still succeeds in environments that only need the package marker.
"""
from __future__ import annotations

__all__ = [
    "inference",
    "FramebyFrameCalib",
    "get_cls_net",
    "get_cls_net_l",
]


def __getattr__(name: str):  # PEP 562 lazy attribute loader
    if name == "inference":
        from inference import inference as _inference  # type: ignore[import-not-found]
        return _inference
    if name == "FramebyFrameCalib":
        from utils.utils_calib import FramebyFrameCalib as _FbF  # type: ignore[import-not-found]
        return _FbF
    if name == "get_cls_net":
        from model.cls_hrnet import get_cls_net as _g  # type: ignore[import-not-found]
        return _g
    if name == "get_cls_net_l":
        from model.cls_hrnet_l import get_cls_net as _gl  # type: ignore[import-not-found]
        return _gl
    raise AttributeError(f"module 'pnlcalib' has no attribute {name!r}")
