"""Tests for catalog_00115."""

import pytest

from cartservice.generated.catalog_00115 import (
    Product_00115,
    bucket_by_tag_00115,
    is_valid_sku_00115,
    price_with_tax_00115,
)


def test_price_with_tax_00115():
    assert price_with_tax_00115(1000, 500) == 1050


def test_price_with_tax_negative_00115():
    with pytest.raises(ValueError):
        price_with_tax_00115(1000, -1)


def test_is_valid_sku_00115():
    assert is_valid_sku_00115("abc123")
    assert not is_valid_sku_00115("")


def test_bucket_by_tag_00115():
    p = Product_00115("s1", 100, ["a"])
    assert bucket_by_tag_00115([p]) == {"a": ["s1"]}
