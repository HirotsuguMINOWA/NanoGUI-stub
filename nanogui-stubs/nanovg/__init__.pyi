"""NanoVG bindings"""
from __future__ import annotations
import nanogui.nanovg
import typing
import nanogui

__all__ = [
    "ALIGN_BASELINE",
    "ALIGN_BOTTOM",
    "ALIGN_CENTER",
    "ALIGN_LEFT",
    "ALIGN_MIDDLE",
    "ALIGN_RIGHT",
    "ALIGN_TOP",
    "ATOP",
    "BEVEL",
    "BUTT",
    "CCW",
    "COPY",
    "CW",
    "DESTINATION_ATOP",
    "DESTINATION_IN",
    "DESTINATION_OUT",
    "DESTINATION_OVER",
    "DST_ALPHA",
    "DST_COLOR",
    "HOLE",
    "HSL",
    "HSLA",
    "LIGHTER",
    "LerpRGBA",
    "MITER",
    "NVGalign",
    "NVGblendFactor",
    "NVGcolor",
    "NVGcompositeOperation",
    "NVGcontext",
    "NVGlineCap",
    "NVGpaint",
    "NVGsolidity",
    "NVGwinding",
    "ONE",
    "ONE_MINUS_DST_ALPHA",
    "ONE_MINUS_DST_COLOR",
    "ONE_MINUS_SRC_ALPHA",
    "ONE_MINUS_SRC_COLOR",
    "RGB",
    "RGBA",
    "RGBAf",
    "RGBf",
    "ROUND",
    "SOLID",
    "SOURCE_IN",
    "SOURCE_OUT",
    "SOURCE_OVER",
    "SQUARE",
    "SRC_ALPHA",
    "SRC_ALPHA_SATURATE",
    "SRC_COLOR",
    "TransRGBA",
    "TransRGBAf",
    "XOR",
    "ZERO"
]


class NVGalign():
    """
    Members:

      ALIGN_LEFT

      ALIGN_CENTER

      ALIGN_RIGHT

      ALIGN_TOP

      ALIGN_MIDDLE

      ALIGN_BOTTOM

      ALIGN_BASELINE
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    ALIGN_BASELINE: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_BASELINE: 64>
    ALIGN_BOTTOM: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_BOTTOM: 32>
    ALIGN_CENTER: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_CENTER: 2>
    ALIGN_LEFT: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_LEFT: 1>
    ALIGN_MIDDLE: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_MIDDLE: 16>
    ALIGN_RIGHT: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_RIGHT: 4>
    ALIGN_TOP: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_TOP: 8>
    __members__: dict # value = {'ALIGN_LEFT': <NVGalign.ALIGN_LEFT: 1>, 'ALIGN_CENTER': <NVGalign.ALIGN_CENTER: 2>, 'ALIGN_RIGHT': <NVGalign.ALIGN_RIGHT: 4>, 'ALIGN_TOP': <NVGalign.ALIGN_TOP: 8>, 'ALIGN_MIDDLE': <NVGalign.ALIGN_MIDDLE: 16>, 'ALIGN_BOTTOM': <NVGalign.ALIGN_BOTTOM: 32>, 'ALIGN_BASELINE': <NVGalign.ALIGN_BASELINE: 64>}
    pass
class NVGblendFactor():
    """
    Members:

      ZERO

      ONE

      SRC_COLOR

      ONE_MINUS_SRC_COLOR

      DST_COLOR

      ONE_MINUS_DST_COLOR

      SRC_ALPHA

      ONE_MINUS_SRC_ALPHA

      DST_ALPHA

      ONE_MINUS_DST_ALPHA

      SRC_ALPHA_SATURATE
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    DST_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.DST_ALPHA: 256>
    DST_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.DST_COLOR: 16>
    ONE: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE: 2>
    ONE_MINUS_DST_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_DST_ALPHA: 512>
    ONE_MINUS_DST_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_DST_COLOR: 32>
    ONE_MINUS_SRC_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_SRC_ALPHA: 128>
    ONE_MINUS_SRC_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_SRC_COLOR: 8>
    SRC_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.SRC_ALPHA: 64>
    SRC_ALPHA_SATURATE: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.SRC_ALPHA_SATURATE: 1024>
    SRC_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.SRC_COLOR: 4>
    ZERO: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ZERO: 1>
    __members__: dict # value = {'ZERO': <NVGblendFactor.ZERO: 1>, 'ONE': <NVGblendFactor.ONE: 2>, 'SRC_COLOR': <NVGblendFactor.SRC_COLOR: 4>, 'ONE_MINUS_SRC_COLOR': <NVGblendFactor.ONE_MINUS_SRC_COLOR: 8>, 'DST_COLOR': <NVGblendFactor.DST_COLOR: 16>, 'ONE_MINUS_DST_COLOR': <NVGblendFactor.ONE_MINUS_DST_COLOR: 32>, 'SRC_ALPHA': <NVGblendFactor.SRC_ALPHA: 64>, 'ONE_MINUS_SRC_ALPHA': <NVGblendFactor.ONE_MINUS_SRC_ALPHA: 128>, 'DST_ALPHA': <NVGblendFactor.DST_ALPHA: 256>, 'ONE_MINUS_DST_ALPHA': <NVGblendFactor.ONE_MINUS_DST_ALPHA: 512>, 'SRC_ALPHA_SATURATE': <NVGblendFactor.SRC_ALPHA_SATURATE: 1024>}
    pass
class NVGcolor():
    def __init__(self, arg0: nanogui.Color) -> None: ...
    pass
class NVGcompositeOperation():
    """
    Members:

      SOURCE_OVER

      SOURCE_IN

      SOURCE_OUT

      ATOP

      DESTINATION_OVER

      DESTINATION_IN

      DESTINATION_OUT

      DESTINATION_ATOP

      LIGHTER

      COPY

      XOR
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    ATOP: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.ATOP: 3>
    COPY: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.COPY: 9>
    DESTINATION_ATOP: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_ATOP: 7>
    DESTINATION_IN: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_IN: 5>
    DESTINATION_OUT: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_OUT: 6>
    DESTINATION_OVER: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_OVER: 4>
    LIGHTER: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.LIGHTER: 8>
    SOURCE_IN: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.SOURCE_IN: 1>
    SOURCE_OUT: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.SOURCE_OUT: 2>
    SOURCE_OVER: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.SOURCE_OVER: 0>
    XOR: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.XOR: 10>
    __members__: dict # value = {'SOURCE_OVER': <NVGcompositeOperation.SOURCE_OVER: 0>, 'SOURCE_IN': <NVGcompositeOperation.SOURCE_IN: 1>, 'SOURCE_OUT': <NVGcompositeOperation.SOURCE_OUT: 2>, 'ATOP': <NVGcompositeOperation.ATOP: 3>, 'DESTINATION_OVER': <NVGcompositeOperation.DESTINATION_OVER: 4>, 'DESTINATION_IN': <NVGcompositeOperation.DESTINATION_IN: 5>, 'DESTINATION_OUT': <NVGcompositeOperation.DESTINATION_OUT: 6>, 'DESTINATION_ATOP': <NVGcompositeOperation.DESTINATION_ATOP: 7>, 'LIGHTER': <NVGcompositeOperation.LIGHTER: 8>, 'COPY': <NVGcompositeOperation.COPY: 9>, 'XOR': <NVGcompositeOperation.XOR: 10>}
    pass
class NVGcontext():
    def AddFallbackFont(self, baseFont: str, fallbackFont: str) -> int: ...
    def AddFallbackFontId(self, baseFont: int, fallbackFont: int) -> int: ...
    def Arc(self, cx: float, cy: float, r: float, a0: float, a1: float, dir: int) -> None: ...
    def ArcTo(self, x1: float, y1: float, x2: float, y2: float, radius: float) -> None: ...
    def BeginFrame(self, windowWidth: float, windowHeight: float, devicePixelRatio: float) -> None: ...
    def BeginPath(self) -> None: ...
    def BezierTo(self, c1x: float, c1y: float, c2x: float, c2y: float, x: float, y: float) -> None: ...
    def BoxGradient(self, x: float, y: float, w: float, h: float, r: float, f: float, icol: NVGcolor, ocol: NVGcolor) -> NVGpaint: ...
    def CancelFrame(self) -> None: ...
    def Circle(self, cx: float, cy: float, r: float) -> None: ...
    def ClosePath(self) -> None: ...
    def CreateFont(self, name: str, filename: str) -> int: ...
    def CreateImage(self, filename: str, imageFlags: int) -> int: ...
    def DeleteImage(self, image: int) -> None: ...
    def Ellipse(self, cx: float, cy: float, rx: float, ry: float) -> None: ...
    def EndFrame(self) -> None: ...
    def Fill(self) -> None: ...
    def FillColor(self, color: NVGcolor) -> None: ...
    def FillPaint(self, paint: NVGpaint) -> None: ...
    def FindFont(self, name: str) -> int: ...
    def FontBlur(self, blur: float) -> None: ...
    def FontFace(self, font: str) -> None: ...
    def FontFaceId(self, font: int) -> None: ...
    def FontSize(self, size: float) -> None: ...
    def GlobalAlpha(self, alpha: float) -> None: ...
    def GlobalCompositeBlendFunc(self, sfactor: int, dfactor: int) -> None: ...
    def GlobalCompositeBlendFuncSeparate(self, srcRGB: int, dstRGB: int, srcAlpha: int, dstAlpha: int) -> None: ...
    def GlobalCompositeOperation(self, factor: int) -> None: ...
    def ImagePattern(self, ox: float, oy: float, ex: float, ey: float, angle: float, image: int, alpha: float) -> NVGpaint: ...
    def IntersectScissor(self, x: float, y: float, w: float, h: float) -> None: ...
    def LineCap(self, cap: int) -> None: ...
    def LineJoin(self, join: int) -> None: ...
    def LineTo(self, x: float, y: float) -> None: ...
    def LinearGradient(self, sx: float, sy: float, ex: float, ey: float, icol: NVGcolor, ocol: NVGcolor) -> NVGpaint: ...
    def MiterLimit(self, limit: float) -> None: ...
    def MoveTo(self, x: float, y: float) -> None: ...
    def PathWinding(self, dir: int) -> None: ...
    def QuadTo(self, cx: float, cy: float, x: float, y: float) -> None: ...
    def RadialGradient(self, cx: float, cy: float, inr: float, outr: float, icol: NVGcolor, ocol: NVGcolor) -> NVGpaint: ...
    def Rect(self, x: float, y: float, w: float, h: float) -> None: ...
    def Reset(self) -> None: ...
    def ResetScissor(self) -> None: ...
    def ResetTransform(self) -> None: ...
    def Restore(self) -> None: ...
    def Rotate(self, angle: float) -> None: ...
    def RoundedRect(self, x: float, y: float, w: float, h: float, r: float) -> None: ...
    def RoundedRectVarying(self, x: float, y: float, w: float, h: float, radTopLeft: float, radTopRight: float, radBottomRight: float, radBottomLeft: float) -> None: ...
    def Save(self) -> None: ...
    def Scale(self, x: float, y: float) -> None: ...
    def Scissor(self, x: float, y: float, w: float, h: float) -> None: ...
    def SkewX(self, angle: float) -> None: ...
    def SkewY(self, angle: float) -> None: ...
    def Stroke(self) -> None: ...
    def StrokeColor(self, color: NVGcolor) -> None: ...
    def StrokePaint(self, paint: NVGpaint) -> None: ...
    def StrokeWidth(self, size: float) -> None: ...
    def Text(self, x: float, y: float, string: str) -> None: ...
    def TextAlign(self, align: int) -> None: ...
    def TextBounds(self, x: float, y: float, string: str) -> typing.Tuple[float, float, float, float]: ...
    def TextBox(self, x: float, y: float, breakRowWidth: float, string: str) -> None: ...
    def TextBoxBounds(self, x: float, y: float, breakRowWidth: float, string: str) -> typing.Tuple[float, float, float, float]: ...
    def TextLetterSpacing(self, spacing: float) -> None: ...
    def TextLineHeight(self, lineHeight: float) -> None: ...
    def Transform(self, a: float, b: float, c: float, d: float, e: float, f: float) -> None: ...
    def Translate(self, x: float, y: float) -> None: ...
    pass
class NVGlineCap():
    """
    Members:

      BUTT

      ROUND

      SQUARE

      BEVEL

      MITER
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    BEVEL: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.BEVEL: 3>
    BUTT: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.BUTT: 0>
    MITER: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.MITER: 4>
    ROUND: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.ROUND: 1>
    SQUARE: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.SQUARE: 2>
    __members__: dict # value = {'BUTT': <NVGlineCap.BUTT: 0>, 'ROUND': <NVGlineCap.ROUND: 1>, 'SQUARE': <NVGlineCap.SQUARE: 2>, 'BEVEL': <NVGlineCap.BEVEL: 3>, 'MITER': <NVGlineCap.MITER: 4>}
    pass
class NVGpaint():
    pass
class NVGsolidity():
    """
    Members:

      SOLID

      HOLE
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    HOLE: nanogui.nanovg.NVGsolidity # value = <NVGsolidity.HOLE: 2>
    SOLID: nanogui.nanovg.NVGsolidity # value = <NVGsolidity.SOLID: 1>
    __members__: dict # value = {'SOLID': <NVGsolidity.SOLID: 1>, 'HOLE': <NVGsolidity.HOLE: 2>}
    pass
class NVGwinding():
    """
    Members:

      CCW

      CW
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CCW: nanogui.nanovg.NVGwinding # value = <NVGwinding.CCW: 1>
    CW: nanogui.nanovg.NVGwinding # value = <NVGwinding.CW: 2>
    __members__: dict # value = {'CCW': <NVGwinding.CCW: 1>, 'CW': <NVGwinding.CW: 2>}
    pass
def HSL(arg0: float, arg1: float, arg2: float) -> NVGcolor:
    pass
def HSLA(arg0: float, arg1: float, arg2: float, arg3: int) -> NVGcolor:
    pass
def LerpRGBA(arg0: NVGcolor, arg1: NVGcolor, arg2: float) -> NVGcolor:
    pass
def RGB(arg0: int, arg1: int, arg2: int) -> NVGcolor:
    pass
def RGBA(arg0: int, arg1: int, arg2: int, arg3: int) -> NVGcolor:
    pass
def RGBAf(arg0: float, arg1: float, arg2: float, arg3: float) -> NVGcolor:
    pass
def RGBf(arg0: float, arg1: float, arg2: float) -> NVGcolor:
    pass
def TransRGBA(arg0: NVGcolor, arg1: int) -> NVGcolor:
    pass
def TransRGBAf(arg0: NVGcolor, arg1: float) -> NVGcolor:
    pass
ALIGN_BASELINE: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_BASELINE: 64>
ALIGN_BOTTOM: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_BOTTOM: 32>
ALIGN_CENTER: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_CENTER: 2>
ALIGN_LEFT: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_LEFT: 1>
ALIGN_MIDDLE: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_MIDDLE: 16>
ALIGN_RIGHT: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_RIGHT: 4>
ALIGN_TOP: nanogui.nanovg.NVGalign # value = <NVGalign.ALIGN_TOP: 8>
ATOP: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.ATOP: 3>
BEVEL: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.BEVEL: 3>
BUTT: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.BUTT: 0>
CCW: nanogui.nanovg.NVGwinding # value = <NVGwinding.CCW: 1>
COPY: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.COPY: 9>
CW: nanogui.nanovg.NVGwinding # value = <NVGwinding.CW: 2>
DESTINATION_ATOP: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_ATOP: 7>
DESTINATION_IN: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_IN: 5>
DESTINATION_OUT: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_OUT: 6>
DESTINATION_OVER: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.DESTINATION_OVER: 4>
DST_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.DST_ALPHA: 256>
DST_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.DST_COLOR: 16>
HOLE: nanogui.nanovg.NVGsolidity # value = <NVGsolidity.HOLE: 2>
LIGHTER: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.LIGHTER: 8>
MITER: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.MITER: 4>
ONE: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE: 2>
ONE_MINUS_DST_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_DST_ALPHA: 512>
ONE_MINUS_DST_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_DST_COLOR: 32>
ONE_MINUS_SRC_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_SRC_ALPHA: 128>
ONE_MINUS_SRC_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ONE_MINUS_SRC_COLOR: 8>
ROUND: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.ROUND: 1>
SOLID: nanogui.nanovg.NVGsolidity # value = <NVGsolidity.SOLID: 1>
SOURCE_IN: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.SOURCE_IN: 1>
SOURCE_OUT: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.SOURCE_OUT: 2>
SOURCE_OVER: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.SOURCE_OVER: 0>
SQUARE: nanogui.nanovg.NVGlineCap # value = <NVGlineCap.SQUARE: 2>
SRC_ALPHA: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.SRC_ALPHA: 64>
SRC_ALPHA_SATURATE: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.SRC_ALPHA_SATURATE: 1024>
SRC_COLOR: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.SRC_COLOR: 4>
XOR: nanogui.nanovg.NVGcompositeOperation # value = <NVGcompositeOperation.XOR: 10>
ZERO: nanogui.nanovg.NVGblendFactor # value = <NVGblendFactor.ZERO: 1>
