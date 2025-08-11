from setuptools import setup, find_packages 
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """ 
    requirements=[]
    hypen_e_dot = "-e ."
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove("-e .")
        return requirements
    
setup(
    name="Yash",    
    version="0.0.1",
    author="Krish",
    author_email="yashwanth0098@gmai.com",
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt') )

