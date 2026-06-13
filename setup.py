from setuptools import find_packages,setup
# ye find_packages kya krta hai ki wo hamare project ke andar jitne bhi packages hai unko automatically find kr leta hai aur unko include kr leta hai hamare distribution me
# ye hamare liye bahut hi convenient hota hai kyunki hume manually har package ko specify karne ki zarurat nahi hoti hai
# to ye saare project ko read kr lega aur saare files ko small packages me divide kr dega aur unko include kr dega hamare distribution me


hyphen_E_DOT = '-e.'

from pathlib import Path
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip()]

        if hyphen_E_DOT in requirements:
            requirements.remove(hyphen_E_DOT)

    return requirements




# setup function ko call krte hai jisme hum apne project ke baare me information dete hai jaise ki name, version, description, author, etc.
setup(
    name="ml_project",
    version='0.0.1',
    author='castimonia',
    author_email='rpandey126.jpsv@gmail.com',
    packages=find_packages(),
    # install_requires=[
    #     'numpy',
    #     'pandas',
    #     'scikit-learn',
    #     'matplotlib',
    #     'seaborn',
    #     'joblib'
    # ]

    # itna mehanat krne ki jagh ham ek function bna dete hai \
    install_requires=get_requirements('requirements.txt')
)







