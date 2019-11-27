# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Create Invoice From Purchase Order Lines",
    "category": "Purchase",
    "summary": """""",
    "version": "12.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "depends": ["account", "purchase_view_adjust_oaw"],
    "description": """
Add a view for invoicable purchase order line to create invoice.
    """,
    "data": ["data/ir_actions.xml", "views/purchase_order_line_views.xml"],
}