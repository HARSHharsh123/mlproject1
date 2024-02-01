from setuptools import setup , find_packages

from typing import List

def  get_requirements(file_path : str) -> List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements = []

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace('\n' , "") for r in requirements]

        return requirements



setup(
    name = "Machine Learning Project",
    version = '0.0.1',
    author = "Harsh Shukla",
    author_email='hs0814497@gamil.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt'),
    discription = "Hello This project is made by Harsh Shukla",
    url='https://github.com/HARSHharsh123/mlproject/tree/main'
)
