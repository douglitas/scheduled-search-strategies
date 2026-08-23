#!/usr/bin/env python3
"""Genera los tres prompts completos = profile.md + common-v1.md + branches-<rutina>.md.

Existen tres ficheros de instrucciones casi identicos y en el tracker hermano
eso ya causo un fallo real: una contradiccion vivia en los tres a la vez. La
parte comun (y el perfil de la candidata) se edita UNA vez y se regenera. Las
routines leen prompts/out/<rutina>.md del propio repo: editar aqui cambia la
rutina sin tocar el disparador.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
profile = open(os.path.join(HERE, 'profile.md'), encoding='utf-8').read().rstrip()
common = open(os.path.join(HERE, 'common-v1.md'), encoding='utf-8').read().rstrip()
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
for r in ('positions', 'fellowships', 'ecosystem'):
    b = open(os.path.join(HERE, f'branches-{r}.md'), encoding='utf-8').read().strip()
    p = os.path.join(HERE, 'out', f'{r}.md')
    open(p, 'w', encoding='utf-8').write(profile + '\n\n' + common + '\n\n' + b + '\n')
    print(f'{p}  {os.path.getsize(p)} caracteres')
