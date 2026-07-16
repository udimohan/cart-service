"""Tests for catalog_01545."""

import pytest

from cartservice.generated.catalog_01545 import (
    Product_01545,
    bucket_by_tag_01545,
    is_valid_sku_01545,
    price_with_tax_01545,
)


def test_price_with_tax_01545():
    assert price_with_tax_01545(1000, 500) == 1050


def test_price_with_tax_negative_01545():
    with pytest.raises(ValueError):
        price_with_tax_01545(1000, -1)


def test_is_valid_sku_01545():
    assert is_valid_sku_01545("abc123")
    assert not is_valid_sku_01545("")


def test_bucket_by_tag_01545():
    p = Product_01545("s1", 100, ["a"])
    assert bucket_by_tag_01545([p]) == {"a": ["s1"]}
