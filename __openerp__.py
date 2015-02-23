{
    'name': "Product list search improvements",
    'version': '1.1',
    'depends': ['product', 'sale', 'product_brand'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Product Management',
    'description': """
    This module adds some searching facilities inside the product list.

It adds:
- the possibility to search on internal reference
- the possibility to search with a barcode reader using the EAN13 code
- the possibility to search on product brand (need to have the product_brand module installed)
    """,
    'data': ['product_view.xml',],
    'demo': [],
}
