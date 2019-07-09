# list of all Reference classes
ReferenceClasses = ['Resource', 'Insight', 'Tool', 'Message']

# list of all Reference sub-classes
ReferenceSubclasses = {
    'Resource': [
        'File',
        'State',
        'Dashboard',
        'App',
        'Notebook',
        'Protocol'
    ],
    'Insight': [
        'Report',
        'Memo',
        'Star'
    ],
    'Tool': ['Tool'],
    'Message': ['Message']
}

# list of all available Relationship types
RelationshipTypes = [
    'WASASSOCIATEDWITH',
    'WASGENERATEDBY',
    'USED',
    'WASATTRIBUTEDTO'
]

NodeRelationships = {
    ('Activity', 'Reference'): 'USED',
    ('Activity', 'Agent'): 'WASASSOCIATEDWITH',
    ('Reference', 'Activity'): 'WASGENERATEDBY',
    ('Reference', 'Agent'): 'WASATTRIBUTEDTO'
}

# list of all Activities Names
ActivityClasses = [
    'Tool session',
    'Mention',
    'Report generation',
    'Memoization',
    'Starred'
]

ActivityRoles = {
    'Tool session': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'was_input', 'num': (1, 4)},
                'Tool': {'role': 'was_executed', 'num': (1, 1)}
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'analyst', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'State': {'role': 'was_created', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'analyst', 'num': (1, 1)},
                'State': {'role': 'was_created', 'num': (1, 1)}
            }
        }
    },
    'Mention': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'was_mentioned', 'num': (0, 1)},
                'Dashboard': {'role': 'was_mentioned', 'num': (0, 1)},
                'App': {'role': 'was_mentioned', 'num': (0, 1)},
                'Notebook': {'role': 'was_mentioned', 'num': (0, 1)},
                'Protocol': {'role': 'was_mentioned', 'num': (0, 1)},
                'State': {'role': 'was_mentioned', 'num': (0, 1)},
                'Report': {'role': 'was_mentioned', 'num': (0, 1)},
                'Memo': {'role': 'was_mentioned', 'num': (0, 1)},
                'Tool': {'role': 'was_mentioned', 'num': (0, 1)},
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'poster', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Mention': {'role': 'was_created', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'poster', 'num': (1, 1)},
                'Mention': {'role': 'was_created', 'num': (1, 1)}
            }
        }
    },
    'Report generation': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'was_attached', 'num': (0, 1)},
                'Dashboard': {'role': 'was_attached', 'num': (0, 1)},
                'App': {'role': 'was_attached', 'num': (0, 1)},
                'Notebook': {'role': 'was_attached', 'num': (0, 1)},
                'Protocol': {'role': 'was_attached', 'num': (0, 1)},
                'State': {'role': 'was_attached', 'num': (0, 1)},
                'Report': {'role': 'was_referenced', 'num': (0, 1)},
                'Memo': {'role': 'was_referenced', 'num': (0, 1)},
                'Tool': {'role': 'was_referenced', 'num': (0, 1)},
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'author', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Report': {'role': 'was_created', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'author', 'num': (1, 1)},
                'Report': {'role': 'was_created', 'num': (1, 1)}
            }
        }
    },
    'Memoization': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'was_attached', 'num': (0, 1)},
                'Dashboard': {'role': 'was_attached', 'num': (0, 1)},
                'App': {'role': 'was_attached', 'num': (0, 1)},
                'Notebook': {'role': 'was_attached', 'num': (0, 1)},
                'Protocol': {'role': 'was_attached', 'num': (0, 1)},
                'State': {'role': 'was_attached', 'num': (0, 1)},
                'Report': {'role': 'was_referenced', 'num': (0, 1)},
                'Memo': {'role': 'was_referenced', 'num': (0, 1)},
                'Tool': {'role': 'was_referenced', 'num': (0, 1)},
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'author', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Memo': {'role': 'was_created', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'author', 'num': (1, 1)},
                'Memo': {'role': 'was_created', 'num': (1, 1)}
            }
        }
    },
    'Starred': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'was_referenced', 'num': (0, 1)},
                'Dashboard': {'role': 'was_referenced', 'num': (0, 1)},
                'App': {'role': 'was_referenced', 'num': (0, 1)},
                'Notebook': {'role': 'was_referenced', 'num': (0, 1)},
                'Protocol': {'role': 'was_referenced', 'num': (0, 1)},
                'State': {'role': 'was_referenced', 'num': (0, 1)},
                'Report': {'role': 'was_referenced', 'num': (0, 1)},
                'Memo': {'role': 'was_referenced', 'num': (0, 1)},
                'Tool': {'role': 'was_referenced', 'num': (0, 1)},
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'author', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Memo': {'role': 'was_created', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'author', 'num': (1, 1)},
                'Memo': {'role': 'was_created', 'num': (1, 1)}
            }
        }
    }
}
