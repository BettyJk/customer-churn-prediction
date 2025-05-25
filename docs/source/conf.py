# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme

project = 'Customer Churn Prediction'
copyright = '0.1, Hajar el Hadri & Bouthayna Jouak & Hattaki Kawter & Fatima El Fadili & Mohamed Laraisse & Ghofrane Alaoui Mdaghri'
author = 'Hajar el Hadri & Bouthayna Jouak & Hattaki Kawter & Fatima El Fadili & Mohamed Laraisse & Ghofrane Alaoui Mdaghri'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'
extensions = ['sphinx_rtd_theme']

html_static_path = ['_static']
