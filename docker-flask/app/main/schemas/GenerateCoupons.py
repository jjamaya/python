schema = {
    'type': 'object',
    'properties': {
        'id_client': {'type': 'number'},
        'name': {'type': 'string'},
        'surname': {'type': 'string'},
        'phone': {'type': 'string'},
        'email': {'type': 'string'}

    },
    'required': ['id_client', 'name', 'surname', 'phone','email']
}
