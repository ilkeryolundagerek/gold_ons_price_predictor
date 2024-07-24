# setup.py
from setuptools import setup, find_packages

setup(
    name='gold_ons_price_predictor',
    version='0.0.1',
    packages=find_packages(),
    description='A package for predicting Gold-Ons Prices using LSTM',
    author="İlker Turan",
    author_email="ilkerturan@outlook.com",
    url="https://github.com/ilkeryolundagerek/gold_ons_price_predictor",
    install_requires=[
        'numpy', 'pandas', 'tensorflow'
    ],
    entry_points={
        'console_scripts': [
            'predict-gold-ons-price=gold_ons_price_predictor.predict:main'
        ]
    }
)
