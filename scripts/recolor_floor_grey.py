#!/usr/bin/env python3
"""Recolorea el terra ceràmic (beige) a gris greige mantenint lluminància i textura."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


# Gris greige porcelànic (referència RSM)
TARGET_RGB = np.array([142, 140, 136], dtype=np.float32)


def rgb_to_lab(rgb: np.ndarray) -> np.ndarray:
    """RGB [0,255] -> LAB (simplificat, suficient per distància)."""
    x = rgb / 255.0
    def lin(c: np.ndarray) -> np.ndarray:
        return np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)

    r, g, b = lin(x[..., 0]), lin(x[..., 1]), lin(x[..., 2])
    X = r * 0.4124 + g * 0.3576 + b * 0.1805
    Y = r * 0.2126 + g * 0.7152 + b * 0.0722
    Z = r * 0.0193 + g * 0.1192 + b * 0.9505
    X, Y, Z = X / 0.95047, Y / 1.0, Z / 1.08883

    def f(t: np.ndarray) -> np.ndarray:
        return np.where(t > 0.008856, t ** (1 / 3), 7.787 * t + 16 / 116)

    fx, fy, fz = f(X), f(Y), f(Z)
    L = 116 * fy - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)
    return np.stack([L, a, b], axis=-1)


def build_floor_mask(rgb: np.ndarray) -> np.ndarray:
    h, w, _ = rgb.shape
    yy = np.arange(h, dtype=np.float32)[:, None]
    xx = np.arange(w, dtype=np.float32)[None, :]

    # Mostres de color del terra (beix original)
    patches = []
    for sy, sx in ((0.82, 0.35), (0.88, 0.55), (0.90, 0.75)):
        py, px = int(h * sy), int(w * sx)
        patches.append(rgb[py - 8 : py + 8, px - 12 : px + 12].reshape(-1, 3))
    ref_lab = np.median(rgb_to_lab(np.vstack(patches)), axis=0)

    lab = rgb_to_lab(rgb)
    dist = np.linalg.norm(lab - ref_lab, axis=-1)

    # Terra: zona baixa de la imatge
    roi = yy >= h * 0.58
    mask = roi & (dist < 30)

    # Exclou moble lavabo (fusta) i WC
    vanity = (xx > w * 0.46) & (yy > h * 0.30) & (yy < h * 0.80)
    toilet = (xx > w * 0.38) & (xx < w * 0.62) & (yy > h * 0.38) & (yy < h * 0.72)
    mask &= ~(vanity | toilet)

    # Exclou plat de dutxa (molt clar, centre fons)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    shower = (
        (yy > h * 0.50)
        & (xx > w * 0.22)
        & (xx < w * 0.72)
        & (r > 195)
        & (g > 195)
        & (b > 195)
    )
    mask &= ~shower

    # Exclou parets i sostre (molt clars, baixa croma)
    chroma = np.max(rgb, axis=-1) - np.min(rgb, axis=-1)
    wallish = (chroma < 20) & (np.min(rgb, axis=-1) > 195)
    mask &= ~wallish

    # Permet terra sota el moble (franja baixa dreta)
    under_vanity = (xx > w * 0.44) & (yy > h * 0.78)
    mask |= under_vanity & (dist < 32)

    mask_u8 = (mask.astype(np.uint8) * 255)
    m = Image.fromarray(mask_u8)
    m = m.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
    return np.array(m) > 127


def recolor_floor(img: Image.Image) -> Image.Image:
    rgb = np.array(img.convert("RGB"), dtype=np.float32)
    mask = build_floor_mask(rgb)

    lum = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
    lum_ref = np.median(lum[mask]) if mask.any() else 160.0
    scale = np.clip(lum / max(lum_ref, 1.0), 0.75, 1.25)

    out = rgb.copy()
    for c in range(3):
        out[..., c] = np.where(mask, TARGET_RGB[c] * scale, out[..., c])

    # Suavitza només vores de la màscara (no les parets)
    mask_u8 = (mask.astype(np.uint8) * 255)
    mask_blur = (
        np.array(Image.fromarray(mask_u8).filter(ImageFilter.GaussianBlur(1)), dtype=np.float32)
        / 255.0
    )[..., None]
    out = out * mask_blur + rgb * (1.0 - mask_blur)

    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "assets/pe/bany_p2_pe_definitiu.png"
    if not src.is_absolute():
        src = root / src
    dst = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else src.with_name(src.stem + "_terra_gris" + src.suffix)
    )
    if not dst.is_absolute():
        dst = root / dst

    result = recolor_floor(Image.open(src))
    result.save(dst, optimize=True)
    print(f"Guardat: {dst}")


if __name__ == "__main__":
    main()
