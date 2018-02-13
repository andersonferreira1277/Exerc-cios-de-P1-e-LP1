from setuptools import setup, find_packages


setup(
    name="Gerador de Documentos",
    version="0.1",
    packages=find_packages(),
    install_requires=['pyqt5','python-docx']
)