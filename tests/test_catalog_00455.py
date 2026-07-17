"""Tests for catalog_00455."""

import pytest

from cartservice.generated.catalog_00455 import (
    Product_00455,
    bucket_by_tag_00455,
    is_valid_sku_00455,
    price_with_tax_00455,
)


def test_price_with_tax_00455():
    assert price_with_tax_00455(1000, 500) == 1050


def test_price_with_tax_negative_00455():
    with pytest.raises(ValueError):
        price_with_tax_00455(1000, -1)


def test_is_valid_sku_00455():
    assert is_valid_sku_00455("abc123")
    assert not is_valid_sku_00455("")


def test_bucket_by_tag_00455():
    p = Product_00455("s1", 100, ["a"])
    assert bucket_by_tag_00455([p]) == {"a": ["s1"]}
