from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError, ValidationError, MissingError
from odoo.tools import config, human_size, ustr, html_escape
from odoo.tools.mimetypes import guess_mimetype

import logging

_logger = logging.getLogger(__name__)


class SchoolTeacherAssignment(models.Model):
    _name = 'school.assignment'
    _description = 'School Teacher Assignment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    school_id = fields.Many2one('school.structure', string='School', translate=True, required=True,
                                 track_visibility='onchange',ondelete="restrict")
    employee_id = fields.Many2one('hr.employee', string='Employee', translate=True, required=True,
                                track_visibility='onchange', ondelete="restrict")
    date_in_service = fields.Date(string='Date in Service', translate=True, required=True,
                                track_visibility='onchange')
    position = fields.Selection([
        ('employee', 'Employee'),
        ('teacher', 'Teacher'),
        ('principal', 'Principal'),
        ('mentor', 'Mentor'),
        ('assistant_director', 'Assistant Director'),
        ('administrative_employee', 'Administrative Employee'),
        ('secret_keeper', 'Secret Keeper')
    ], track_visibility='onchange', string="Position", store=True, required=True)