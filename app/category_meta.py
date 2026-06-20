"""Static fallback emoji maps for product groups and categories.

Used when a name is not yet present in the ``nav_groups`` /
``nav_categories`` DB tables.  Logic mirrors ``tech_bot/app/categories.py``
but is adapted for the technomarket_client_template data model (plain
string names stored in ``products.group_name`` / ``products.category``).
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Category fallback map  —  keyed by lowercase UA/RU name / alias
# ---------------------------------------------------------------------------

_CATEGORY_EMOJI: dict[str, str] = {
    # Boilers / water heaters
    "бойлери": "🔥",
    "бойлер": "🔥",
    "нагрівачі": "🔥",
    "нагрівач": "🔥",
    "бойлеры": "🔥",
    "нагреватели": "🔥",
    # Refrigerators
    "холодильники": "🧊",
    "холодильник": "🧊",
    "морозильники": "🧊",
    "морозильник": "🧊",
    # Washing machines
    "пральні машини": "🧺",
    "пральна машина": "🧺",
    "стиральные машины": "🧺",
    "стиральная машина": "🧺",
    # Air conditioners
    "кондиціонери": "❄️",
    "кондиціонер": "❄️",
    "кондиционеры": "❄️",
    "кондиционер": "❄️",
    # Heaters (convectors / fan-heaters, separate from boilers)
    "обігрівачі": "🔥",
    "обігрівач": "🔥",
    "обогреватели": "🔥",
    "обогреватель": "🔥",
    # Hoods / extraction fans
    "витяжки": "🏭",
    "витяжка": "🏭",
    "вытяжки": "🏭",
    "вытяжка": "🏭",
    # Gas stoves
    "газові плити": "🔥",
    "газова плита": "🔥",
    "газовые плиты": "🔥",
    "газовая плита": "🔥",
    "плити": "🔥",
    "плиты": "🔥",
    # Microwaves
    "мікрохвильовки": "📡",
    "мікрохвильовка": "📡",
    "микроволновки": "📡",
    "микроволновка": "📡",
    "свч": "📡",
    # Vacuum cleaners
    "пилососи": "🧹",
    "пилосос": "🧹",
    "пылесосы": "🧹",
    "пылесос": "🧹",
    # Coffee machines
    "кавомашини": "☕",
    "кавомашина": "☕",
    "кавоварки": "☕",
    "кавоварка": "☕",
    "кофемашины": "☕",
    "кофемашина": "☕",
    # Catch-all
    "інша техніка": "📦",
    "другая техника": "📦",
    "всі товари": "📦",
    "все товары": "📦",
    "інше": "📦",
    "другое": "📦",
}

# ---------------------------------------------------------------------------
# Group fallback map  —  top-level navigation groups
# ---------------------------------------------------------------------------

_GROUP_EMOJI: dict[str, str] = {
    "кліматична техніка": "❄️",
    "климатическая техника": "❄️",
    "водонагрівальна техніка": "🔥",
    "водонагревательная техника": "🔥",
    "пральна техніка": "🧺",
    "стиральная техника": "🧺",
    "кухонна техніка": "🍳",
    "кухонная техника": "🍳",
    "прибирання": "🧹",
    "уборка": "🧹",
    "холодильна техніка": "🧊",
    "холодильная техника": "🧊",
    "вентиляція": "🌬️",
    "вентиляция": "🌬️",
    "побутова техніка": "🏠",
    "бытовая техника": "🏠",
}


def category_emoji(name: str | None) -> str:
    """Return a fallback emoji for a *category* name.

    Looks up ``_CATEGORY_EMOJI`` by lowercase name.
    Returns ``"🏷️"`` for unknown names.
    """
    if not name:
        return "🏷️"
    return _CATEGORY_EMOJI.get(name.strip().lower(), "🏷️")


def group_emoji(name: str | None) -> str:
    """Return a fallback emoji for a *group* name.

    Checks ``_GROUP_EMOJI`` first, then falls through to ``_CATEGORY_EMOJI``
    (some groups share names with categories).  Returns ``"🏷️"`` if unknown.
    """
    if not name:
        return "🏷️"
    key = name.strip().lower()
    return _GROUP_EMOJI.get(key) or _CATEGORY_EMOJI.get(key, "🏷️")
