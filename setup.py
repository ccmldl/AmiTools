import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="amitools",
    version="0.1.0",
    author="ccmldl",
    author_email="1738407610@qq.com",
    description="create session and redis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://lidelin@git.netsdl.cn/lidelin/AmiTools",
    packages=setuptools.find_packages(),
    install_requires=["loguru==0.5.3","pyodbc==4.0.30","redis==3.5.3","SQLAlchemy==1.3.23"]
)