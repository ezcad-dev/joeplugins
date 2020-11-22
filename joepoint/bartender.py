# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from .dialog_geojson import Dialog as ImportGeojsonDialog
from .load_geojson import load_geojson


class Bartender:
    """Bartender handles orders from the menubar."""
    def __init__(self, treebase):
        self.treebase = treebase
        self.workerThreads = []

    def import_geojson(self):
        dialog = ImportGeojsonDialog(self.treebase)
        dialog.sig_start.connect(self.import_geojson_worker)
        dialog.show()

    def import_geojson_worker(self, fn, object_name):
        dob = load_geojson(fn, object_name)
        self.treebase.sigDataObjectLoaded.emit(dob)
