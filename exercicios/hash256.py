#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

import hashlib

texto = input('Digite o texto para gerar a hash')
h = hashlib.sha256()
print(texto.encode())
h.update(texto.encode())
print('Hash SHA256: '+h.hexdigest())
