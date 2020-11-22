# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import numpy as np
import geojson
from ezcad_plugins.gopoint.new.new import init_dob


def load_geojson(fn, object_name):
    with open(fn) as f:
        data = geojson.load(f)
    prop_names = ['X', 'Y', 'Z']
    vertexes = np.array(data["geometry"]["coordinates"])
    dob = init_dob(object_name, prop_names, vertexes)
    return dob


def main():
    dob = load_geojson('point.geojson', 'point')
    print(dob)


if __name__ == '__main__':
    main()
