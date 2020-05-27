# Author: Julien Coux
# Copyright 2016 Camptocamp SA
# Copyright 2017 Akretion - Alexis de Lattre
# Copyright 2018 Eficent Business and IT Consuting Services, S.L.
# Copyright 2020 Therp B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class TrialBalanceReportWizard(models.TransientModel):

    _inherit = "trial.balance.report.wizard"
    _description = "Trial Balance Report Wizard"

    horizontal = fields.Boolean()

    @api.multi
    def button_export_html(self):
        res = super(TrialBalanceReportWizard, self).button_export_html()
        if self.horizontal:
            action = self.env.ref(
                'account_finiancial_report.action_report_trial_balance_hor')
            res.update(action.read()[0])
        return res

    @api.multi
    def _prepare_report_trial_balance(self):
        res = super(
            TrialBalanceReportWizard, self)._prepare_report_trial_balance()
        res['horizontal'] = self.horizontal
        return res
