"""Tests for catalog_01542."""

import pytest

from cartservice.generated.catalog_01542 import (
    Product_01542,
    bucket_by_tag_01542,
    is_valid_sku_01542,
    price_with_tax_01542,
)


def test_price_with_tax_01542():
    assert price_with_tax_01542(1000, 500) == 1050


def test_price_with_tax_negative_01542():
    with pytest.raises(ValueError):
        price_with_tax_01542(1000, -1)


def test_is_valid_sku_01542():
    assert is_valid_sku_01542("abc123")
    assert not is_valid_sku_01542("")


def test_bucket_by_tag_01542():
    p = Product_01542("s1", 100, ["a"])
    assert bucket_by_tag_01542([p]) == {"a": ["s1"]}
