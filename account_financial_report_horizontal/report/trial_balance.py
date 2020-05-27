# © 2016 Julien Coux (Camptocamp)
# © 2018 Forest and Biomass Romania SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class TrialBalanceReportCompute(models.TransientModel):
    _inherit = 'report_trial_balance'

    horizontal = fields.Boolean()

    @api.multi
    def print_report(self, report_type):
        if report_type != 'xlsx' and self.horizontal:
            report_name = \
               'account_financial_report_horizontal.report_trial_balance_qweb'
            return self.env['ir.actions.report'].search(
                [('report_name', '=', report_name),
                 ('report_type', '=', report_type)],
                limit=1).report_action(self, config=False)
        return super(TrialBalanceReportCompute, self).print_report(report_type)

    def _get_html(self):
        if self.horizontal:
            result = {}
            rcontext = {}
            context = dict(self.env.context)
            report = self.browse(context.get('active_id'))
            if report:
                rcontext['o'] = report
                result['html'] = self.env.ref(
                    'account_financial_report_horizontal.report_trial_balance'
                ).render(rcontext)
                return result
        return super(TrialBalanceReportCompute, self)._get_html()
