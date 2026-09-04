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
""",
    'version': '19.0.1.0.0',
    'category': 'Website/Theme',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippet_templates.xml',
        'views/snippets.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_custom/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'theme_custom/static/src/scss/style.scss',
            'theme_custom/static/src/js/theme_custom.js',
        ],
    },
    'installable': True,
    'application': False,
}
