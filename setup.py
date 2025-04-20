from setuptools import find_packages,setup
def get_requirements(file):
    with open(file) as file_obj:
        requires=file_obj.readlines()
        requires=[req.replace("\n"," ") for req in requires]
        if "-e ." in requires:
            requires.remove("-e .")
    
    return requires
    


setup(
    name="ML project Setup",
    version="0.0.1",
    author="Shaik Abdul Rehaman",
    author_email="rehamanshaik000@gmail.com",
    install_requires=get_requirements("requirements.txt")
    
)