import pickle

tags_and_types = {'task': 'double', 'system': 'double',
'meshMovement': 'inline', 'timeStep': 'inline',
'plasticity': 'inline', 'matrixDecomposition': 'inline',
'bodies': 'double', 'body': 'double', 
'mesh': 'inline', 'material': 'inline', 
'borderCondition': 'double', 'area': 'inline'
}

tags_and_params = {'task': ['numberOfSnaps', 'stepsPerSnap'],
'system': [], 'meshMovement': ['type'], 'timeStep': ['multiplier'],
'plasticity': ['type'], 'matrixDecomposition': ['implementation'],
'bodies': [], 'body': ['id'], 'mesh': ['id', 'type', 'file', 'tetrSize'],
'material': ['id'], 
'borderCondition': ['calculator', 'normalStress', 'tangentialStress'],
'area': ['type', 'minX', 'maxX', 'minY', 'maxY', 'minZ', 'maxZ']
}

with open('t&p.pickle', 'wb') as f:
	pickle.dump(tags_and_params, f)

with open('t&t.pickle', 'wb') as f:
	pickle.dump(tags_and_types, f)
