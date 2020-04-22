{
    'name': "Credit Control - Attach invoices report",

    'application': False,

    'author': "FIEF Management S.A.",
    'website': "https://www.fief.ch",

    'category': 'Uniforme',
    'version': '12.0.1.0.0',

    'depends': [
        'account_credit_control'
    ],

    'data': [
        'reports/report_credit_control_invoice.xml',
    ],
}
