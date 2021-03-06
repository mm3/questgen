# coding: utf-8


class PROFESSION:
    NONE = 0
    BLACKSMITH = 1
    ROGUE = 2


class PLACE_TYPE:
    NONE = 0
    HOLY_CITY = 1


class OPTION_MARKERS:
    HONORABLE = 0
    DISHONORABLE = 1
    AGGRESSIVE = 2
    UNAGGRESSIVE = 3


OPTION_MARKERS_GROUPS = [set([OPTION_MARKERS.HONORABLE, OPTION_MARKERS.DISHONORABLE]),
                         set([OPTION_MARKERS.AGGRESSIVE, OPTION_MARKERS.UNAGGRESSIVE])]
