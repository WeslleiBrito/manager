from typing import TypedDict, NotRequired
from PySide6.QtCore import QDate

class TDateComponent(TypedDict):
    legend: str
    default_date: NotRequired[QDate]
    with_calendar: NotRequired[bool]
    display_format: NotRequired[str]
    min_date: NotRequired[QDate | None]
    max_date: NotRequired[QDate | None]