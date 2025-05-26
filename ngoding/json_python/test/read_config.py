#!/usr/bin/python

import json

with open('config.json') as f:

    config = json.load(f)
    
    print('Theme: {}'.format(config['theme']))
    print('Size: {}'.format(config['size']))
    print('Splash screen: {}'.format(config['splashscreen']))