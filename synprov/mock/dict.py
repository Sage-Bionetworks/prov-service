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
                'File': {'role': 'dataToInput', 'num': (1, 1)},
                'Tool': {'role': 'toolToExecute', 'num': (1, 1)}
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'analyst', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'State': {'role': 'state', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'analyst', 'num': (1, 1)},
                'State': {'role': 'state', 'num': (1, 1)}
            }
        }
    },
    'Mention': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'entityToMention', 'num': (0, 1)},
                'Dashboard': {'role': 'entityToMention', 'num': (0, 1)},
                'App': {'role': 'entityToMention', 'num': (0, 1)},
                'Notebook': {'role': 'entityToMention', 'num': (0, 1)},
                'Protocol': {'role': 'entityToMention', 'num': (0, 1)},
                'State': {'role': 'entityToMention', 'num': (0, 1)},
                'Report': {'role': 'entityToMention', 'num': (0, 1)},
                'Memo': {'role': 'entityToMention', 'num': (0, 1)},
                'Tool': {'role': 'entityToMention', 'num': (0, 1)},
                'Message': {'role': 'entityToMention', 'num': (0, 1)}
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'author', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Message': {'role': 'message', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'author', 'num': (1, 1)},
                'Message': {'role': 'message', 'num': (1, 1)}
            }
        }
    },
    'Report generation': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'entityToReference', 'num': (0, 1)},
                'Dashboard': {'role': 'entityToReference', 'num': (0, 1)},
                'App': {'role': 'entityToReference', 'num': (0, 1)},
                'Notebook': {'role': 'entityToReference', 'num': (0, 1)},
                'Protocol': {'role': 'entityToReference', 'num': (0, 1)},
                'State': {'role': 'entityToReference', 'num': (0, 1)},
                'Report': {'role': 'entityToReference', 'num': (0, 1)},
                'Memo': {'role': 'entityToReference', 'num': (0, 1)},
                'Tool': {'role': 'entityToReference', 'num': (0, 1)},
                'Message': {'role': 'entityToReference', 'num': (0, 1)}
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'author', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Report': {'role': 'report', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'author', 'num': (1, 1)},
                'Report': {'role': 'report', 'num': (1, 1)}
            }
        }
    },
    'Memoization': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Dashboard': {'role': 'entityToMemoize', 'num': (0, 1)},
                'App': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Notebook': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Protocol': {'role': 'entityToMemoize', 'num': (0, 1)},
                'State': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Report': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Memo': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Tool': {'role': 'entityToMemoize', 'num': (0, 1)},
                'Message': {'role': 'entityToMemoize', 'num': (0, 1)}
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'author', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Memo': {'role': 'memo', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'author', 'num': (1, 1)},
                'Memo': {'role': 'memo', 'num': (1, 1)}
            }
        }
    },
    'Starred': {
        'in_subclass': {
            'USED': {
                'File': {'role': 'entityToStar', 'num': (0, 1)},
                'Dashboard': {'role': 'entityToStar', 'num': (0, 1)},
                'App': {'role': 'entityToStar', 'num': (0, 1)},
                'Notebook': {'role': 'entityToStar', 'num': (0, 1)},
                'Protocol': {'role': 'entityToStar', 'num': (0, 1)},
                'State': {'role': 'entityToStar', 'num': (0, 1)},
                'Report': {'role': 'entityToStar', 'num': (0, 1)},
                'Memo': {'role': 'entityToStar', 'num': (0, 1)},
                'Tool': {'role': 'entityToStar', 'num': (0, 1)},
                'Message': {'role': 'entityToStar', 'num': (0, 1)}
            },
            'WASASSOCIATEDWITH': {
                'Agent': {'role': 'creator', 'num': (1, 1)}
            }
        },
        'out_subclass': {
            'WASGENERATEDBY': {
                'Star': {'role': 'star', 'num': (1, 1)}
            },
            'WASATTRIBUTEDTO': {
                'Agent': {'role': 'creator', 'num': (1, 1)},
                'Star': {'role': 'star', 'num': (1, 1)}
            }
        }
    }
}
