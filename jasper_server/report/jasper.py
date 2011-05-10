# -*- coding: utf-8 -*-
##############################################################################
#
#    jasper_server module for OpenERP,
#    Copyright (C) 2009 SYLEAM Info Services (<http://www.syleam.fr/>)
#                  Christophe CHAUVET <christophe.chauvet@syleam.fr>
#
#    This file is a part of jasper_server
#
#    jasper_server is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jasper_server is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from report.interface import report_int
from report_soap import Report
import netsvc

logger = netsvc.Logger()


class report_jasper(report_int):
    """
    Extend report_int to use Jasper Server
    """
    def __init__(self, name):
        super(report_jasper, self).__init__(name)
        logger.notifyChannel('jasper_server', netsvc.LOG_DEBUG, 'Init report %s' % (self.name,))

    def create(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}

        logger.notifyChannel('jasper_server', netsvc.LOG_DEBUG, 'Call %s' % (self.name,))
        return Report(self.name, cr, uid, ids, data, context).execute()

report_jasper('report.print.jasper.server')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
