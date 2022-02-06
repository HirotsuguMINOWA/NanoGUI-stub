"""NanoGUI plugin"""
from __future__ import annotations

import capsule as capsule
import nanogui
from nanogui.nanovg import NVGcontext
import typing
import numpy
_Shape = typing.Tuple[int, ...]

__all__ = [
    "AdvancedGridLayout",
    "Alignment",
    "BoxLayout",
    "Button",
    "Canvas",
    "CheckBox",
    "Color",
    "ColorPicker",
    "ColorWheel",
    "ComboBox",
    "Cursor",
    "FloatBox",
    "FormHelper",
    "Graph",
    "GridLayout",
    "GroupLayout",
    "ImagePanel",
    "ImageView",
    "IntBox",
    "Label",
    "Layout",
    "MainloopHandle",
    "Matrix4f",
    "MessageDialog",
    "Object",
    "Orientation",
    "Popup",
    "PopupButton",
    "ProgressBar",
    "RenderPass",
    "Screen",
    "Shader",
    "Slider",
    "TabWidget",
    "TabWidgetBase",
    "TextArea",
    "TextBox",
    "Texture",
    "Theme",
    "ToolButton",
    "VScrollPanel",
    "Vector2f",
    "Vector2i",
    "Vector3f",
    "Widget",
    "Window",
    "active",
    "api",
    "async",
    "chdir_to_bundle_parent",
    "file_dialog",
    "get_cmake_dir",
    "glfw",
    "icons",
    "init",
    "leave",
    "load_image_directory",
    "mainloop",
    "nanogui_ext",
    "nanovg",
    "shutdown",
    "utf8"
]


class Layout():
    def perform_layout(self, arg0: NVGcontext, arg1: Widget) -> None: 
        """
        Performs applies all layout computations for the given widget.

        Parameter ``ctx``:
            The ``NanoVG`` context being used for drawing.

        Parameter ``widget``:
            The Widget whose child widgets will be positioned by the layout
            class..
        """
    def preferred_size(self, arg0: NVGcontext, arg1: Widget) -> Vector2i: 
        """
        Compute the preferred size for a given layout and widget

        Parameter ``ctx``:
            The ``NanoVG`` context being used for drawing.

        Parameter ``widget``:
            Widget, whose preferred size should be computed

        Returns:
            The preferred size, accounting for things such as spacing, padding
            for icons, etc.
        """
    pass
class Alignment():
    """
    The different kinds of alignments a layout can perform.

    Members:

      Minimum

      Middle

      Maximum

      Fill
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
    Fill: nanogui.Alignment # value = <Alignment.Fill: 3>
    Maximum: nanogui.Alignment # value = <Alignment.Maximum: 2>
    Middle: nanogui.Alignment # value = <Alignment.Middle: 1>
    Minimum: nanogui.Alignment # value = <Alignment.Minimum: 0>
    __members__: dict # value = {'Minimum': <Alignment.Minimum: 0>, 'Middle': <Alignment.Middle: 1>, 'Maximum': <Alignment.Maximum: 2>, 'Fill': <Alignment.Fill: 3>}
    pass
class BoxLayout(Layout):
    def __init__(self, orientation: Orientation, alignment: Alignment = Alignment.Middle, margin: int = 0, spacing: int = 0) -> None: 
        """
        Construct a box layout which packs widgets in the given
        ``Orientation``

        Parameter ``orientation``:
            The Orientation this BoxLayout expands along

        Parameter ``alignment``:
            Widget alignment perpendicular to the chosen orientation

        Parameter ``margin``:
            Margin around the layout container

        Parameter ``spacing``:
            Extra spacing placed between widgets
        """
    def alignment(self) -> Alignment: 
        """
        The Alignment of this BoxLayout.
        """
    def margin(self) -> int: 
        """
        The margin of this BoxLayout.
        """
    def orientation(self) -> Orientation: 
        """
        The Orientation this BoxLayout is using.
        """
    def set_alignment(self, arg0: Alignment) -> None: 
        """
        Sets the Alignment of this BoxLayout.
        """
    def set_margin(self, arg0: int) -> None: 
        """
        Sets the margin of this BoxLayout.
        """
    def set_orientation(self, arg0: Orientation) -> None: 
        """
        Sets the Orientation of this BoxLayout.
        """
    def set_spacing(self, arg0: int) -> None: 
        """
        Sets the spacing of this BoxLayout.
        """
    def spacing(self) -> int: 
        """
        The spacing this BoxLayout is using to pad in between widgets.
        """
    pass
class Object():
    pass
class Widget(Object):
    def __delitem__(self, arg0: int) -> None: 
        """
        Remove a child widget by index
        """
    def __getitem__(self, arg0: int) -> Widget: 
        """
        Retrieves the child at the specific position
        """
    def __init__(self, arg0: Widget) -> None: 
        """
        Construct a new widget with the given parent widget
        """
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: 
        """
        Return the number of child widgets
        """
    def absolute_position(self) -> Vector2i: 
        """
        Return the absolute position on screen
        """
    @typing.overload
    def add_child(self, arg0: Widget) -> None: 
        """
        Add a child widget to the current widget at the specified index.

        This function almost never needs to be called by hand, since the
        constructor of Widget automatically adds the current widget to its
        parent

        Convenience function which appends a widget at the end
        """
    @typing.overload
    def add_child(self, arg0: int, arg1: Widget) -> None: ...
    def child_count(self) -> int: 
        """
        Return the number of child widgets
        """
    def child_index(self, arg0: Widget) -> int: 
        """
        Returns the index of a specific child or -1 if not found
        """
    def children(self) -> typing.List[Widget]: 
        """
        Return the list of child widgets of the current widget
        """
    def contains(self, arg0: Vector2i) -> bool: 
        """
        Check if the widget contains a certain position
        """
    def cursor(self) -> Cursor: 
        """
        Return a pointer to the cursor of the widget
        """
    def draw(self, arg0: NVGcontext) -> None: 
        """
        Draw the widget (and all child widgets)
        """
    def enabled(self) -> bool: 
        """
        Return whether or not this widget is currently enabled
        """
    def find_widget(self, arg0: Vector2i) -> Widget: 
        """
        Determine the widget located at the given position value (recursive)
        """
    def fixed_height(self) -> int: ...
    def fixed_size(self) -> Vector2i: 
        """
        Return the fixed size (see set_fixed_size())
        """
    def fixed_width(self) -> int: ...
    def focus_event(self, focused: bool) -> bool: 
        """
        Handle a focus change event (default implementation: record the focus
        status, but do nothing)
        """
    def focused(self) -> bool: 
        """
        Return whether or not this widget is currently focused
        """
    def font_size(self) -> int: 
        """
        Return current font size. If not set the default of the current theme
        will be returned
        """
    def has_font_size(self) -> bool: 
        """
        Return whether the font size is explicitly specified for this widget
        """
    def height(self) -> int: 
        """
        Return the height of the widget
        """
    def keyboard_character_event(self, arg0: int) -> bool: 
        """
        Handle text input (UTF-32 format) (default implementation: do nothing)
        """
    def keyboard_event(self, key: int, scancode: int, action: int, modifiers: int) -> bool: 
        """
        Handle a keyboard event (default implementation: do nothing)
        """
    @staticmethod
    def layout(*args, **kwargs) -> typing.Any: 
        """
        Return the used Layout generator
        """
    def mouse_button_event(self, p: Vector2i, button: int, down: bool, modifiers: int) -> bool: 
        """
        Handle a mouse button event (default implementation: propagate to
        children)
        """
    def mouse_drag_event(self, p: Vector2i, rel: Vector2i, button: int, modifiers: int) -> bool: 
        """
        Handle a mouse drag event (default implementation: do nothing)
        """
    def mouse_enter_event(self, p: Vector2i, enter: bool) -> bool: 
        """
        Handle a mouse enter/leave event (default implementation: record this
        fact, but do nothing)
        """
    def mouse_motion_event(self, p: Vector2i, rel: Vector2i, button: int, modifiers: int) -> bool: 
        """
        Handle a mouse motion event (default implementation: propagate to
        children)
        """
    def parent(self) -> Widget: 
        """
        Return the parent widget
        """
    def perform_layout(self, arg0: NVGcontext) -> None: 
        """
        Invoke the associated layout generator to properly place child
        widgets, if any
        """
    def position(self) -> Vector2i: 
        """
        Return the position relative to the parent widget
        """
    def preferred_size(self, arg0: NVGcontext) -> Vector2i: 
        """
        Compute the preferred size of the widget
        """
    def remove_child(self, arg0: Widget) -> None: 
        """
        Remove a child widget by value
        """
    def remove_child_at(self, arg0: int) -> None: 
        """
        Remove a child widget by index
        """
    def request_focus(self) -> None: 
        """
        Request the focus to be moved to this widget
        """
    @staticmethod
    def screen(*args, **kwargs) -> typing.Any: 
        """
        Walk up the hierarchy and return the parent screen
        """
    def scroll_event(self, p: Vector2i, rel: Vector2f) -> bool: 
        """
        Handle a mouse scroll event (default implementation: propagate to
        children)
        """
    def set_cursor(self, arg0: Cursor) -> None: 
        """
        Set the cursor of the widget
        """
    def set_enabled(self, arg0: bool) -> None: 
        """
        Set whether or not this widget is currently enabled
        """
    def set_fixed_height(self, arg0: int) -> None: 
        """
        Set the fixed height (see set_fixed_size())
        """
    def set_fixed_size(self, arg0: Vector2i) -> None: 
        """
        Set the fixed size of this widget

        If nonzero, components of the fixed size attribute override any values
        computed by a layout generator associated with this widget. Note that
        just setting the fixed size alone is not enough to actually change its
        size; this is done with a call to set_size or a call to
        perform_layout() in the parent widget.
        """
    def set_fixed_width(self, arg0: int) -> None: 
        """
        Set the fixed width (see set_fixed_size())
        """
    def set_focused(self, arg0: bool) -> None: 
        """
        Set whether or not this widget is currently focused
        """
    def set_font_size(self, arg0: int) -> None: 
        """
        Set the font size of this widget
        """
    def set_height(self, arg0: int) -> None: 
        """
        Set the height of the widget
        """
    @staticmethod
    def set_layout(*args, **kwargs) -> typing.Any: 
        """
        Set the used Layout generator
        """
    def set_parent(self, arg0: Widget) -> None: 
        """
        Set the parent widget
        """
    def set_position(self, arg0: Vector2i) -> None: 
        """
        Set the position relative to the parent widget
        """
    def set_size(self, arg0: Vector2i) -> None: 
        """
        set the size of the widget
        """
    @staticmethod
    def set_theme(*args, **kwargs) -> typing.Any: 
        """
        Set the Theme used to draw this widget
        """
    def set_tooltip(self, arg0: str) -> None: ...
    def set_visible(self, arg0: bool) -> None: 
        """
        Set whether or not the widget is currently visible (assuming all
        parents are visible)
        """
    def set_width(self, arg0: int) -> None: 
        """
        Set the width of the widget
        """
    def size(self) -> Vector2i: 
        """
        Return the size of the widget
        """
    @staticmethod
    def theme(*args, **kwargs) -> typing.Any: 
        """
        Return the Theme used to draw this widget
        """
    def tooltip(self) -> str: ...
    def visible(self) -> bool: 
        """
        Return whether or not the widget is currently visible (assuming all
        parents are visible)
        """
    def visible_recursive(self) -> bool: 
        """
        Check if this widget is currently visible, taking parent widgets into
        account
        """
    def width(self) -> int: 
        """
        Return the width of the widget
        """
    @staticmethod
    def window(*args, **kwargs) -> typing.Any: 
        """
        Walk up the hierarchy and return the parent window
        """
    pass
class CheckBox(Widget, Object):
    """
    \class CheckBox checkbox.h nanogui/checkbox.h

    Two-state check box widget.

    Remark:
        This class overrides nanogui::Widget::mIconExtraScale to be
        ``1.2f``, which affects all subclasses of this Widget. Subclasses
        must explicitly set a different value if needed (e.g., in their
        constructor).
    """
    @typing.overload
    def __init__(self, parent: Widget, caption: str = 'Untitled') -> None: 
        """
        Adds a CheckBox to the specified ``parent``.

        Parameter ``parent``:
            The Widget to add this CheckBox to.

        Parameter ``caption``:
            The caption text of the CheckBox (default ``"Untitled"``).

        Parameter ``callback``:
            If provided, the callback to execute when the CheckBox is checked
            or unchecked. Default parameter function does nothing. See
            nanogui::CheckBox::mPushed for the difference between "pushed" and
            "checked".

        Adds a CheckBox to the specified ``parent``.

        Parameter ``parent``:
            The Widget to add this CheckBox to.

        Parameter ``caption``:
            The caption text of the CheckBox (default ``"Untitled"``).

        Parameter ``callback``:
            If provided, the callback to execute when the CheckBox is checked
            or unchecked. Default parameter function does nothing. See
            nanogui::CheckBox::mPushed for the difference between "pushed" and
            "checked".
        """
    @typing.overload
    def __init__(self, parent: Widget, caption: str, callback: typing.Callable[[bool], None]) -> None: ...
    def callback(self) -> typing.Callable[[bool], None]: 
        """
        Returns the current callback of this CheckBox.
        """
    def caption(self) -> str: 
        """
        The caption of this CheckBox.
        """
    def checked(self) -> bool: 
        """
        Whether or not this CheckBox is currently checked.
        """
    def pushed(self) -> bool: 
        """
        Whether or not this CheckBox is currently pushed. See
        nanogui::CheckBox::m_pushed.
        """
    def set_callback(self, arg0: typing.Callable[[bool], None]) -> None: 
        """
        Sets the callback to be executed when this CheckBox is checked /
        unchecked.
        """
    def set_caption(self, arg0: str) -> None: 
        """
        Sets the caption of this CheckBox.
        """
    def set_checked(self, arg0: bool) -> None: 
        """
        Sets whether or not this CheckBox is currently checked.
        """
    def set_pushed(self, arg0: bool) -> None: ...
    pass
class Color():
    """
    \class Color common.h nanogui/common.h

    Stores an RGBA floating point color value.

    This class simply wraps around an ``Vector4f``, providing some
    convenient methods and terminology for thinking of it as a color. The
    data operates in the same way as ``Vector4f``, and the following
    values are identical:

    \rst +---------+-------------+----------------+-------------+ |
    Channel | Array Index | Vector4f field | Color field |
    +=========+=============+================+=============+ | Red | ``0``
    | x() | r() | +---------+-------------+----------------+-------------+
    | Green | ``1`` | y() | g() |
    +---------+-------------+----------------+-------------+ | Blue |
    ``2`` | z() | b() |
    +---------+-------------+----------------+-------------+ | Alpha |
    ``3`` | w() | a() |
    +---------+-------------+----------------+-------------+ \endrst
    """
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None: 
        """
        Parameter ``color``:
            The three dimensional integer vector being copied, will be divided
            by ``255.0``.

        Parameter ``color``:
            The three dimensional float vector being copied.

        Parameter ``color``:
            The three dimensional integer vector being copied, will be divided
            by ``255.0``.

        Parameter ``color``:
            The three dimensional float vector being copied.
        """
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    def __repr__(self) -> str: ...
    def contrasting_color(self) -> Color: 
        """
        Computes the luminance as ``l = 0.299r + 0.587g + 0.144b + 0.0a``. If
        the luminance is less than 0.5, white is returned. If the luminance is
        greater than or equal to 0.5, black is returned. Both returns will
        have an alpha component of 1.0.
        """
    @property
    def b(self) -> float:
        """
        Return a reference to the blue channel

        :type: float
        """
    @b.setter
    def b(self, arg1: float) -> None:
        """
        Return a reference to the blue channel
        """
    @property
    def g(self) -> float:
        """
        Return a reference to the green channel

        :type: float
        """
    @g.setter
    def g(self, arg1: float) -> None:
        """
        Return a reference to the green channel
        """
    @property
    def r(self) -> float:
        """
        Return a reference to the red channel

        :type: float
        """
    @r.setter
    def r(self, arg1: float) -> None:
        """
        Return a reference to the red channel
        """
    @property
    def w(self) -> float:
        """
        Return a reference to the alpha channel.

        :type: float
        """
    @w.setter
    def w(self, arg1: float) -> None:
        """
        Return a reference to the alpha channel.
        """
    pass
class Button(Widget, Object):
    """
    \class Button button.h nanogui/button.h

    [Normal/Toggle/Radio/Popup] Button widget.
    """
    class Flags():
        """
        Flags to specify the button behavior (can be combined with binary OR)

        Members:

          NormalButton

          RadioButton

          ToggleButton

          PopupButton

          MenuButton
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
        MenuButton: nanogui.Button.Flags # value = <Flags.MenuButton: 16>
        NormalButton: nanogui.Button.Flags # value = <Flags.NormalButton: 1>
        PopupButton: nanogui.Button.Flags # value = <Flags.PopupButton: 8>
        RadioButton: nanogui.Button.Flags # value = <Flags.RadioButton: 2>
        ToggleButton: nanogui.Button.Flags # value = <Flags.ToggleButton: 4>
        __members__: dict # value = {'NormalButton': <Flags.NormalButton: 1>, 'RadioButton': <Flags.RadioButton: 2>, 'ToggleButton': <Flags.ToggleButton: 4>, 'PopupButton': <Flags.PopupButton: 8>, 'MenuButton': <Flags.MenuButton: 16>}
        pass
    class IconPosition():
        """
        The available icon positions.

        Members:

          Left

          LeftCentered

          RightCentered

          Right
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
        Left: nanogui.Button.IconPosition # value = <IconPosition.Left: 0>
        LeftCentered: nanogui.Button.IconPosition # value = <IconPosition.LeftCentered: 1>
        Right: nanogui.Button.IconPosition # value = <IconPosition.Right: 3>
        RightCentered: nanogui.Button.IconPosition # value = <IconPosition.RightCentered: 2>
        __members__: dict # value = {'Left': <IconPosition.Left: 0>, 'LeftCentered': <IconPosition.LeftCentered: 1>, 'RightCentered': <IconPosition.RightCentered: 2>, 'Right': <IconPosition.Right: 3>}
        pass
    def __init__(self, parent: Widget, caption: str = 'Untitled', icon: int = 0) -> None: 
        """
        Creates a button attached to the specified parent.

        Parameter ``parent``:
            The nanogui::Widget this Button will be attached to.

        Parameter ``caption``:
            The name of the button (default ``"Untitled"``).

        Parameter ``icon``:
            The icon to display with this Button. See nanogui::Button::mIcon.
        """
    def background_color(self) -> Color: 
        """
        Returns the background color of this Button.
        """
    def button_group(self) -> typing.List[Button]: 
        """
        Return the button group (for radio buttons)
        """
    def callback(self) -> typing.Callable[[], None]: 
        """
        Return the push callback (for any type of button)
        """
    def caption(self) -> str: 
        """
        Returns the caption of this Button.
        """
    def change_callback(self) -> typing.Callable[[bool], None]: 
        """
        Return the change callback (for toggle buttons)
        """
    def flags(self) -> int: 
        """
        The current flags of this Button (see nanogui::Button::Flags for
        options).
        """
    def icon(self) -> int: 
        """
        Returns the icon of this Button. See nanogui::Button::m_icon.
        """
    @staticmethod
    def icon_position(*args, **kwargs) -> typing.Any: 
        """
        The position of the icon for this Button.
        """
    def pushed(self) -> bool: 
        """
        Whether or not this Button is currently pushed.
        """
    def set_background_color(self, arg0: Color) -> None: 
        """
        Sets the background color of this Button.
        """
    def set_button_group(self, arg0: typing.List[Button]) -> None: 
        """
        Set the button group (for radio buttons)
        """
    def set_callback(self, arg0: typing.Callable[[], None]) -> None: 
        """
        Set the push callback (for any type of button).
        """
    def set_caption(self, arg0: str) -> None: 
        """
        Sets the caption of this Button.
        """
    def set_change_callback(self, arg0: typing.Callable[[bool], None]) -> None: 
        """
        Set the change callback (for toggle buttons).
        """
    def set_flags(self, arg0: int) -> None: 
        """
        Sets the flags of this Button (see nanogui::Button::Flags for
        options).
        """
    def set_icon(self, arg0: int) -> None: 
        """
        Sets the icon of this Button. See nanogui::Button::m_icon.
        """
    @staticmethod
    def set_icon_position(*args, **kwargs) -> typing.Any: 
        """
        Sets the position of the icon for this Button.
        """
    def set_pushed(self, arg0: bool) -> None: 
        """
        Sets whether or not this Button is currently pushed.
        """
    def set_text_color(self, arg0: Color) -> None: 
        """
        Sets the text color of the caption of this Button.
        """
    def text_color(self) -> Color: 
        """
        Returns the text color of the caption of this Button.
        """
    pass
class ColorWheel(Widget, Object):
    """
    \class ColorWheel colorwheel.h nanogui/colorwheel.h

    Fancy analog widget to select a color value. This widget was
    contributed by Dmitriy Morozov.
    """
    @typing.overload
    def __init__(self, parent: Widget) -> None: 
        """
        Adds a ColorWheel to the specified parent.

        Parameter ``parent``:
            The Widget to add this ColorWheel to.

        Parameter ``color``:
            The initial color of the ColorWheel (default: Red).
        """
    @typing.overload
    def __init__(self, parent: Widget, Color: Color) -> None: ...
    def callback(self) -> typing.Callable[[Color], None]: 
        """
        The callback to execute when a user changes the ColorWheel value.
        """
    def color(self) -> Color: 
        """
        The current Color this ColorWheel has selected.
        """
    def set_callback(self, arg0: typing.Callable[[Color], None]) -> None: 
        """
        Sets the callback to execute when a user changes the ColorWheel value.
        """
    def set_color(self, arg0: Color) -> None: 
        """
        Sets the current Color this ColorWheel has selected.
        """
    pass
class ComboBox(Widget, Object):
    """
    \class ComboBox combobox.h nanogui/combobox.h

    Simple combo box widget based on a popup button.
    """
    @typing.overload
    def __init__(self, parent: Widget) -> None: 
        """
        Create an empty combo box
        """
    @typing.overload
    def __init__(self, parent: Widget, items: typing.List[str]) -> None: ...
    @typing.overload
    def __init__(self, parent: Widget, items: typing.List[str], items_short: typing.List[str]) -> None: ...
    def callback(self) -> typing.Callable[[int], None]: 
        """
        The callback to execute for this ComboBox.
        """
    def items(self) -> typing.List[str]: 
        """
        The items associated with this ComboBox.
        """
    def items_short(self) -> typing.List[str]: 
        """
        The short descriptions associated with this ComboBox.
        """
    def selected_index(self) -> int: 
        """
        The current index this ComboBox has selected.
        """
    def set_callback(self, arg0: typing.Callable[[int], None]) -> None: 
        """
        Sets the callback to execute for this ComboBox.
        """
    @typing.overload
    def set_items(self, arg0: typing.List[str]) -> None: 
        """
        Sets the items for this ComboBox, providing both short and long
        descriptive lables for each item.
        """
    @typing.overload
    def set_items(self, arg0: typing.List[str], arg1: typing.List[str]) -> None: ...
    def set_selected_index(self, arg0: int) -> None: 
        """
        Sets the current index this ComboBox has selected.
        """
    pass
class Cursor():
    """
    Cursor shapes available to use in GLFW. Shape of actual cursor
    determined by Operating System.

    Members:

      Arrow

      IBeam

      Crosshair

      Hand

      HResize

      VResize
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
    Arrow: nanogui.Cursor # value = <Cursor.Arrow: 0>
    Crosshair: nanogui.Cursor # value = <Cursor.Crosshair: 2>
    HResize: nanogui.Cursor # value = <Cursor.HResize: 4>
    Hand: nanogui.Cursor # value = <Cursor.Hand: 3>
    IBeam: nanogui.Cursor # value = <Cursor.IBeam: 1>
    VResize: nanogui.Cursor # value = <Cursor.VResize: 5>
    __members__: dict # value = {'Arrow': <Cursor.Arrow: 0>, 'IBeam': <Cursor.IBeam: 1>, 'Crosshair': <Cursor.Crosshair: 2>, 'Hand': <Cursor.Hand: 3>, 'HResize': <Cursor.HResize: 4>, 'VResize': <Cursor.VResize: 5>}
    pass
class TextBox(Widget, Object):
    class Alignment():
        """
        How to align the text in the text box.

        Members:

          Left

          Center

          Right
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
        Center: nanogui.TextBox.Alignment # value = <Alignment.Center: 1>
        Left: nanogui.TextBox.Alignment # value = <Alignment.Left: 0>
        Right: nanogui.TextBox.Alignment # value = <Alignment.Right: 2>
        __members__: dict # value = {'Left': <Alignment.Left: 0>, 'Center': <Alignment.Center: 1>, 'Right': <Alignment.Right: 2>}
        pass
    def __init__(self, parent: Widget, value: str = 'Untitled') -> None: ...
    @staticmethod
    def alignment(*args, **kwargs) -> typing.Any: ...
    def callback(self) -> typing.Callable[[str], bool]: 
        """
        The callback to execute when the value of this TextBox has changed.
        """
    def default_value(self) -> str: ...
    def editable(self) -> bool: ...
    def format(self) -> str: 
        """
        Return the underlying regular expression specifying valid formats
        """
    def placeholder(self) -> str: 
        """
        Return the placeholder text to be displayed while the text box is
        empty.
        """
    @staticmethod
    def set_alignment(*args, **kwargs) -> typing.Any: ...
    def set_callback(self, arg0: typing.Callable[[str], bool]) -> None: 
        """
        Sets the callback to execute when the value of this TextBox has
        changed.
        """
    def set_default_value(self, arg0: str) -> None: ...
    def set_editable(self, arg0: bool) -> None: ...
    def set_format(self, arg0: str) -> None: 
        """
        Specify a regular expression specifying valid formats
        """
    def set_placeholder(self, arg0: str) -> None: 
        """
        Specify a placeholder text to be displayed while the text box is
        empty.
        """
    def set_spinnable(self, arg0: bool) -> None: ...
    def set_units(self, arg0: str) -> None: ...
    def set_units_image(self, arg0: int) -> None: ...
    def set_value(self, arg0: str) -> None: ...
    def spinnable(self) -> bool: ...
    def units(self) -> str: ...
    def units_image(self) -> int: ...
    def value(self) -> str: ...
    pass
class FormHelper():
    """
    \class FormHelper formhelper.h nanogui/formhelper.h

    Convenience class to create simple AntTweakBar-style layouts that
    expose variables of various types using NanoGUI widgets

    **Example**:

    \rst .. code-block:: cpp

    // [ ... initialize NanoGUI, construct screen ... ]

    FormHelper* h = new FormHelper(screen);

    // Add a new windows widget h->add_window(Vector2i(10,10),"Menu");

    // Start a new group h->add_group("Group 1");

    // Expose an integer variable by reference h->add_variable("integer
    variable", a_int);

    // Expose a float variable via setter/getter functions
    h->add_variable( [&](float value) { a_float = value; }, [&]() { return
    *a_float; }, "float variable");

    // add a new button h->add_button("Button", [&]() { std::cout <<
    "Button pressed" << std::endl; });

    \endrst
    """
    def __init__(self, arg0: Screen) -> None: 
        """
        Create a helper class to construct NanoGUI widgets on the given screen
        """
    def add_bool_variable(self, label: str, setter: typing.Callable[[bool], None], getter: typing.Callable[[], bool], editable: bool = True) -> CheckBox: ...
    def add_button(self, label: str, cb: typing.Callable[[], None]) -> Button: 
        """
        Add a new group that may contain several sub-widgets
        """
    @staticmethod
    def add_color_variable(*args, **kwargs) -> typing.Any: ...
    def add_double_variable(self, label: str, setter: typing.Callable[[float], None], getter: typing.Callable[[], float], editable: bool = True) -> FloatBox: ...
    def add_enum_variable(self, label: str, setter: typing.Callable[[int], None], getter: typing.Callable[[], int], editable: bool = True) -> ComboBox: ...
    def add_group(self, arg0: str) -> Label: 
        """
        Add a new group that may contain several sub-widgets
        """
    def add_int_variable(self, label: str, setter: typing.Callable[[int], None], getter: typing.Callable[[], int], editable: bool = True) -> IntBox: ...
    def add_string_variable(self, label: str, setter: typing.Callable[[str], None], getter: typing.Callable[[], str], editable: bool = True) -> TextBox: ...
    def add_widget(self, arg0: str, arg1: Widget) -> None: 
        """
        Add an arbitrary (optionally labeled) widget to the layout
        """
    def add_window(self, pos: Vector2i, title: str = 'Untitled') -> Window: 
        """
        Add a new top-level window
        """
    def fixed_size(self) -> Vector2i: 
        """
        The current fixed size being used for newly added widgets.
        """
    def group_font_name(self) -> str: 
        """
        The font name being used for group headers.
        """
    def group_font_size(self) -> int: 
        """
        The size of the font being used for group headers.
        """
    def label_font_name(self) -> str: 
        """
        The font name being used for labels.
        """
    def label_font_size(self) -> int: 
        """
        The size of the font being used for labels.
        """
    def refresh(self) -> None: 
        """
        Cause all widgets to re-synchronize with the underlying variable state
        """
    def set_fixed_size(self, arg0: Vector2i) -> None: 
        """
        Specify a fixed size for newly added widgets
        """
    def set_group_font_name(self, arg0: str) -> None: 
        """
        Sets the font name to be used for group headers.
        """
    def set_group_font_size(self, arg0: int) -> None: 
        """
        Sets the size of the font being used for group headers.
        """
    def set_label_font_name(self, arg0: str) -> None: 
        """
        Sets the font name being used for labels.
        """
    def set_label_font_size(self, arg0: int) -> None: 
        """
        Sets the size of the font being used for labels.
        """
    def set_widget_font_size(self, arg0: int) -> None: 
        """
        Sets the size of the font being used for non-group / non-label
        widgets.
        """
    def set_window(self, arg0: Window) -> None: 
        """
        Set the active Window instance.
        """
    def widget_font_size(self) -> int: 
        """
        The size of the font being used for non-group / non-label widgets.
        """
    def window(self) -> Window: 
        """
        Access the currently active Window instance
        """
    pass
class Graph(Widget, Object):
    """
    \class Graph graph.h nanogui/graph.h

    Simple graph widget for showing a function plot.
    """
    def __init__(self, parent: Widget, caption: str = 'Untitled') -> None: ...
    def background_color(self) -> Color: ...
    def caption(self) -> str: ...
    def fill_color(self) -> Color: ...
    def footer(self) -> str: ...
    def header(self) -> str: ...
    def set_background_color(self, arg0: Color) -> None: ...
    def set_caption(self, arg0: str) -> None: ...
    def set_fill_color(self, arg0: Color) -> None: ...
    def set_footer(self, arg0: str) -> None: ...
    def set_header(self, arg0: str) -> None: ...
    def set_stroke_color(self, arg0: Color) -> None: ...
    def set_text_color(self, arg0: Color) -> None: ...
    def set_values(self, arg0: typing.List[float]) -> None: ...
    def stroke_color(self) -> Color: ...
    def text_color(self) -> Color: ...
    def values(self) -> typing.List[float]: ...
    pass
class GridLayout(Layout):
    def __init__(self, orientation: Orientation = Orientation.Horizontal, resolution: int = 2, alignment: Alignment = Alignment.Middle, margin: int = 0, spacing: int = 0) -> None: 
        """
        Create a 2-column grid layout by default.

        Parameter ``orientation``:
            The fixed dimension of this GridLayout.

        Parameter ``resolution``:
            The number of rows or columns in the grid (depending on the
            Orientation).

        Parameter ``alignment``:
            How widgets should be aligned within each grid cell.

        Parameter ``margin``:
            The amount of spacing to add around the border of the grid.

        Parameter ``spacing``:
            The amount of spacing between widgets added to the grid.
        """
    def alignment(self, arg0: int, arg1: int) -> Alignment: 
        """
        The Alignment of the specified axis (row or column number, depending
        on the Orientation) at the specified index of that row or column.
        """
    def margin(self) -> int: 
        """
        The margin around this GridLayout.
        """
    def orientation(self) -> Orientation: 
        """
        The Orientation of this GridLayout.
        """
    def resolution(self) -> int: 
        """
        The number of rows or columns (depending on the Orientation) of this
        GridLayout.
        """
    @typing.overload
    def set_col_alignment(self, arg0: Alignment) -> None: 
        """
        Sets the Alignment of the columns.
        """
    @typing.overload
    def set_col_alignment(self, arg0: typing.List[Alignment]) -> None: ...
    def set_margin(self, arg0: int) -> None: 
        """
        Sets the margin of this GridLayout.
        """
    def set_orientation(self, arg0: Orientation) -> None: 
        """
        Sets the Orientation of this GridLayout.
        """
    def set_resolution(self, arg0: int) -> None: 
        """
        Sets the number of rows or columns (depending on the Orientation) of
        this GridLayout.
        """
    @typing.overload
    def set_row_alignment(self, arg0: Alignment) -> None: 
        """
        Sets the Alignment of the rows.
        """
    @typing.overload
    def set_row_alignment(self, arg0: typing.List[Alignment]) -> None: ...
    @typing.overload
    def set_spacing(self, arg0: int) -> None: 
        """
        Sets the spacing for a specific axis.

        Sets the spacing for all axes.
        """
    @typing.overload
    def set_spacing(self, arg0: int, arg1: int) -> None: ...
    def spacing(self, arg0: int) -> int: 
        """
        The spacing at the specified axis (row or column number, depending on
        the Orientation).
        """
    pass
class GroupLayout(Layout):
    def __init__(self, margin: int = 15, spacing: int = 6, group_spacing: int = 14, group_indent: int = 20) -> None: 
        """
        Creates a GroupLayout.

        Parameter ``margin``:
            The margin around the widgets added.

        Parameter ``spacing``:
            The spacing between widgets added.

        Parameter ``group_spacing``:
            The spacing between groups (groups are defined by each Label
            added).

        Parameter ``group_indent``:
            The amount to indent widgets in a group (underneath a Label).
        """
    def group_indent(self) -> int: 
        """
        The indent of widgets in a group (underneath a Label) of this
        GroupLayout.
        """
    def group_spacing(self) -> int: 
        """
        The spacing between groups of this GroupLayout.
        """
    def margin(self) -> int: 
        """
        The margin of this GroupLayout.
        """
    def set_group_indent(self, arg0: int) -> None: 
        """
        Sets the indent of widgets in a group (underneath a Label) of this
        GroupLayout.
        """
    def set_group_spacing(self, arg0: int) -> None: 
        """
        Sets the spacing between groups of this GroupLayout.
        """
    def set_margin(self, arg0: int) -> None: 
        """
        Sets the margin of this GroupLayout.
        """
    def set_spacing(self, arg0: int) -> None: 
        """
        Sets the spacing between widgets of this GroupLayout.
        """
    def spacing(self) -> int: 
        """
        The spacing between widgets of this GroupLayout.
        """
    pass
class ImagePanel(Widget, Object):
    def __init__(self, parent: Widget) -> None: ...
    def callback(self) -> typing.Callable[[int], None]: ...
    def images(self) -> typing.List[typing.Tuple[int, str]]: ...
    def set_callback(self, arg0: typing.Callable[[int], None]) -> None: ...
    def set_images(self, arg0: typing.List[typing.Tuple[int, str]]) -> None: ...
    pass
class Canvas(Widget, Object):
    """
    \class GLCanvas canvas.h nanogui/canvas.h

    Canvas widget for rendering OpenGL/GLES2/Metal content

    Canvas widget that can be used to display arbitrary OpenGL content.
    This is useful to display and manipulate 3D objects as part of an
    interactive application. The implementation uses scissoring to ensure
    that rendered objects don't spill into neighboring widgets.

    \rst **Usage** Override :func:`nanogui::GLCanvas::draw_contents` in
    subclasses to provide custom drawing code. See
    :ref:`nanogui_example_4`.

    \endrst
    """
    def __init__(self, parent: Widget, samples: int = 4, has_depth_buffer: bool = True, has_stencil_buffer: bool = False, clear: bool = True) -> None: 
        """
        Creates a new Canvas widget

        Parameter ``parent``:
            The parent widget

        Parameter ``samples``:
            The number of pixel samples (MSAA)

        Parameter ``has_depth_buffer``:
            Should the widget allocate a depth buffer for the underlying
            render pass?

        Parameter ``has_stencil_buffer``:
            Should the widget allocate a stencil buffer for the underlying
            render pass?

        Parameter ``clear``:
            Should the widget clear its color/depth/stencil buffer?
        """
    def background_color(self) -> Color: 
        """
        Return whether the widget border is drawn
        """
    def border_color(self) -> Color: 
        """
        Return whether the widget border is drawn
        """
    def draw_border(self) -> bool: 
        """
        Return whether the widget border will be drawn
        """
    def draw_contents(self) -> None: 
        """
        Draw the widget contents. Override this method.
        """
    @staticmethod
    def render_pass(*args, **kwargs) -> typing.Any: 
        """
        Return the render pass associated with the canvas object
        """
    def set_background_color(self, arg0: Color) -> None: 
        """
        Specify the widget background color
        """
    def set_border_color(self, arg0: Color) -> None: 
        """
        Specify the widget border color
        """
    def set_draw_border(self, arg0: bool) -> None: 
        """
        Specify whether to draw the widget border
        """
    pass
class IntBox(TextBox, Widget, Object):
    """
    \class IntBox textbox.h nanogui/textbox.h

    A specialization of TextBox for representing integral values.

    Template parameters should be integral types, e.g. ``int``, ``long``,
    ``uint32_t``, etc.
    """
    def __init__(self, parent: Widget, value: int = 0) -> None: ...
    def set_callback(self, arg0: typing.Callable[[int], None]) -> None: ...
    def set_max_value(self, arg0: int) -> None: ...
    @typing.overload
    def set_min_value(self, arg0: int) -> None: ...
    @typing.overload
    def set_min_value(self, arg0: int, arg1: int) -> None: ...
    def set_value(self, arg0: int) -> None: ...
    def set_value_increment(self, arg0: int) -> None: ...
    def value(self) -> int: ...
    pass
class Label(Widget, Object):
    def __init__(self, parent: Widget, caption: str, font: str = 'sans', font_size: int = -1) -> None: ...
    def caption(self) -> str: 
        """
        Get the label's text caption
        """
    def color(self) -> Color: 
        """
        Get the label color
        """
    def font(self) -> str: 
        """
        Get the currently active font
        """
    def set_caption(self, arg0: str) -> None: 
        """
        Set the label's text caption
        """
    def set_color(self, arg0: Color) -> None: 
        """
        Set the label color
        """
    def set_font(self, arg0: str) -> None: 
        """
        Set the currently active font (2 are available by default: 'sans' and
        'sans-bold')
        """
    pass
class AdvancedGridLayout(Layout):
    class Anchor():
        @typing.overload
        def __init__(self, x: int, y: int, horiz: Alignment = Alignment.Fill, vert: Alignment = Alignment.Fill) -> None: 
            """
            Create an Anchor at position ``(x, y)`` with specified Alignment.

            Create an Anchor at position ``(x, y)`` of size ``(w, h)`` with
            specified alignments.
            """
        @typing.overload
        def __init__(self, x: int, y: int, w: int, h: int, horiz: Alignment = Alignment.Fill, vert: Alignment = Alignment.Fill) -> None: ...
        pass
    def __init__(self, widths: typing.List[int], heights: typing.List[int]) -> None: 
        """
        Creates an AdvancedGridLayout with specified columns, rows, and
        margin.
        """
    @staticmethod
    def anchor(*args, **kwargs) -> typing.Any: 
        """
        Retrieve the anchor data structure for a given widget
        """
    def append_col(self, size: int, stretch: float = 0) -> None: 
        """
        Append a column of the given size (and stretch factor)
        """
    def append_row(self, size: int, stretch: float = 0) -> None: 
        """
        Append a row of the given size (and stretch factor)
        """
    def col_count(self) -> int: 
        """
        Return the number of cols
        """
    def margin(self) -> int: 
        """
        The margin of this AdvancedGridLayout.
        """
    def row_count(self) -> int: 
        """
        Return the number of rows
        """
    @staticmethod
    def set_anchor(*args, **kwargs) -> typing.Any: 
        """
        Specify the anchor data structure for a given widget
        """
    def set_col_stretch(self, arg0: int, arg1: float) -> None: 
        """
        Set the stretch factor of a given column
        """
    def set_margin(self, arg0: int) -> None: 
        """
        Sets the margin of this AdvancedGridLayout.
        """
    def set_row_stretch(self, arg0: int, arg1: float) -> None: 
        """
        Set the stretch factor of a given row
        """
    pass
class MainloopHandle():
    def join(self) -> None: ...
    pass
class Matrix4f():
    def __getitem__(self, index: typing.Tuple[int, int]) -> float: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: float) -> None: ...
    def __matmul__(self, arg0: Matrix4f) -> Matrix4f: ...
    def __repr__(self) -> str: ...
    def __setitem__(self, index: typing.Tuple[int, int], value: float) -> None: ...
    @staticmethod
    def look_at(origin: Vector3f, target: Vector3f, up: Vector3f) -> Matrix4f: ...
    @staticmethod
    def ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix4f: ...
    @staticmethod
    def perspective(fov: float, near: float, far: float, aspect: float = 1.0) -> Matrix4f: ...
    @staticmethod
    def rotate(axis: Vector3f, angle: float) -> Matrix4f: ...
    @staticmethod
    def scale(amount: Vector3f) -> Matrix4f: ...
    @staticmethod
    def translate(amount: Vector3f) -> Matrix4f: ...
    pass
class Window(Widget, Object):
    def __init__(self, parent: Widget, title: str = 'Untitled') -> None: ...
    def button_panel(self) -> Widget: 
        """
        Return the panel used to house window buttons
        """
    def center(self) -> None: 
        """
        Center the window in the current Screen
        """
    def dispose(self) -> None: 
        """
        Dispose the window
        """
    def modal(self) -> bool: 
        """
        Is this a model dialog?
        """
    def set_modal(self, arg0: bool) -> None: 
        """
        Set whether or not this is a modal dialog
        """
    def set_title(self, arg0: str) -> None: 
        """
        Set the window title
        """
    def title(self) -> str: 
        """
        Return the window title
        """
    pass
class PopupButton(Button, Widget, Object):
    def __init__(self, parent: Widget, caption: str = 'Untitled', button_icon: int = 0) -> None: ...
    def chevron_icon(self) -> int: ...
    def popup(self) -> Popup: ...
    def set_chevron_icon(self, arg0: int) -> None: ...
    def set_side(self, arg0: Popup.Side) -> None: ...
    def side(self) -> Popup.Side: ...
    pass
class Orientation():
    """
    The direction of data flow for a layout.

    Members:

      Horizontal

      Vertical
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
    Horizontal: nanogui.Orientation # value = <Orientation.Horizontal: 0>
    Vertical: nanogui.Orientation # value = <Orientation.Vertical: 1>
    __members__: dict # value = {'Horizontal': <Orientation.Horizontal: 0>, 'Vertical': <Orientation.Vertical: 1>}
    pass
class Popup(Window, Widget, Object):
    class Side():
        """
        Members:

          Left

          Right
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
        Left: nanogui.Popup.Side # value = <Side.Left: 0>
        Right: nanogui.Popup.Side # value = <Side.Right: 1>
        __members__: dict # value = {'Left': <Side.Left: 0>, 'Right': <Side.Right: 1>}
        pass
    def __init__(self, parent: Widget, parent_window: Window) -> None: 
        """
        Create a new popup parented to a screen (first argument) and a parent
        window (if applicable)
        """
    def anchor_offset(self) -> int: 
        """
        Return the anchor height; this determines the vertical shift relative
        to the anchor position
        """
    def anchor_pos(self) -> Vector2i: 
        """
        Set the anchor position in the parent window; the placement of the
        popup is relative to it
        """
    def anchor_size(self) -> int: 
        """
        Return the anchor width
        """
    def parent_window(self) -> Window: 
        """
        Return the parent window of the popup
        """
    def set_anchor_offset(self, arg0: int) -> None: 
        """
        Set the anchor height; this determines the vertical shift relative to
        the anchor position
        """
    def set_anchor_pos(self, arg0: Vector2i) -> None: 
        """
        Return the anchor position in the parent window; the placement of the
        popup is relative to it
        """
    def set_anchor_size(self, arg0: int) -> None: 
        """
        Set the anchor width
        """
    @staticmethod
    def set_side(*args, **kwargs) -> typing.Any: 
        """
        Set the side of the parent window at which popup will appear
        """
    @staticmethod
    def side(*args, **kwargs) -> typing.Any: 
        """
        Return the side of the parent window at which popup will appear
        """
    Left: nanogui.Popup.Side # value = <Side.Left: 0>
    Right: nanogui.Popup.Side # value = <Side.Right: 1>
    pass
class ColorPicker(PopupButton, Button, Widget, Object):
    """
    \class ColorPicker colorpicker.h nanogui/colorpicker.h

    Push button with a popup to tweak a color value.
    """
    @typing.overload
    def __init__(self, parent: Widget) -> None: 
        """
        Attaches a ColorPicker to the specified parent.

        Parameter ``parent``:
            The Widget to add this ColorPicker to.

        Parameter ``color``:
            The color initially selected by this ColorPicker (default: Red).
        """
    @typing.overload
    def __init__(self, parent: Widget, Color: Color) -> None: ...
    def callback(self) -> typing.Callable[[Color], None]: 
        """
        The callback executed when the ColorWheel changes.
        """
    def color(self) -> Color: 
        """
        Get the current color
        """
    def final_callback(self) -> typing.Callable[[Color], None]: 
        """
        The callback to execute when a new Color is selected on the ColorWheel
        **and** the user clicks the nanogui::ColorPicker::m_pick_button or
        nanogui::ColorPicker::m_reset_button.
        """
    def set_callback(self, arg0: typing.Callable[[Color], None]) -> None: 
        """
        Sets the callback is executed as the ColorWheel itself is changed. Set
        this callback if you need to receive updates for the ColorWheel
        changing before the user clicks nanogui::ColorPicker::mPickButton or
        nanogui::ColorPicker::mPickButton.
        """
    def set_color(self, arg0: Color) -> None: 
        """
        Set the current color
        """
    def set_final_callback(self, arg0: typing.Callable[[Color], None]) -> None: 
        """
        The callback to execute when a new Color is selected on the ColorWheel
        **and** the user clicks the nanogui::ColorPicker::m_pick_button or
        nanogui::ColorPicker::m_reset_button.
        """
    pass
class ProgressBar(Widget, Object):
    def __init__(self, parent: Widget) -> None: ...
    def set_value(self, arg0: float) -> None: ...
    def value(self) -> float: ...
    pass
class RenderPass(Object):
    class CullMode():
        """
        Culling mode

        Members:

          Disabled : 

          Front : 

          Back : 
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
        Back: nanogui.RenderPass.CullMode # value = <CullMode.Back: 2>
        Disabled: nanogui.RenderPass.CullMode # value = <CullMode.Disabled: 0>
        Front: nanogui.RenderPass.CullMode # value = <CullMode.Front: 1>
        __members__: dict # value = {'Disabled': <CullMode.Disabled: 0>, 'Front': <CullMode.Front: 1>, 'Back': <CullMode.Back: 2>}
        pass
    class DepthTest():
        """
        Depth test

        Members:

          Never : 

          Less : 

          Equal : 

          LessEqual : 

          Greater : 

          NotEqual : 

          GreaterEqual : 

          Always : 
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
        Always: nanogui.RenderPass.DepthTest # value = <DepthTest.Always: 7>
        Equal: nanogui.RenderPass.DepthTest # value = <DepthTest.Equal: 2>
        Greater: nanogui.RenderPass.DepthTest # value = <DepthTest.Greater: 4>
        GreaterEqual: nanogui.RenderPass.DepthTest # value = <DepthTest.GreaterEqual: 6>
        Less: nanogui.RenderPass.DepthTest # value = <DepthTest.Less: 1>
        LessEqual: nanogui.RenderPass.DepthTest # value = <DepthTest.LessEqual: 3>
        Never: nanogui.RenderPass.DepthTest # value = <DepthTest.Never: 0>
        NotEqual: nanogui.RenderPass.DepthTest # value = <DepthTest.NotEqual: 5>
        __members__: dict # value = {'Never': <DepthTest.Never: 0>, 'Less': <DepthTest.Less: 1>, 'Equal': <DepthTest.Equal: 2>, 'LessEqual': <DepthTest.LessEqual: 3>, 'Greater': <DepthTest.Greater: 4>, 'NotEqual': <DepthTest.NotEqual: 5>, 'GreaterEqual': <DepthTest.GreaterEqual: 6>, 'Always': <DepthTest.Always: 7>}
        pass
    def __enter__(self) -> None: ...
    # def __exit__(self, arg0: handle, arg1: handle, arg2: handle) -> None: ...
    def __init__(self, color_targets: typing.List[Object], depth_target: Object = None, stencil_target: Object = None, blit_target: Object = None, clear: bool = True) -> None: 
        """
        Create a new render pass for rendering to a specific set of targets

        Parameter ``color_targets``:
            One or more target objects to which color information will be
            rendered. Must either be a Screen or a Texture instance.

        Parameter ``depth_target``:
            Target object to which depth information will be rendered. Must
            either be ``NULL`` or a Texture instance.

        Parameter ``stencil_target``:
            Target object to which stencil information will be rendered. Must
            either be ``NULL`` or a Texture instance. Can be identical to
            'depth_target' in case the texture has the pixel format
            Texture::PixelFormat::DepthStencil.

        Parameter ``blit_target``:
            When rendering finishes, the render pass can (optionally) blit the
            framebuffer to another target (which can either be another
            RenderPass instance or a Screen instance). This is mainly useful
            for multisample antialiasing (MSAA) rendering where set of multi-
            sample framebuffers must be converted into ordinary framebuffers
            for display.

        Parameter ``clear``:
            Should enter() begin by clearing all buffers?
        """
    def begin(self) -> None: 
        """
        Begin the render pass

        The specified drawing state (e.g. depth tests, culling mode, blending
        mode) are automatically set up at this point. Later changes between
        begin() and end() are possible but cause additional OpenGL/GLES/Metal
        API calls.

        The Python bindings also include extra ``__enter__`` and ``__exit__``
        aliases so that the render pass can be activated via Pythons 'with'
        statement.
        """
    def blit_to(self, src_offset: Vector2i, src_size: Vector2i, dst: Object, dst_offset: Vector2i) -> None: 
        """
        Blit the framebuffer to another target (which can either be another
        RenderPass instance or a Screen instance).
        """
    def clear_color(self, arg0: int) -> Color: 
        """
        Return the clear color for a given color attachment
        """
    def clear_depth(self) -> float: 
        """
        Return the clear depth for the depth attachment
        """
    def clear_stencil(self) -> int: 
        """
        Return the clear stencil for the stencil attachment
        """
    def command_encoder(self) -> capsule: ...
    @staticmethod
    def cull_mode(*args, **kwargs) -> typing.Any: 
        """
        Return the culling mode associated with the render pass
        """
    @staticmethod
    def depth_test(*args, **kwargs) -> typing.Any: 
        """
        Return the depth test and depth write mask of this render pass
        """
    def end(self) -> None: 
        """
        Finish the render pass
        """
    def resize(self, arg0: Vector2i) -> None: 
        """
        Resize all texture targets attached to the render pass
        """
    def set_clear_color(self, arg0: int, arg1: Color) -> None: 
        """
        Set the clear color for a given color attachment
        """
    def set_clear_depth(self, arg0: float) -> None: 
        """
        Set the clear depth for the depth attachment
        """
    def set_clear_stencil(self, arg0: int) -> None: 
        """
        Set the clear stencil for the stencil attachment
        """
    @staticmethod
    def set_cull_mode(*args, **kwargs) -> typing.Any: 
        """
        Specify the culling mode associated with the render pass
        """
    @staticmethod
    def set_depth_test(*args, **kwargs) -> typing.Any: 
        """
        Specify the depth test and depth write mask of this render pass
        """
    def set_viewport(self, offset: Vector2i, size: Vector2i) -> None: 
        """
        Set the pixel offset and size of the viewport region
        """
    def viewport(self) -> typing.Tuple[Vector2i, Vector2i]: 
        """
        Return the pixel offset and size of the viewport region
        """
    pass
class Screen(Widget, Object):
    def __init__(self, size: Vector2i, caption: str = 'Unnamed', resizable: bool = True, fullscreen: bool = False, depth_buffer: bool = True, stencil_buffer: bool = True, float_buffer: bool = False, gl_major: int = 3, gl_minor: int = 2) -> None: 
        """
        Create a new Screen instance

        Parameter ``size``:
            Size in pixels at 96 dpi (on high-DPI screens, the actual
            resolution in terms of hardware pixels may be larger by an integer
            factor)

        Parameter ``caption``:
            Window title (in UTF-8 encoding)

        Parameter ``resizable``:
            If creating a window, should it be resizable?

        Parameter ``fullscreen``:
            Specifies whether to create a windowed or full-screen view

        Parameter ``stencil_buffer``:
            Should an 8-bit stencil buffer be allocated? NanoVG requires this
            to rasterize non-convex polygons. (NanoGUI does not render such
            polygons, but your application might.)

        Parameter ``float_buffer``:
            Should NanoGUI try to allocate a floating point framebuffer? This
            is useful for HDR and wide-gamut displays.

        Parameter ``gl_major``:
            The requested OpenGL Major version number. The default is 3, if
            changed the value must correspond to a forward compatible core
            profile (for portability reasons). For example, set this to 4 and
            gl_minor to 1 for a forward compatible core OpenGL 4.1 profile.
            Requesting an invalid profile will result in no context (and
            therefore no GUI) being created. This attribute is ignored when
            targeting OpenGL ES 2 or Metal.

        Parameter ``gl_minor``:
            The requested OpenGL Minor version number. The default is 2, if
            changed the value must correspond to a forward compatible core
            profile (for portability reasons). For example, set this to 1 and
            gl_major to 4 for a forward compatible core OpenGL 4.1 profile.
            Requesting an invalid profile will result in no context (and
            therefore no GUI) being created. This attribute is ignored when
            targeting OpenGL ES 2 or Metal.
        """
    def background(self) -> Color: 
        """
        Return the screen's background color
        """
    def caption(self) -> str: 
        """
        Get the window title bar caption
        """
    def clear(self) -> None: 
        """
        Clear the screen with the background color (glClearColor, glClear,
        etc.)

        You typically won't need to call this function yourself, as it is
        called by the default implementation of draw_contents() (which is
        called by draw_all())
        """
    @staticmethod
    def component_format(*args, **kwargs) -> typing.Any: 
        """
        Return the component format underlying the screen
        """
    @staticmethod
    def depth_stencil_texture(*args, **kwargs) -> typing.Any: ...
    def draw_all(self) -> None: 
        """
        Redraw the screen if the redraw flag is set

        This function does everything -- it calls draw_setup(),
        draw_contents() (which also clears the screen by default), draw(), and
        finally draw_teardown().

        See also:
            redraw
        """
    def draw_contents(self) -> None: 
        """
        Calls clear() and draws the window contents --- put your rendering
        code here.
        """
    def drop_event(self, arg0: typing.List[str]) -> bool: 
        """
        Handle a file drop event
        """
    def framebuffer_size(self) -> Vector2i: 
        """
        Return the framebuffer size (potentially larger than size() on high-
        DPI screens)
        """
    def glfw_window(self) -> GLFWwindow: 
        """
        Return a pointer to the underlying GLFW window data structure
        """
    def has_depth_buffer(self) -> bool: 
        """
        Does the framebuffer have a depth buffer
        """
    def has_float_buffer(self) -> bool: 
        """
        Does the framebuffer use a floating point representation
        """
    def has_stencil_buffer(self) -> bool: 
        """
        Does the framebuffer have a stencil buffer
        """
    def metal_layer(self) -> capsule: ...
    def metal_texture(self) -> capsule: ...
    def mouse_pos(self) -> Vector2i: 
        """
        Return the last observed mouse position value
        """
    def nvg_context(self) -> NVGcontext: 
        """
        Return a pointer to the underlying NanoVG draw context
        """
    def nvg_flush(self) -> None: 
        """
        Flush all queued up NanoVG rendering commands
        """
    def perform_layout(self) -> None: 
        """
        Compute the layout of all widgets
        """
    @staticmethod
    def pixel_format(*args, **kwargs) -> typing.Any: 
        """
        Return the pixel format underlying the screen
        """
    def pixel_ratio(self) -> float: 
        """
        Return the ratio between pixel and device coordinates (e.g. >= 2 on
        Mac Retina displays)
        """
    def redraw(self) -> None: 
        """
        Send an event that will cause the screen to be redrawn at the next
        event loop iteration
        """
    def resize_callback(self) -> typing.Callable[[Vector2i], None]: ...
    def resize_event(self, size: Vector2i) -> bool: 
        """
        Window resize event handler
        """
    def set_background(self, arg0: Color) -> None: 
        """
        Set the screen's background color
        """
    def set_caption(self, arg0: str) -> None: 
        """
        Set the window title bar caption
        """
    def set_resize_callback(self, arg0: typing.Callable[[Vector2i], None]) -> None: ...
    def set_size(self, arg0: Vector2i) -> None: 
        """
        Set window size
        """
    def set_visible(self, arg0: bool) -> None: 
        """
        Set the top-level window visibility (no effect on full-screen windows)
        """
    pass
class Shader(Object):
    class BlendMode():
        """
        Alpha blending mode

        Members:

          None : 

          AlphaBlend : 
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
        AlphaBlend: nanogui.Shader.BlendMode # value = <BlendMode.AlphaBlend: 1>
        # None: nanogui.Shader.BlendMode # value = <BlendMode.None: 0>
        __members__: dict # value = {'None': <BlendMode.None: 0>, 'AlphaBlend': <BlendMode.AlphaBlend: 1>}
        pass
    class PrimitiveType():
        """
        The type of geometry that should be rendered

        Members:

          Point : 

          Line : 

          LineStrip : 

          Triangle : 

          TriangleStrip : 
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
        Line: nanogui.Shader.PrimitiveType # value = <PrimitiveType.Line: 1>
        LineStrip: nanogui.Shader.PrimitiveType # value = <PrimitiveType.LineStrip: 2>
        Point: nanogui.Shader.PrimitiveType # value = <PrimitiveType.Point: 0>
        Triangle: nanogui.Shader.PrimitiveType # value = <PrimitiveType.Triangle: 3>
        TriangleStrip: nanogui.Shader.PrimitiveType # value = <PrimitiveType.TriangleStrip: 4>
        __members__: dict # value = {'Point': <PrimitiveType.Point: 0>, 'Line': <PrimitiveType.Line: 1>, 'LineStrip': <PrimitiveType.LineStrip: 2>, 'Triangle': <PrimitiveType.Triangle: 3>, 'TriangleStrip': <PrimitiveType.TriangleStrip: 4>}
        pass
    def __enter__(self) -> None: ...
    # def __exit__(self, arg0: handle, arg1: handle, arg2: handle) -> None: ...
    @staticmethod
    def __init__(*args, **kwargs) -> typing.Any: 
        """
        Initialize the shader using the specified source strings.

        Parameter ``render_pass``:
            RenderPass object encoding targets to which color, depth, and
            stencil information will be rendered.

        Parameter ``name``:
            A name identifying this shader

        Parameter ``vertex_shader``:
            The source of the vertex shader as a string.

        Parameter ``fragment_shader``:
            The source of the fragment shader as a string.
        """
    def begin(self) -> None: 
        """
        Begin drawing using this shader

        Note that any updates to 'uniform' and 'varying' shader parameters
        *must* occur prior to this method call.

        The Python bindings also include extra ``__enter__`` and ``__exit__``
        aliases so that the shader can be activated via Pythons 'with'
        statement.
        """
    def blend_mode(self) -> Shader.BlendMode: 
        """
        Return the blending mode of this shader
        """
    @staticmethod
    def draw_array(*args, **kwargs) -> typing.Any: 
        """
        Render geometry arrays, either directly or using an index array.

        Parameter ``primitive_type``:
            What type of geometry should be rendered?

        Parameter ``offset``:
            First index to render. Must be a multiple of 2 or 3 for lines and
            triangles, respectively (unless specified using strips).

        Parameter ``offset``:
            Number of indices to render. Must be a multiple of 2 or 3 for
            lines and triangles, respectively (unless specified using strips).

        Parameter ``indexed``:
            Render indexed geometry? In this case, an ``uint32_t`` valued
            buffer with name ``indices`` must have been uploaded using set().
        """
    def end(self) -> None: 
        """
        End drawing using this shader
        """
    def name(self) -> str: 
        """
        Return the name of this shader
        """
    def pipeline_state(self) -> capsule: ...
    def set_buffer(self, arg0: str, arg1: numpy.ndarray) -> None: 
        """
        Upload a buffer (e.g. vertex positions) that will be associated with a
        named shader parameter.

        Note that this function should be used both for 'varying' and
        'uniform' data---the implementation takes care of routing the data to
        the right endpoint. Matrices should be specified in column-major
        order.

        The buffer will be replaced if it is already present.
        """
    def set_texture(self, arg0: str, arg1: Texture) -> None: 
        """
        Associate a texture with a named shader parameter

        The association will be replaced if it is already present.
        """
    pass
class Slider(Widget, Object):
    def __init__(self, parent: Widget) -> None: ...
    def callback(self) -> typing.Callable[[float], None]: ...
    def final_callback(self) -> typing.Callable[[float], None]: ...
    def highlight_color(self) -> Color: ...
    def highlighted_range(self) -> typing.Tuple[float, float]: ...
    def range(self) -> typing.Tuple[float, float]: ...
    def set_callback(self, arg0: typing.Callable[[float], None]) -> None: ...
    def set_final_callback(self, arg0: typing.Callable[[float], None]) -> None: ...
    def set_highlight_color(self, arg0: Color) -> None: ...
    def set_highlighted_range(self, arg0: typing.Tuple[float, float]) -> None: ...
    def set_range(self, arg0: typing.Tuple[float, float]) -> None: ...
    def set_value(self, arg0: float) -> None: ...
    def value(self) -> float: ...
    pass
class TabWidgetBase(Widget, Object):
    def __init__(self, arg0: Widget) -> None: 
        """
        Construct a new tab widget
        """
    def append_tab(self, caption: str) -> int: 
        """
        Appends a new tab and returns its ID.
        """
    def background_color(self) -> Color: 
        """
        Return the widget's background color (a global property)
        """
    def callback(self) -> typing.Callable[[int], None]: 
        """
        Callback that is used to notify a listener about tab changes (will be
        called with the tab ID)
        """
    def close_callback(self) -> typing.Callable[[int], None]: 
        """
        Callback that is used to notify a listener about tab close events
        (will be called with the tab ID)
        """
    def insert_tab(self, index: int, caption: str) -> int: 
        """
        Inserts a new tab at the specified position and returns its ID.
        """
    def padding(self) -> int: 
        """
        Return the padding between the tab widget boundary and child widgets
        """
    def popup_callback(self) -> typing.Callable[[int, Screen], Popup]: 
        """
        Callback that is used to notify a listener about popup events (will be
        called with the tab ID)
        """
    def remove_tab(self, id: int) -> None: 
        """
        Removes a tab with the specified ID
        """
    def selected_id(self) -> int: 
        """
        Return the ID of the currently active tab
        """
    def selected_index(self) -> int: 
        """
        Return the index of the currently active tab
        """
    def set_background_color(self, arg0: Color) -> None: 
        """
        Set the widget's background color (a global property)
        """
    def set_callback(self, arg0: typing.Callable[[int], None]) -> None: 
        """
        Set a callback that is used to notify a listener about tab changes
        (will be called with the tab ID)
        """
    def set_close_callback(self, arg0: typing.Callable[[int], None]) -> None: 
        """
        Set a callback that is used to notify a listener about tab close
        events (will be called with the tab ID)
        """
    def set_padding(self, arg0: int) -> None: ...
    def set_popup_callback(self, arg0: typing.Callable[[int, Screen], Popup]) -> None: 
        """
        Set a callback that is used to notify a listener about popup events
        (will be called with the tab ID)
        """
    def set_selected_id(self, id: int) -> None: 
        """
        Set the ID of the currently active tab
        """
    def set_selected_index(self, id: int) -> None: 
        """
        Set the index of the currently active tab
        """
    def set_tab_caption(self, id: int, caption: str) -> None: 
        """
        Change the caption of the tab with the given ID
        """
    def set_tabs_closeable(self, arg0: bool) -> None: ...
    def set_tabs_draggable(self, arg0: bool) -> None: ...
    def tab_caption(self, id: int) -> str: 
        """
        Return the caption of the tab with the given ID
        """
    def tab_count(self) -> int: 
        """
        Return the total number of tabs
        """
    def tab_id(self, arg0: int) -> int: 
        """
        Return the ID of the tab at a given index
        """
    def tab_index(self, arg0: int) -> int: 
        """
        Return the index of the tab with a given ID (or throw an exception)
        """
    def tabs_closeable(self) -> bool: 
        """
        Return whether tabs provide a close button
        """
    def tabs_draggable(self) -> bool: 
        """
        Return whether tabs can be dragged to different positions
        """
    pass
class TabWidget(TabWidgetBase, Widget, Object):
    def __init__(self, arg0: Widget) -> None: 
        """
        Construct a new tab widget
        """
    def append_tab(self, caption: str, widget: Widget) -> int: 
        """
        Appends a new tab and returns its ID.
        """
    def insert_tab(self, index: int, caption: str, widget: Widget) -> int: 
        """
        Inserts a new tab at the specified position and returns its ID.
        """
    def remove_children(self) -> bool: 
        """
        Remove child widgets when the associated tab is closed/removed?
        """
    def set_remove_children(self, id: bool) -> None: 
        """
        Remove child widgets when the associated tab is closed/removed?
        """
    pass
class TextArea(Widget, Object):
    def __init__(self, arg0: Widget) -> None: ...
    def append(self, arg0: str) -> None: 
        """
        Append text at the end of the widget
        """
    def append_line(self, arg0: str) -> None: 
        """
        Append a line of text at the bottom
        """
    def background_color(self) -> Color: 
        """
        Return the widget's background color (a global property)
        """
    def clear(self) -> None: 
        """
        Clear all current contents
        """
    def font(self) -> str: 
        """
        Return the used font
        """
    def foreground_color(self) -> Color: 
        """
        Return the foreground color (applies to all subsequently added text)
        """
    def is_selectable(self) -> int: 
        """
        Return whether the text can be selected using the mouse
        """
    def padding(self) -> int: 
        """
        Return the amount of padding that is added around the text
        """
    def selection_color(self) -> Color: 
        """
        Return the widget's selection color (a global property)
        """
    def set_background_color(self, arg0: Color) -> None: 
        """
        Set the widget's background color (a global property)
        """
    def set_font(self, arg0: str) -> None: 
        """
        Set the used font
        """
    def set_foreground_color(self, arg0: Color) -> None: 
        """
        Set the foreground color (applies to all subsequently added text)
        """
    def set_padding(self, arg0: int) -> None: 
        """
        Set the amount of padding to add around the text
        """
    def set_selectable(self, arg0: int) -> None: 
        """
        Set whether the text can be selected using the mouse
        """
    def set_selection_color(self, arg0: Color) -> None: 
        """
        Set the widget's selection color (a global property)
        """
    pass
class FloatBox(TextBox, Widget, Object):
    """
    \class FloatBox textbox.h nanogui/textbox.h

    A specialization of TextBox representing floating point values.

    The emplate parametersshould a be floating point type, e.g. ``float``
    or ``double``.
    """
    def __init__(self, parent: Widget, value: float = 0.0) -> None: ...
    def set_callback(self, arg0: typing.Callable[[float], None]) -> None: ...
    def set_max_value(self, arg0: float) -> None: ...
    @typing.overload
    def set_min_value(self, arg0: float) -> None: ...
    @typing.overload
    def set_min_value(self, arg0: float, arg1: float) -> None: ...
    def set_value(self, arg0: float) -> None: ...
    def set_value_increment(self, arg0: float) -> None: ...
    def value(self) -> float: ...
    pass
class Texture(Object):
    class ComponentFormat():
        """
        Number format of pixel components

        Members:

          UInt8 : 

          Int8 : 

          UInt16 : 

          Int16 : 

          UInt32 : 

          Int32 : 

          Float16 : 

          Float32 : 
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
        Float16: nanogui.Texture.ComponentFormat # value = <ComponentFormat.Float16: 9>
        Float32: nanogui.Texture.ComponentFormat # value = <ComponentFormat.Float32: 10>
        Int16: nanogui.Texture.ComponentFormat # value = <ComponentFormat.Int16: 3>
        Int32: nanogui.Texture.ComponentFormat # value = <ComponentFormat.Int32: 5>
        Int8: nanogui.Texture.ComponentFormat # value = <ComponentFormat.Int8: 1>
        UInt16: nanogui.Texture.ComponentFormat # value = <ComponentFormat.UInt16: 4>
        UInt32: nanogui.Texture.ComponentFormat # value = <ComponentFormat.UInt32: 6>
        UInt8: nanogui.Texture.ComponentFormat # value = <ComponentFormat.UInt8: 2>
        __members__: dict # value = {'UInt8': <ComponentFormat.UInt8: 2>, 'Int8': <ComponentFormat.Int8: 1>, 'UInt16': <ComponentFormat.UInt16: 4>, 'Int16': <ComponentFormat.Int16: 3>, 'UInt32': <ComponentFormat.UInt32: 6>, 'Int32': <ComponentFormat.Int32: 5>, 'Float16': <ComponentFormat.Float16: 9>, 'Float32': <ComponentFormat.Float32: 10>}
        pass
    class InterpolationMode():
        """
        Texture interpolation mode

        Members:

          Nearest : Nearest neighbor interpolation

          Bilinear : Bilinear ineterpolation

          Trilinear : Trilinear interpolation (using MIP mapping)
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
        Bilinear: nanogui.Texture.InterpolationMode # value = <InterpolationMode.Bilinear: 1>
        Nearest: nanogui.Texture.InterpolationMode # value = <InterpolationMode.Nearest: 0>
        Trilinear: nanogui.Texture.InterpolationMode # value = <InterpolationMode.Trilinear: 2>
        __members__: dict # value = {'Nearest': <InterpolationMode.Nearest: 0>, 'Bilinear': <InterpolationMode.Bilinear: 1>, 'Trilinear': <InterpolationMode.Trilinear: 2>}
        pass
    class PixelFormat():
        """
        Overall format of the texture (e.g. luminance-only or RGBA)

        Members:

          R : Single-channel bitmap

          RA : Two-channel bitmap

          RGB : RGB bitmap

          RGBA : RGB bitmap + alpha channel

          BGR : BGR bitmap

          BGRA : BGR bitmap + alpha channel

          Depth : Depth map

          DepthStencil : Combined depth + stencil map
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
        BGR: nanogui.Texture.PixelFormat # value = <PixelFormat.BGR: 4>
        BGRA: nanogui.Texture.PixelFormat # value = <PixelFormat.BGRA: 5>
        Depth: nanogui.Texture.PixelFormat # value = <PixelFormat.Depth: 6>
        DepthStencil: nanogui.Texture.PixelFormat # value = <PixelFormat.DepthStencil: 7>
        R: nanogui.Texture.PixelFormat # value = <PixelFormat.R: 0>
        RA: nanogui.Texture.PixelFormat # value = <PixelFormat.RA: 1>
        RGB: nanogui.Texture.PixelFormat # value = <PixelFormat.RGB: 2>
        RGBA: nanogui.Texture.PixelFormat # value = <PixelFormat.RGBA: 3>
        __members__: dict # value = {'R': <PixelFormat.R: 0>, 'RA': <PixelFormat.RA: 1>, 'RGB': <PixelFormat.RGB: 2>, 'RGBA': <PixelFormat.RGBA: 3>, 'BGR': <PixelFormat.BGR: 4>, 'BGRA': <PixelFormat.BGRA: 5>, 'Depth': <PixelFormat.Depth: 6>, 'DepthStencil': <PixelFormat.DepthStencil: 7>}
        pass
    class TextureFlags():
        """
        How will the texture be used? (Must specify at least one)

        Members:

          ShaderRead : Texture to be read in shaders

          RenderTarget : Target framebuffer for rendering
        """
        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
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
        RenderTarget: nanogui.Texture.TextureFlags # value = <TextureFlags.RenderTarget: 2>
        ShaderRead: nanogui.Texture.TextureFlags # value = <TextureFlags.ShaderRead: 1>
        __members__: dict # value = {'ShaderRead': <TextureFlags.ShaderRead: 1>, 'RenderTarget': <TextureFlags.RenderTarget: 2>}
        pass
    class WrapMode():
        """
        How should out-of-bounds texture evaluations be handled?

        Members:

          ClampToEdge : Clamp evaluations to the edge of the texture

          Repeat : Repeat the texture

          MirrorRepeat : Repeat, but flip the texture after crossing the boundary
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
        ClampToEdge: nanogui.Texture.WrapMode # value = <WrapMode.ClampToEdge: 0>
        MirrorRepeat: nanogui.Texture.WrapMode # value = <WrapMode.MirrorRepeat: 2>
        Repeat: nanogui.Texture.WrapMode # value = <WrapMode.Repeat: 1>
        __members__: dict # value = {'ClampToEdge': <WrapMode.ClampToEdge: 0>, 'Repeat': <WrapMode.Repeat: 1>, 'MirrorRepeat': <WrapMode.MirrorRepeat: 2>}
        pass
    @typing.overload
    def __init__(self, filename: str, min_interpolation_mode: Texture.InterpolationMode = InterpolationMode.Bilinear, mag_interpolation_mode: Texture.InterpolationMode = InterpolationMode.Bilinear, wrap_mode: Texture.WrapMode = WrapMode.ClampToEdge) -> None: 
        """
        Allocate memory for a texture with the given configuration

        \note Certain combinations of pixel and component formats may not be
        natively supported by the hardware. In this case, init() chooses a
        similar supported configuration that can subsequently be queried using
        pixel_format() and component_format(). Some caution must be exercised
        in this case, since upload() will need to provide the data in a
        different storage format.

        Load an image from the given file using stb-image
        """
    @typing.overload
    def __init__(self, pixel_format: Texture.PixelFormat, component_format: Texture.ComponentFormat, size: Vector2i, min_interpolation_mode: Texture.InterpolationMode = InterpolationMode.Bilinear, mag_interpolation_mode: Texture.InterpolationMode = InterpolationMode.Bilinear, wrap_mode: Texture.WrapMode = WrapMode.ClampToEdge, samples: int = 1, flags: int = 1) -> None: ...
    def bytes_per_pixel(self) -> int: 
        """
        Return the number of bytes consumed per pixel of this texture
        """
    def channels(self) -> int: 
        """
        Return the number of channels of this texture
        """
    def component_format(self) -> Texture.ComponentFormat: 
        """
        Return the component format
        """
    def download(self) -> numpy.ndarray: 
        """
        Download packed pixel data from the GPU to the CPU
        """
    def flags(self) -> int: 
        """
        Return a combination of flags (from Texture::TextureFlags)
        """
    def mag_interpolation_mode(self) -> Texture.InterpolationMode: 
        """
        Return the interpolation mode for minimization
        """
    def min_interpolation_mode(self) -> Texture.InterpolationMode: 
        """
        Return the interpolation mode for minimization
        """
    def pixel_format(self) -> Texture.PixelFormat: 
        """
        Return the pixel format
        """
    def resize(self, arg0: Vector2i) -> None: 
        """
        Resize the texture (discards the current contents)
        """
    def sampler_state_handle(self) -> capsule: ...
    def samples(self) -> int: 
        """
        Return the number of samples (MSAA)
        """
    def size(self) -> Vector2i: 
        """
        Return the size of this texture
        """
    def texture_handle(self) -> capsule: ...
    def upload(self, arg0: numpy.ndarray) -> None: 
        """
        Upload packed pixel data from the CPU to the GPU
        """
    def wrap_mode(self) -> Texture.WrapMode: 
        """
        Return the wrap mode
        """
    pass
class Theme():
    def __init__(self, arg0: NVGcontext) -> None: ...
    @property
    def m_border_dark(self) -> Color:
        """
        The dark border color (default: intensity=``29``, alpha=``255``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_border_dark.setter
    def m_border_dark(self, arg0: Color) -> None:
        """
        The dark border color (default: intensity=``29``, alpha=``255``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_border_light(self) -> Color:
        """
        The light border color (default: intensity=``92``, alpha=``255``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_border_light.setter
    def m_border_light(self, arg0: Color) -> None:
        """
        The light border color (default: intensity=``92``, alpha=``255``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_border_medium(self) -> Color:
        """
        The medium border color (default: intensity=``35``, alpha=``255``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_border_medium.setter
    def m_border_medium(self, arg0: Color) -> None:
        """
        The medium border color (default: intensity=``35``, alpha=``255``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_button_corner_radius(self) -> int:
        """
        Rounding radius for Button (and derived types) widgets (default:
        ``2``).

        :type: int
        """
    @m_button_corner_radius.setter
    def m_button_corner_radius(self, arg0: int) -> None:
        """
        Rounding radius for Button (and derived types) widgets (default:
        ``2``).
        """
    @property
    def m_button_font_size(self) -> int:
        """
        The font size for buttons (default: ``20``).

        :type: int
        """
    @m_button_font_size.setter
    def m_button_font_size(self, arg0: int) -> None:
        """
        The font size for buttons (default: ``20``).
        """
    @property
    def m_button_gradient_bot_focused(self) -> Color:
        """
        The bottom gradient color for buttons in focus (default:
        intensity=``48``, alpha=``255``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_button_gradient_bot_focused.setter
    def m_button_gradient_bot_focused(self, arg0: Color) -> None:
        """
        The bottom gradient color for buttons in focus (default:
        intensity=``48``, alpha=``255``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_button_gradient_bot_pushed(self) -> Color:
        """
        The bottom gradient color for buttons currently pushed (default:
        intensity=``29``, alpha=``255``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_button_gradient_bot_pushed.setter
    def m_button_gradient_bot_pushed(self, arg0: Color) -> None:
        """
        The bottom gradient color for buttons currently pushed (default:
        intensity=``29``, alpha=``255``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_button_gradient_bot_unfocused(self) -> Color:
        """
        The bottom gradient color for buttons not in focus (default:
        intensity=``58``, alpha=``255``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_button_gradient_bot_unfocused.setter
    def m_button_gradient_bot_unfocused(self, arg0: Color) -> None:
        """
        The bottom gradient color for buttons not in focus (default:
        intensity=``58``, alpha=``255``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_button_gradient_top_focused(self) -> Color:
        """
        The top gradient color for buttons in focus (default:
        intensity=``64``, alpha=``255``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_button_gradient_top_focused.setter
    def m_button_gradient_top_focused(self, arg0: Color) -> None:
        """
        The top gradient color for buttons in focus (default:
        intensity=``64``, alpha=``255``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_button_gradient_top_pushed(self) -> Color:
        """
        The top gradient color for buttons currently pushed (default:
        intensity=``41``, alpha=``255``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_button_gradient_top_pushed.setter
    def m_button_gradient_top_pushed(self, arg0: Color) -> None:
        """
        The top gradient color for buttons currently pushed (default:
        intensity=``41``, alpha=``255``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_button_gradient_top_unfocused(self) -> Color:
        """
        The top gradient color for buttons not in focus (default:
        intensity=``74``, alpha=``255``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_button_gradient_top_unfocused.setter
    def m_button_gradient_top_unfocused(self, arg0: Color) -> None:
        """
        The top gradient color for buttons not in focus (default:
        intensity=``74``, alpha=``255``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_check_box_icon(self) -> int:
        """
        Icon to use for check box widgets (default: ``FA_CHECK``).

        :type: int
        """
    @m_check_box_icon.setter
    def m_check_box_icon(self, arg0: int) -> None:
        """
        Icon to use for check box widgets (default: ``FA_CHECK``).
        """
    @property
    def m_disabled_text_color(self) -> Color:
        """
        The disable dtext color (default: intensity=``255``, alpha=``80``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_disabled_text_color.setter
    def m_disabled_text_color(self, arg0: Color) -> None:
        """
        The disable dtext color (default: intensity=``255``, alpha=``80``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_drop_shadow(self) -> Color:
        """
        The color of the drop shadow drawn behind widgets (default:
        intensity=``0``, alpha=``128``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_drop_shadow.setter
    def m_drop_shadow(self, arg0: Color) -> None:
        """
        The color of the drop shadow drawn behind widgets (default:
        intensity=``0``, alpha=``128``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_font_icons(self) -> int:
        """
        The icon font face (default: ``"icons"`` from
        ``resources/entypo.ttf``).

        :type: int
        """
    @m_font_icons.setter
    def m_font_icons(self, arg0: int) -> None:
        """
        The icon font face (default: ``"icons"`` from
        ``resources/entypo.ttf``).
        """
    @property
    def m_font_mono_regular(self) -> int:
        """
        The monospace font face (default: ``"mono"`` from
        ``resources/inconsolata_regular.ttf``).

        :type: int
        """
    @m_font_mono_regular.setter
    def m_font_mono_regular(self, arg0: int) -> None:
        """
        The monospace font face (default: ``"mono"`` from
        ``resources/inconsolata_regular.ttf``).
        """
    @property
    def m_font_sans_bold(self) -> int:
        """
        The bold font face (default: ``"sans-bold"`` from
        ``resources/roboto_regular.ttf``).

        :type: int
        """
    @m_font_sans_bold.setter
    def m_font_sans_bold(self, arg0: int) -> None:
        """
        The bold font face (default: ``"sans-bold"`` from
        ``resources/roboto_regular.ttf``).
        """
    @property
    def m_font_sans_regular(self) -> int:
        """
        The standard font face (default: ``"sans"`` from
        ``resources/roboto_regular.ttf``).

        :type: int
        """
    @m_font_sans_regular.setter
    def m_font_sans_regular(self, arg0: int) -> None:
        """
        The standard font face (default: ``"sans"`` from
        ``resources/roboto_regular.ttf``).
        """
    @property
    def m_icon_color(self) -> Color:
        """
        The icon color (default: nanogui::Theme::m_text_color).

        :type: Color
        """
    @m_icon_color.setter
    def m_icon_color(self, arg0: Color) -> None:
        """
        The icon color (default: nanogui::Theme::m_text_color).
        """
    @property
    def m_icon_scale(self) -> float:
        """
        The amount of scaling that is applied to each icon to fit the size of
        NanoGUI widgets. The default value is ``0.77f``, setting to e.g.
        higher than ``1.0f`` is generally discouraged.

        :type: float
        """
    @m_icon_scale.setter
    def m_icon_scale(self, arg0: float) -> None:
        """
        The amount of scaling that is applied to each icon to fit the size of
        NanoGUI widgets. The default value is ``0.77f``, setting to e.g.
        higher than ``1.0f`` is generally discouraged.
        """
    @property
    def m_message_alt_button_icon(self) -> int:
        """
        Icon to use on message dialog alt button (default:
        ``FA_CIRCLE_WITH_CROSS``).

        :type: int
        """
    @m_message_alt_button_icon.setter
    def m_message_alt_button_icon(self, arg0: int) -> None:
        """
        Icon to use on message dialog alt button (default:
        ``FA_CIRCLE_WITH_CROSS``).
        """
    @property
    def m_message_information_icon(self) -> int:
        """
        Icon to use for informational message dialog widgets (default:
        ``FA_INFO_CIRCLE``).

        :type: int
        """
    @m_message_information_icon.setter
    def m_message_information_icon(self, arg0: int) -> None:
        """
        Icon to use for informational message dialog widgets (default:
        ``FA_INFO_CIRCLE``).
        """
    @property
    def m_message_primary_button_icon(self) -> int:
        """
        Icon to use on message_dialog primary button (default: ``FA_CHECK``).

        :type: int
        """
    @m_message_primary_button_icon.setter
    def m_message_primary_button_icon(self, arg0: int) -> None:
        """
        Icon to use on message_dialog primary button (default: ``FA_CHECK``).
        """
    @property
    def m_message_question_icon(self) -> int:
        """
        Icon to use for interrogative message dialog widgets (default:
        ``FA_QUESTION_CIRCLE``).

        :type: int
        """
    @m_message_question_icon.setter
    def m_message_question_icon(self, arg0: int) -> None:
        """
        Icon to use for interrogative message dialog widgets (default:
        ``FA_QUESTION_CIRCLE``).
        """
    @property
    def m_message_warning_icon(self) -> int:
        """
        Icon to use for warning message dialog widgets (default:
        ``FA_EXCLAMATION_TRINAGLE``).

        :type: int
        """
    @m_message_warning_icon.setter
    def m_message_warning_icon(self, arg0: int) -> None:
        """
        Icon to use for warning message dialog widgets (default:
        ``FA_EXCLAMATION_TRINAGLE``).
        """
    @property
    def m_popup_chevron_left_icon(self) -> int:
        """
        Icon to use for Popup_button widgets opening to the left (default:
        ``FA_CHEVRON_LEFT``).

        :type: int
        """
    @m_popup_chevron_left_icon.setter
    def m_popup_chevron_left_icon(self, arg0: int) -> None:
        """
        Icon to use for Popup_button widgets opening to the left (default:
        ``FA_CHEVRON_LEFT``).
        """
    @property
    def m_popup_chevron_right_icon(self) -> int:
        """
        Icon to use for Popup_button widgets opening to the right (default:
        ``FA_CHEVRON_RIGHT``).

        :type: int
        """
    @m_popup_chevron_right_icon.setter
    def m_popup_chevron_right_icon(self, arg0: int) -> None:
        """
        Icon to use for Popup_button widgets opening to the right (default:
        ``FA_CHEVRON_RIGHT``).
        """
    @property
    def m_standard_font_size(self) -> int:
        """
        The font size for all widgets other than buttons and textboxes
        (default: `` 16``).

        :type: int
        """
    @m_standard_font_size.setter
    def m_standard_font_size(self, arg0: int) -> None:
        """
        The font size for all widgets other than buttons and textboxes
        (default: `` 16``).
        """
    @property
    def m_tab_border_width(self) -> float:
        """
        The border width for Tab_header widgets (default: ``0.75f``).

        :type: float
        """
    @m_tab_border_width.setter
    def m_tab_border_width(self, arg0: float) -> None:
        """
        The border width for Tab_header widgets (default: ``0.75f``).
        """
    @property
    def m_tab_button_horizontal_padding(self) -> int:
        """
        The amount of horizontal padding for a Tab_header widget (default:
        ``10``).

        :type: int
        """
    @m_tab_button_horizontal_padding.setter
    def m_tab_button_horizontal_padding(self, arg0: int) -> None:
        """
        The amount of horizontal padding for a Tab_header widget (default:
        ``10``).
        """
    @property
    def m_tab_button_vertical_padding(self) -> int:
        """
        The amount of vertical padding for a Tab_header widget (default:
        ``2``).

        :type: int
        """
    @m_tab_button_vertical_padding.setter
    def m_tab_button_vertical_padding(self, arg0: int) -> None:
        """
        The amount of vertical padding for a Tab_header widget (default:
        ``2``).
        """
    @property
    def m_tab_control_width(self) -> int:
        """
        Used to help specify what lies "in bound" for a Tab_header widget
        (default: ``20``).

        :type: int
        """
    @m_tab_control_width.setter
    def m_tab_control_width(self, arg0: int) -> None:
        """
        Used to help specify what lies "in bound" for a Tab_header widget
        (default: ``20``).
        """
    @property
    def m_tab_inner_margin(self) -> int:
        """
        The inner margin on a Tab_header widget (default: ``5``).

        :type: int
        """
    @m_tab_inner_margin.setter
    def m_tab_inner_margin(self, arg0: int) -> None:
        """
        The inner margin on a Tab_header widget (default: ``5``).
        """
    @property
    def m_tab_max_button_width(self) -> int:
        """
        The maximum size for buttons on a Tab_header widget (default:
        ``160``).

        :type: int
        """
    @m_tab_max_button_width.setter
    def m_tab_max_button_width(self, arg0: int) -> None:
        """
        The maximum size for buttons on a Tab_header widget (default:
        ``160``).
        """
    @property
    def m_tab_min_button_width(self) -> int:
        """
        The minimum size for buttons on a Tab_header widget (default: ``20``).

        :type: int
        """
    @m_tab_min_button_width.setter
    def m_tab_min_button_width(self, arg0: int) -> None:
        """
        The minimum size for buttons on a Tab_header widget (default: ``20``).
        """
    @property
    def m_text_box_down_icon(self) -> int:
        """
        Icon to use when a text box has a down toggle (e.g. IntBox) (default:
        ``FA_CHEVRON_DOWN``).

        :type: int
        """
    @m_text_box_down_icon.setter
    def m_text_box_down_icon(self, arg0: int) -> None:
        """
        Icon to use when a text box has a down toggle (e.g. IntBox) (default:
        ``FA_CHEVRON_DOWN``).
        """
    @property
    def m_text_box_font_size(self) -> int:
        """
        The font size for text boxes (default: ``20``).

        :type: int
        """
    @m_text_box_font_size.setter
    def m_text_box_font_size(self, arg0: int) -> None:
        """
        The font size for text boxes (default: ``20``).
        """
    @property
    def m_text_box_up_icon(self) -> int:
        """
        Icon to use when a text box has an up toggle (e.g. IntBox) (default:
        ``FA_CHEVRON_UP``).

        :type: int
        """
    @m_text_box_up_icon.setter
    def m_text_box_up_icon(self, arg0: int) -> None:
        """
        Icon to use when a text box has an up toggle (e.g. IntBox) (default:
        ``FA_CHEVRON_UP``).
        """
    @property
    def m_text_color(self) -> Color:
        """
        The text color (default: intensity=``255``, alpha=``160``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_text_color.setter
    def m_text_color(self, arg0: Color) -> None:
        """
        The text color (default: intensity=``255``, alpha=``160``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_text_color_shadow(self) -> Color:
        """
        The text shadow color (default: intensity=``0``, alpha=``160``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_text_color_shadow.setter
    def m_text_color_shadow(self, arg0: Color) -> None:
        """
        The text shadow color (default: intensity=``0``, alpha=``160``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_transparent(self) -> Color:
        """
        The transparency color (default: intensity=``0``, alpha=``0``; see
        nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_transparent.setter
    def m_transparent(self, arg0: Color) -> None:
        """
        The transparency color (default: intensity=``0``, alpha=``0``; see
        nanogui::Color::Color(int,int)).
        """
    @property
    def m_window_corner_radius(self) -> int:
        """
        Rounding radius for Window widget corners (default: ``2``).

        :type: int
        """
    @m_window_corner_radius.setter
    def m_window_corner_radius(self, arg0: int) -> None:
        """
        Rounding radius for Window widget corners (default: ``2``).
        """
    @property
    def m_window_drop_shadow_size(self) -> int:
        """
        Size of drop shadow rendered behind the Window widgets (default:
        ``10``).

        :type: int
        """
    @m_window_drop_shadow_size.setter
    def m_window_drop_shadow_size(self, arg0: int) -> None:
        """
        Size of drop shadow rendered behind the Window widgets (default:
        ``10``).
        """
    @property
    def m_window_fill_focused(self) -> Color:
        """
        The fill color for a Window that is in focus (default:
        intensity=``45``, alpha=``230``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_window_fill_focused.setter
    def m_window_fill_focused(self, arg0: Color) -> None:
        """
        The fill color for a Window that is in focus (default:
        intensity=``45``, alpha=``230``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_window_fill_unfocused(self) -> Color:
        """
        The fill color for a Window that is not in focus (default:
        intensity=``43``, alpha=``230``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_window_fill_unfocused.setter
    def m_window_fill_unfocused(self, arg0: Color) -> None:
        """
        The fill color for a Window that is not in focus (default:
        intensity=``43``, alpha=``230``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_window_header_gradient_bot(self) -> Color:
        """
        The bottom gradient color for Window headings (default:
        nanogui::Theme::m_button_gradient_bot_unfocused).

        :type: Color
        """
    @m_window_header_gradient_bot.setter
    def m_window_header_gradient_bot(self, arg0: Color) -> None:
        """
        The bottom gradient color for Window headings (default:
        nanogui::Theme::m_button_gradient_bot_unfocused).
        """
    @property
    def m_window_header_gradient_top(self) -> Color:
        """
        The top gradient color for Window headings (default:
        nanogui::Theme::m_button_gradient_top_unfocused).

        :type: Color
        """
    @m_window_header_gradient_top.setter
    def m_window_header_gradient_top(self, arg0: Color) -> None:
        """
        The top gradient color for Window headings (default:
        nanogui::Theme::m_button_gradient_top_unfocused).
        """
    @property
    def m_window_header_height(self) -> int:
        """
        Default size of Window widget titles (default: ``30``).

        :type: int
        """
    @m_window_header_height.setter
    def m_window_header_height(self, arg0: int) -> None:
        """
        Default size of Window widget titles (default: ``30``).
        """
    @property
    def m_window_header_sep_bot(self) -> Color:
        """
        The Window header bottom separation color (default:
        nanogui::Theme::m_border_dark).

        :type: Color
        """
    @m_window_header_sep_bot.setter
    def m_window_header_sep_bot(self, arg0: Color) -> None:
        """
        The Window header bottom separation color (default:
        nanogui::Theme::m_border_dark).
        """
    @property
    def m_window_header_sep_top(self) -> Color:
        """
        The Window header top separation color (default:
        nanogui::Theme::m_border_light).

        :type: Color
        """
    @m_window_header_sep_top.setter
    def m_window_header_sep_top(self, arg0: Color) -> None:
        """
        The Window header top separation color (default:
        nanogui::Theme::m_border_light).
        """
    @property
    def m_window_popup(self) -> Color:
        """
        The popup window color (default: intensity=``50``, alpha=``255``; see
        nanogui::Color::Color(int,int))).

        :type: Color
        """
    @m_window_popup.setter
    def m_window_popup(self, arg0: Color) -> None:
        """
        The popup window color (default: intensity=``50``, alpha=``255``; see
        nanogui::Color::Color(int,int))).
        """
    @property
    def m_window_popup_transparent(self) -> Color:
        """
        The transparent popup window color (default: intensity=``50``,
        alpha=``0``; see nanogui::Color::Color(int,int))).

        :type: Color
        """
    @m_window_popup_transparent.setter
    def m_window_popup_transparent(self, arg0: Color) -> None:
        """
        The transparent popup window color (default: intensity=``50``,
        alpha=``0``; see nanogui::Color::Color(int,int))).
        """
    @property
    def m_window_title_focused(self) -> Color:
        """
        The title color for a Window that is in focus (default:
        intensity=``255``, alpha=``190``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_window_title_focused.setter
    def m_window_title_focused(self, arg0: Color) -> None:
        """
        The title color for a Window that is in focus (default:
        intensity=``255``, alpha=``190``; see nanogui::Color::Color(int,int)).
        """
    @property
    def m_window_title_unfocused(self) -> Color:
        """
        The title color for a Window that is not in focus (default:
        intensity=``220``, alpha=``160``; see nanogui::Color::Color(int,int)).

        :type: Color
        """
    @m_window_title_unfocused.setter
    def m_window_title_unfocused(self, arg0: Color) -> None:
        """
        The title color for a Window that is not in focus (default:
        intensity=``220``, alpha=``160``; see nanogui::Color::Color(int,int)).
        """
    pass
class ToolButton(Button, Widget, Object):
    def __init__(self, parent: Widget, icon: int, caption: str = '') -> None: ...
    pass
class VScrollPanel(Widget, Object):
    def __init__(self, parent: Widget) -> None: ...
    def scroll(self) -> float: 
        """
        Return the current scroll amount as a value between 0 and 1. 0 means
        scrolled to the top and 1 to the bottom.
        """
    def set_scroll(self, arg0: float) -> None: 
        """
        Set the scroll amount to a value between 0 and 1. 0 means scrolled to
        the top and 1 to the bottom.
        """
    pass
class Vector2f():
    def __add__(self, arg0: Vector2f) -> Vector2f: ...
    def __eq__(self, arg0: Vector2f) -> bool: ...
    def __getitem__(self, index: int) -> float: ...
    def __iadd__(self, arg0: Vector2f) -> Vector2f: ...
    def __imul__(self, arg0: Vector2f) -> Vector2f: ...
    @typing.overload
    def __init__(self, arg0: Vector2f) -> None: ...
    @typing.overload
    def __init__(self, arg0: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.List[float[2]]) -> None: ...
    def __isub__(self, arg0: Vector2f) -> Vector2f: ...
    def __itruediv__(self, arg0: Vector2f) -> Vector2f: ...
    def __mul__(self, arg0: Vector2f) -> Vector2f: ...
    def __ne__(self, arg0: Vector2f) -> bool: ...
    def __radd__(self, arg0: float) -> Vector2f: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, arg0: float) -> Vector2f: ...
    def __rsub__(self, arg0: float) -> Vector2f: ...
    def __rtruediv__(self, arg0: float) -> Vector2f: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __sub__(self, arg0: Vector2f) -> Vector2f: ...
    def __truediv__(self, arg0: Vector2f) -> Vector2f: ...
    @property
    def x(self) -> float:
        """
        :type: float
        """
    @x.setter
    def x(self, arg1: float) -> None:
        pass
    @property
    def y(self) -> float:
        """
        :type: float
        """
    @y.setter
    def y(self, arg1: float) -> None:
        pass
    __hash__ = None
    pass
class Vector2i():
    def __add__(self, arg0: Vector2i) -> Vector2i: ...
    def __eq__(self, arg0: Vector2i) -> bool: ...
    def __getitem__(self, index: int) -> int: ...
    def __iadd__(self, arg0: Vector2i) -> Vector2i: ...
    def __imul__(self, arg0: Vector2i) -> Vector2i: ...
    @typing.overload
    def __init__(self, arg0: Vector2i) -> None: ...
    @typing.overload
    def __init__(self, arg0: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.List[int[2]]) -> None: ...
    def __isub__(self, arg0: Vector2i) -> Vector2i: ...
    def __itruediv__(self, arg0: Vector2i) -> Vector2i: ...
    def __mul__(self, arg0: Vector2i) -> Vector2i: ...
    def __ne__(self, arg0: Vector2i) -> bool: ...
    def __radd__(self, arg0: int) -> Vector2i: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, arg0: int) -> Vector2i: ...
    def __rsub__(self, arg0: int) -> Vector2i: ...
    def __rtruediv__(self, arg0: int) -> Vector2i: ...
    def __setitem__(self, index: int, value: int) -> None: ...
    def __sub__(self, arg0: Vector2i) -> Vector2i: ...
    def __truediv__(self, arg0: Vector2i) -> Vector2i: ...
    @property
    def x(self) -> int:
        """
        :type: int
        """
    @x.setter
    def x(self, arg1: int) -> None:
        pass
    @property
    def y(self) -> int:
        """
        :type: int
        """
    @y.setter
    def y(self, arg1: int) -> None:
        pass
    __hash__ = None
    pass
class Vector3f():
    def __add__(self, arg0: Vector3f) -> Vector3f: ...
    def __eq__(self, arg0: Vector3f) -> bool: ...
    def __getitem__(self, index: int) -> float: ...
    def __iadd__(self, arg0: Vector3f) -> Vector3f: ...
    def __imul__(self, arg0: Vector3f) -> Vector3f: ...
    @typing.overload
    def __init__(self, arg0: Vector3f) -> None: ...
    @typing.overload
    def __init__(self, arg0: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.List[float[3]]) -> None: ...
    def __isub__(self, arg0: Vector3f) -> Vector3f: ...
    def __itruediv__(self, arg0: Vector3f) -> Vector3f: ...
    def __mul__(self, arg0: Vector3f) -> Vector3f: ...
    def __ne__(self, arg0: Vector3f) -> bool: ...
    def __radd__(self, arg0: float) -> Vector3f: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, arg0: float) -> Vector3f: ...
    def __rsub__(self, arg0: float) -> Vector3f: ...
    def __rtruediv__(self, arg0: float) -> Vector3f: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __sub__(self, arg0: Vector3f) -> Vector3f: ...
    def __truediv__(self, arg0: Vector3f) -> Vector3f: ...
    @property
    def x(self) -> float:
        """
        :type: float
        """
    @x.setter
    def x(self, arg1: float) -> None:
        pass
    @property
    def y(self) -> float:
        """
        :type: float
        """
    @y.setter
    def y(self, arg1: float) -> None:
        pass
    @property
    def z(self) -> float:
        """
        :type: float
        """
    @z.setter
    def z(self, arg1: float) -> None:
        pass
    __hash__ = None
    pass
class ImageView(Canvas, Widget, Object):
    def __init__(self, arg0: Widget) -> None: 
        """
        Initialize the widget
        """
    def center(self) -> None: 
        """
        Center the image on the screen
        """
    @staticmethod
    def image(*args, **kwargs) -> typing.Any: 
        """
        Return the currently active image
        """
    def offset(self) -> Vector2f: 
        """
        Return the pixel offset of the zoomed image rectangle
        """
    def pixel_to_pos(self, arg0: Vector2f) -> Vector2f: 
        """
        Convert a pixel position in the image to a position within the widget
        """
    def pos_to_pixel(self, arg0: Vector2f) -> Vector2f: 
        """
        Convert a position within the widget to a pixel position in the image
        """
    def reset(self) -> None: 
        """
        Center the image on the screen and set the scale to 1:1
        """
    def scale(self) -> float: 
        """
        Return the current magnification of the image
        """
    @staticmethod
    def set_image(*args, **kwargs) -> typing.Any: 
        """
        Set the currently active image
        """
    def set_offset(self, arg0: Vector2f) -> None: 
        """
        Set the pixel offset of the zoomed image rectangle
        """
    def set_pixel_callback(self, arg0: typing.Callable[[Vector2i], typing.List[str[4]]]) -> None: 
        """
        Set the callback that is used to acquire information about pixel
        components
        """
    def set_scale(self, arg0: float) -> None: 
        """
        Set the current magnification of the image
        """
    pass
class MessageDialog(Window, Widget, Object):
    class Type():
        """
        Classification of the type of message this MessageDialog represents.

        Members:

          Information

          Question

          Warning
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
        Information: nanogui.MessageDialog.Type # value = <Type.Information: 0>
        Question: nanogui.MessageDialog.Type # value = <Type.Question: 1>
        Warning: nanogui.MessageDialog.Type # value = <Type.Warning: 2>
        __members__: dict # value = {'Information': <Type.Information: 0>, 'Question': <Type.Question: 1>, 'Warning': <Type.Warning: 2>}
        pass
    @staticmethod
    def __init__(*args, **kwargs) -> typing.Any: ...
    def callback(self) -> typing.Callable[[int], None]: ...
    def message_label(self) -> Label: ...
    def set_callback(self, arg0: typing.Callable[[int], None]) -> None: ...
    pass
def active() -> bool:
    """
    Return whether or not a main loop is currently active
    """
def async(*args, **kwargs) -> typing.Any:
    """
    Enqueue a function to be executed executed before the application is
    redrawn the next time.

    NanoGUI is not thread-safe, and async() provides a mechanism for
    queuing up UI-related state changes from other threads.
    """
def chdir_to_bundle_parent() -> None:
    pass
@typing.overload
def file_dialog(arg0: typing.List[typing.Tuple[str, str]], arg1: bool) -> str:
    """
    Open a native file open/save dialog.

    Parameter ``filetypes``:
        Pairs of permissible formats with descriptions like ``("png",
        "Portable Network Graphics")``.

    Parameter ``save``:
        Set to ``True`` if you would like subsequent file dialogs to open
        at whatever folder they were in when they close this one.

    Open a native file open dialog, which allows multiple selection.

    Parameter ``filetypes``:
        Pairs of permissible formats with descriptions like ``("png",
        "Portable Network Graphics")``.

    Parameter ``save``:
        Set to ``True`` if you would like subsequent file dialogs to open
        at whatever folder they were in when they close this one.

    Parameter ``multiple``:
        Set to ``True`` if you would like to be able to select multiple
        files at once. May not be simultaneously true with \p save.
    """
@typing.overload
def file_dialog(arg0: typing.List[typing.Tuple[str, str]], arg1: bool, arg2: bool) -> typing.List[str]:
    pass
def init() -> None:
    """
    Static initialization; should be called once before invoking **any**
    NanoGUI functions **if** you are having NanoGUI manage OpenGL / GLFW.
    This method is effectively a wrapper call to ``glfwInit()``, so if you
    are managing OpenGL / GLFW on your own *do not call this method*.

    \rst Refer to :ref:`nanogui_example_3` for how you might go about
    managing OpenGL and GLFW on your own, while still using NanoGUI's
    classes. \endrst
    """
def leave() -> None:
    """
    Request the application main loop to terminate (e.g. if you detached
    mainloop).
    """
def load_image_directory(arg0: NVGcontext, arg1: str) -> typing.List[typing.Tuple[int, str]]:
    """
    Load a directory of PNG images and upload them to the GPU (suitable
    for use with ImagePanel)
    """
def mainloop(refresh: float = -1, detach: object = None) -> MainloopHandle:
    """
    Enter the application main loop

    Parameter ``refresh``:
        NanoGUI issues a redraw call whenever an keyboard/mouse/.. event
        is received. In the absence of any external events, it enforces a
        redraw once every ``refresh`` milliseconds. To disable the refresh
        timer, specify a negative value here.

    Parameter ``detach``:
        This parameter only exists in the Python bindings. When the active
        ``Screen`` instance is provided via the ``detach`` parameter, the
        ``mainloop()`` function becomes non-blocking and returns
        immediately (in this case, the main loop runs in parallel on a
        newly created thread). This feature is convenient for prototyping
        user interfaces on an interactive Python command prompt. When
        ``detach != None``, the function returns an opaque handle that
        will release any resources allocated by the created thread when
        the handle's ``join()`` method is invoked (or when it is garbage
        collected).

    Remark:
        Unfortunately, Mac OS X strictly requires all event processing to
        take place on the application's main thread, which is
        fundamentally incompatible with this type of approach. Thus,
        NanoGUI relies on a rather crazy workaround on Mac OS (kudos to
        Dmitriy Morozov): ``mainloop()`` launches a new thread as before
        but then uses libcoro to swap the thread execution environment
        (stack, registers, ..) with the main thread. This means that the
        main application thread is hijacked and processes events in the
        main loop to satisfy the requirements on Mac OS, while the thread
        that actually returns from this function is the newly created one
        (paradoxical, as that may seem). Deleting or ``join()``ing the
        returned handle causes application to wait for the termination of
        the main loop and then swap the two thread environments back into
        their initial configuration.
    """
def shutdown() -> None:
    """
    Static shutdown; should be called before the application terminates.
    """
def utf8(arg0: int) -> str:
    """
    Convert a single UTF32 character code to UTF8.

    \rst NanoGUI uses this to convert the icon character codes defined in
    :ref:`file_nanogui_entypo.h`. \endrst

    Parameter ``c``:
        The UTF32 character to be converted.
    """
api = 'metal'
