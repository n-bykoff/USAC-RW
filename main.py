from xml_maker import make_xml

if __name__ == '__main__':
    materials = ['steel', 'steel_2']

    for material in materials:
        tags = {'task': [1, [150, 1, 'gcm3d.plugins.ndi']], 
        'system': [2, []], 
        'meshMovement': [3, ['none']],
        'loadPlugin': [3, ['ndi']], 
        'bodies': [2, []], 'body': [3, ['ndc_test_steel']],
        'rheology': [4, ['elastic']],
        'mesh': [4, ['ndc_test_steel', 'geo2', 'models/layer-10x10x1.geo', 0.05]], 
        'material': [4, [material]],
        'ndi:emitter': [2, ['emitter_and_sensor', 'true']], 
        'area': [3, ['box', 5.2, 5.5, 5.2, 5.5, 0.99, 1.01]],
        'values': [3, [-100.0]]}

        make_xml(tags, f'testing_xml({material})')