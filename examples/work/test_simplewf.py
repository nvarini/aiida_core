# -*- coding: utf-8 -*-

from aiida.backends.utils import load_dbenv, is_dbenv_loaded

__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__authors__ = "The AiiDA team."
__version__ = "0.7.1"

if not is_dbenv_loaded():
    load_dbenv()

from aiida.work.run import run, submit

from aiida.tutorial.simple_wf import SimpleWF
from aiida.orm.data.parameter import ParameterData


p = ParameterData(dict=dict(number=12))
p.store()
submit(SimpleWF, params=p)
