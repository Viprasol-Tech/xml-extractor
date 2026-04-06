"""
xml-extractor - Extract and query data from XML documents

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import XmlExtractor, extract, process, main

__all__ = ["XmlExtractor", "extract", "process", "main"]
