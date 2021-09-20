#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.

from augly.image.composition import Compose, OneOf
from augly.image.functional import (
    apply_lambda,
    apply_pil_filter,
    blur,
    brightness,
    change_aspect_ratio,
    clip_image_size,
    color_jitter,
    contrast,
    convert_color,
    crop,
    distort_barrel,
    distort_pincushion,
    encoding_quality,
    grayscale,
    hflip,
    masked_composite,
    meme_format,
    opacity,
    overlay_emoji,
    overlay_image,
    overlay_onto_background_image,
    overlay_onto_screenshot,
    overlay_stripes,
    overlay_text,
    pad,
    pad_square,
    perspective_transform,
    pixelization,
    random_noise,
    resize,
    rotate,
    saturation,
    scale,
    sharpen,
    shuffle_pixels,
    vflip,
)
from augly.image.helpers import aug_np_wrapper
from augly.image.intensity import (
    apply_lambda_intensity,
    apply_pil_filter_intensity,
    blur_intensity,
    brightness_intensity,
    change_aspect_ratio_intensity,
    clip_image_size_intensity,
    color_jitter_intensity,
    contrast_intensity,
    convert_color_intensity,
    crop_intensity,
    distort_barrel_intensity,
    distort_pincushion_intensity,
    encoding_quality_intensity,
    grayscale_intensity,
    hflip_intensity,
    masked_composite_intensity,
    meme_format_intensity,
    opacity_intensity,
    overlay_emoji_intensity,
    overlay_image_intensity,
    overlay_onto_background_image_intensity,
    overlay_onto_screenshot_intensity,
    overlay_stripes_intensity,
    overlay_text_intensity,
    pad_intensity,
    pad_square_intensity,
    perspective_transform_intensity,
    pixelization_intensity,
    random_noise_intensity,
    resize_intensity,
    rotate_intensity,
    saturation_intensity,
    scale_intensity,
    sharpen_intensity,
    shuffle_pixels_intensity,
    vflip_intensity,
)
from augly.image.transforms import (
    ApplyLambda,
    ApplyPILFilter,
    Blur,
    Brightness,
    ChangeAspectRatio,
    ClipImageSize,
    ColorJitter,
    Contrast,
    ConvertColor,
    Crop,
    DistortBarrel,
    DistortPincushion,
    EncodingQuality,
    Grayscale,
    HFlip,
    MaskedComposite,
    MemeFormat,
    Opacity,
    OverlayEmoji,
    OverlayImage,
    OverlayOntoBackgroundImage,
    OverlayOntoScreenshot,
    OverlayStripes,
    OverlayText,
    Pad,
    PadSquare,
    PerspectiveTransform,
    Pixelization,
    RandomAspectRatio,
    RandomBlur,
    RandomBrightness,
    RandomEmojiOverlay,
    RandomNoise,
    RandomPixelization,
    RandomRotation,
    Resize,
    Rotate,
    Saturation,
    Scale,
    Sharpen,
    ShufflePixels,
    VFlip,
)


__all__ = [
    "ApplyLambda",
    "ApplyPILFilter",
    "Blur",
    "Brightness",
    "ChangeAspectRatio",
    "ClipImageSize",
    "ColorJitter",
    "Compose",
    "Contrast",
    "ConvertColor",
    "Crop",
    "DistortBarrel",
    "DistortPincushion",
    "EncodingQuality",
    "Grayscale",
    "HFlip",
    "MaskedComposite",
    "MemeFormat",
    "OneOf",
    "Opacity",
    "OverlayEmoji",
    "OverlayImage",
    "OverlayOntoBackgroundImage",
    "OverlayOntoScreenshot",
    "OverlayStripes",
    "OverlayText",
    "Pad",
    "PadSquare",
    "PerspectiveTransform",
    "Pixelization",
    "RandomAspectRatio",
    "RandomBlur",
    "RandomBrightness",
    "RandomEmojiOverlay",
    "RandomNoise",
    "RandomPixelization",
    "RandomRotation",
    "Resize",
    "Rotate",
    "Saturation",
    "Scale",
    "Sharpen",
    "ShufflePixels",
    "VFlip",
    "apply_lambda",
    "apply_pil_filter",
    "aug_np_wrapper",
    "blur",
    "brightness",
    "change_aspect_ratio",
    "clip_image_size",
    "color_jitter",
    "contrast",
    "convert_color",
    "crop",
    "distort_barrel",
    "distort_pincushion",
    "encoding_quality",
    "grayscale",
    "hflip",
    "masked_composite",
    "meme_format",
    "opacity",
    "overlay_emoji",
    "overlay_image",
    "overlay_onto_background_image",
    "overlay_onto_screenshot",
    "overlay_stripes",
    "overlay_text",
    "pad",
    "pad_square",
    "perspective_transform",
    "pixelization",
    "random_noise",
    "resize",
    "rotate",
    "saturation",
    "scale",
    "sharpen",
    "shuffle_pixels",
    "vflip",
    "apply_lambda_intensity",
    "apply_pil_filter_intensity",
    "blur_intensity",
    "brightness_intensity",
    "change_aspect_ratio_intensity",
    "clip_image_size_intensity",
    "color_jitter_intensity",
    "contrast_intensity",
    "convert_color_intensity",
    "crop_intensity",
    "distort_barrel_intensity",
    "distort_pincushion_intensity",
    "encoding_quality_intensity",
    "grayscale_intensity",
    "hflip_intensity",
    "masked_composite_intensity",
    "meme_format_intensity",
    "opacity_intensity",
    "overlay_emoji_intensity",
    "overlay_image_intensity",
    "overlay_onto_background_image_intensity",
    "overlay_onto_screenshot_intensity",
    "overlay_stripes_intensity",
    "overlay_text_intensity",
    "pad_intensity",
    "pad_square_intensity",
    "perspective_transform_intensity",
    "pixelization_intensity",
    "random_noise_intensity",
    "resize_intensity",
    "rotate_intensity",
    "saturation_intensity",
    "scale_intensity",
    "sharpen_intensity",
    "shuffle_pixels_intensity",
    "vflip_intensity",
]
