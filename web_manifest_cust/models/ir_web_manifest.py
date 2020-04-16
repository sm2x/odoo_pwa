from odoo import models, fields, api, _


class IrWebManifest(models.Model):
    _inherit = 'ir.web.manifest'

    start_url = fields.Char(default="/", required=True)
    display = fields.Char(default="standalone", required=True)
    # image_src = fields.Char(required=True)
    image_small = fields.Char(default="192x192", required=True)
    image_medium = fields.Char(default="512x512", required=True)
    image_type = fields.Char(default="image/png", required=True)

    @api.multi
    def get_manifest_data(self):
        res = super(IrWebManifest, self).get_manifest_data()
        res.update({
            'start_url': self.start_url,
            'display': self.display,
            'icons': [
                {
                    'src': '/web_manifest_cust/static/src/img/cat_small.png',
                    'sizes': self.image_small,
                    'type': self.image_type
                },
                {
                    'src': '/web_manifest_cust/static/src/img/cat_medium.png',
                    'sizes': self.image_medium,
                    'type': self.image_type
                }
            ]
        })
        return res
