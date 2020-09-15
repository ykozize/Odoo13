from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError, ValidationError, MissingError
from odoo.tools import config, human_size, ustr, html_escape
from odoo.tools.mimetypes import guess_mimetype

import logging

_logger = logging.getLogger(__name__)


class AdministrativeDirectorate(models.Model):
    _name = 'school.administrative_directorate'
    _description = 'School Administrative Directorate'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name', required=True, copy=False,
                       index=True, default=lambda self: _('New'),
                       translate=True, track_visibility='onchange')

