from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError, ValidationError, MissingError
from odoo.tools import config, human_size, ustr, html_escape
from odoo.tools.mimetypes import guess_mimetype

import logging

_logger = logging.getLogger(__name__)


class SchoolStructure(models.Model):
    _name = 'school.structure'
    _description = 'School Structure'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'),
                       translate=True, track_visibility='onchange')
    _sql_constraints = [('unique_school_name', 'UNIQUE(name)', 'name already found')]

    school_name = fields.Char(string='School Name', required=True, copy=False,translate=True, track_visibility='onchange')

    parent_id = fields.Many2one('school.structure', string='Parent', translate=True, track_visibility='onchange',
                                 ondelete="restrict")
    child_ids = fields.One2many('school.structure', 'parent_id', string='Structures', translate=True, track_visibility='onchange',
                                ondelete="restrict", readonly=True)
    company_id = fields.Many2one('res.company', string='Company', translate=True, required=True,
                                 track_visibility='onchange',
                                 default=lambda self: self.env.company.id, ondelete="restrict")
    administrative_directorate_id = fields.Many2one('school.administrative_directorate', string='Administrative Directorate',
                                                    translate=True, required=True,track_visibility='onchange',
                                                    ondelete="restrict")
    principal_id = fields.Many2one('hr.employee', string='Principal', translate=True, required=False,
                                  track_visibility='onchange', ondelete="restrict")
    assistant_director_id = fields.Many2one('hr.employee', string='Assistant Director', translate=True, required=False,
                                  track_visibility='onchange', ondelete="restrict")
    secret_keeper_id = fields.Many2one('hr.employee', string='Secret Keeper', translate=True, required=False,
                                  track_visibility='onchange', ondelete="restrict")

    school_street = fields.Char(string='Street', required=False, copy=False,translate=True, track_visibility='onchange')
    school_city = fields.Char(string='City', required=False, copy=False,translate=True, track_visibility='onchange')
    school_country_id = fields.Many2one('res.country', string='Country', translate=True, required=True,
                                       track_visibility='onchange')

    school_phone_number = fields.Char(string='Phone Number', required=True, copy=False,
                                        translate=True, track_visibility='onchange')
    school_license_number = fields.Char(string='License Number', required=False, copy=False,
                                        translate=True, track_visibility='onchange')
    school_email = fields.Char(string='Email', required=False, copy=True, track_visibility='onchange')
    school_website = fields.Char(string='Website', required=False, copy=True, track_visibility='onchange')
    assignment_ids = fields.One2many('school.assignment','school_id',translate=True,
                                     track_visibility='onchange')
    # physical_structure_ids
    # academic_year_ids
    # rule_ids

    @api.onchange('principal_id')
    def domain_principal(self):
        principals = []
        principals = self.env['school.assignment'].search([('position','=','principal'),('school_id','=',self.id)]).ids
        return {'domain': {'principal_id': [('id', 'in', principals)]}}

    @api.onchange('assistant_director_id')
    def domain_assistant_director(self):
        assistant_directors = []
        assistant_directors = self.env['school.assignment'].search(
            [('position', '=', 'assistant_director'), ('school_id', '=', self.id)]).ids
        return {'domain': {'assistant_director_id': [('id', 'in', assistant_directors)]}}

    @api.onchange('secret_keeper_id')
    def domain_secret_keeper(self):
        secret_keepers = []
        secret_keepers = self.env['school.assignment'].search(
            [('position', '=', 'secret_keeper'), ('school_id', '=', self.id)]).ids
        return {'domain': {'secret_keeper_id': [('id', 'in', secret_keepers)]}}
    
    
    def get_child_action(self):
        action = self.env.ref('school_management.ebt_school_structure_action').read()[0]
        action['domain'] = [('parent_id','=',self.id)]
        return action
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('school_structure_name_seq') or '/'
        return super(SchoolStructure, self).create(vals)
        
    
