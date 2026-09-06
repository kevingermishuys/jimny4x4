{
    'name': "Jimny 4x4 Rentals Theme",
    'summary': "Custom website building blocks for Jimny 4x4 Rentals",
    'description': """
Building blocks (snippets) that bring the approved Jimny 4x4 Rentals
website redesign into the Website Builder: hero, fleet showcase with
photo galleries, pricing ledger, add-ons, testimonials, route ideas,
events and contact/booking sections.

Drop these onto any page from the "Insert Blocks" panel and edit the
text, images and links in place with the standard website editor.

Purely additive: installing this only makes the new blocks available.
It does not change any existing page, color, font, or the login/
payment screens.
""",
    'version': '19.0.1.0.1',
    'category': 'Website',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippet_templates.xml',
        'views/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'jimny_snippets/static/src/scss/style.scss',
            'jimny_snippets/static/src/js/jimny_snippets.js',
        ],
    },
    'installable': True,
    'application': False,
}
