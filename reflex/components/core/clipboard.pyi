"""Stub file for reflex/components/core/clipboard.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Optional, Sequence, overload

from reflex.components.base.fragment import Fragment
from reflex.event import EventType
from reflex.style import Style
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

class Clipboard(Fragment):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        targets: Sequence[str] | Var[Sequence[str]] | None = None,
        on_paste_event_actions: Var[dict[str, bool | int]]
        | dict[str, bool | int]
        | None = None,
        style: Style | None = None,
        key: Any | None = None,
        id: Any | None = None,
        class_name: Any | None = None,
        autofocus: bool | None = None,
        custom_attrs: dict[str, Var | Any] | None = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_paste: Optional[EventType[()] | EventType[list[tuple[str, str]]]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "Clipboard":
        """Create a Clipboard component.

        Args:
            *children: The children of the component.
            targets: The element ids to attach the event listener to. Defaults to all child components or the document.
            on_paste: Called when the user pastes data into the document. Data is a list of tuples of (mime_type, data). Binary types will be base64 encoded as a data uri.
            on_paste_event_actions: Save the original event actions for the on_paste event.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Clipboard Component.
        """
        ...

    def add_imports(self) -> dict[str, ImportVar]: ...
    def add_hooks(self) -> list[str | Var[str]]: ...

clipboard = Clipboard.create
