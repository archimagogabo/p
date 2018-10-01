
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class canvas_business(models.Model):
    _description = "canvas business"
    _name = 'canvas.business'

    name = fields.Char('Name', translate=True)
    texto = fields.Text('Text', translate=True,
                        default='''Business model canvas, translated as a business model canvas,
        is a strategic management template for the development of new models of
        business or document existing ones. It is a visual graphic with elements that
        describe the product or value proposal of the company, the infrastructure,
        Customers and finances. It helps companies to align their activities through
        the illustration of possible compensations. The business model of the canvas was
        initially proposed by Alexander Osterwalder1 on the basis of his work
        previous on the ontology of business models. Since the publication of
        the work of Osterwalder in 2008, new canvases have appeared for specific niches,
        like the Lean Canvas. The formal descriptions of the business become the blocks
        of construction for their activities. There are many different conceptualizations of
        deal; The work of Osterwalder and thesis (2010, 2004) propose a unique model of
        reference based on the similarities of a wide range of model conceptualizations
        of business. With your business model template design, a company can describe
        easily your business model.''')

    partners_clave = fields.Text('Partners Clave', translate=True,
                                 default='What can partners do better than you or at a lower cost and, therefore, enrich your business model?')
    actividades_clave = fields.Text('Key Activities', translate=True,
                                    default='What key activities do you have to develop in your business model in what way do you carry them out?')
    propuesta_de_valor = fields.Text('Value proposal', translate=True,
                                     default='What problems do we solve? What need do we satisfy? What are the benefits?')
    relacion_con_clientes = fields.Text('Relationship with Customers', translate=True,
                                        default='What kind of relationships do your clients expect you to establish and maintain with them?')
    segmentos_de_clientes = fields.Text('Customer Segments', translate=True,
                                        default='Who do we target? Which segments do we consider? Which ones are priorities?')
    recursos_claves = fields.Text('Key Resources', translate=True,
                                  default='What key resources does your business model require?')
    canales = fields.Text('Channels', translate=True,
                          default='Through which channels / media will you contact and assist your customers?')
    estructura_de_coste = fields.Text('Cost Structure', translate=True,
                                      default='What is the cost structure of your business model?')
    flujos_de_ingresos = fields.Text('Income flows', translate=True,
                                     default='What value are your customers willing to pay for your solution and what forms of payment? What margins do I get?')
