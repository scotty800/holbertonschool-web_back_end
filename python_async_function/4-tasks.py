#!/usr/bin/env python3
''' async and await syntax '''


import asyncio
from typing import List


get = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Fonction qui retourne une liste de délais en ordre croissant
    en utilisant des tâches asyncio.
    
    Args:
        n (int): Le nombre de fois où appeler task_wait_random.
        max_delay (int): Le délai maximal en secondes pour chaque tâche.
        
    Returns:
        List[float]: Liste des délais en ordre croissant.
    '''
    lst = [get(max_delay) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(lst)]
    return finish
