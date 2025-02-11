import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = '0.0.0'

REPO_NAME = 'mental-health-treatment-predictor'
AUTHOR_USER_NAME = "saGit1990"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "suel.abbasi@outlook.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package to detect whether a person is how likely to get mental health treatment",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)