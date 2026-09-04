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

Also carries the brand (colors, fonts) onto pages this module doesn't
template directly, via a sitewide Bootstrap variable override, plus a
light branded pass on the login/signup screen and the payment-method
selection step.
""",
    'version': '19.0.1.0.0',
    'category': 'Website/Theme',
    'license': 'LGPL-3',
    'depends': ['website', 'web', 'payment'],
    'data': [
        'views/snippet_templates.xml',
        'views/snippets.xml',
        'views/auth_payment_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_custom/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'theme_custom/static/src/scss/style.scss',
            'theme_custom/static/src/scss/auth_payment.scss',
            'theme_custom/static/src/js/theme_custom.js',
        ],
    },
    'installable': True,
    'application': False,
}
