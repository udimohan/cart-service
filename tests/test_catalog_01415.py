"""Tests for catalog_01415."""

import pytest

from cartservice.generated.catalog_01415 import (
    Product_01415,
    bucket_by_tag_01415,
    is_valid_sku_01415,
    price_with_tax_01415,
)


def test_price_with_tax_01415():
    assert price_with_tax_01415(1000, 500) == 1050


def test_price_with_tax_negative_01415():
    with pytest.raises(ValueError):
        price_with_tax_01415(1000, -1)


def test_is_valid_sku_01415():
    assert is_valid_sku_01415("abc123")
    assert not is_valid_sku_01415("")


def test_bucket_by_tag_01415():
    p = Product_01415("s1", 100, ["a"])
    assert bucket_by_tag_01415([p]) == {"a": ["s1"]}
