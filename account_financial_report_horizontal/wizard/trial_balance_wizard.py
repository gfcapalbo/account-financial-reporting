# Author: Julien Coux
# Copyright 2016 Camptocamp SA
# Copyright 2017 Akretion - Alexis de Lattre
# Copyright 2018 Eficent Business and IT Consuting Services, S.L.
# Copyright 2020 Therp B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class TrialBalanceReportWizard(models.TransientModel):
    """Trial balance report wizard."""

    _inherit = "trial.balance.report.wizard"
    _description = "Trial Balance Report Wizard"

    horizontal = fields.Boolean()

    @api.multi
    def button_export_html(self):
        res = super(TrialBalanceReportWizard, self).button_export_html()
        if self.horizontal = True:
            res =
