# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.config.base import _
from ezcad.widgets.mode_switch import PluginMenuBar
from ezcad.utils.qthelpers import create_action, add_actions
from joepoint.bartender import Bartender


class PointMenuBar(PluginMenuBar):
    NAME = "JoePoint Menubar"

    def __init__(self):
        super().__init__()
        self.treebase = None
        self.bartender = None
        self.gate_menu = self.addMenu(_("Gate"))

    def setup(self):
        # call bartender after set treebase
        self.bartender = Bartender(self.treebase)
        self.make_actions()
        self.gate_menu_actions = [self.act_import_geojson]
        add_actions(self.gate_menu, self.gate_menu_actions)

    def make_actions(self):
        self.act_import_geojson = create_action(self,
            _('Import GeoJSON file'),
            triggered=self.bartender.import_geojson)
