from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT ='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    Get all requirements from requirements.txt
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)    
    
    
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Yipu Lerina ',
    author_email='yipulerina29@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
)