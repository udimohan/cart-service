"""Tests for catalog_00892."""

import pytest

from cartservice.generated.catalog_00892 import (
    Product_00892,
    bucket_by_tag_00892,
    is_valid_sku_00892,
    price_with_tax_00892,
)


def test_price_with_tax_00892():
    assert price_with_tax_00892(1000, 500) == 1050


def test_price_with_tax_negative_00892():
    with pytest.raises(ValueError):
        price_with_tax_00892(1000, -1)


def test_is_valid_sku_00892():
    assert is_valid_sku_00892("abc123")
    assert not is_valid_sku_00892("")


def test_bucket_by_tag_00892():
    p = Product_00892("s1", 100, ["a"])
    assert bucket_by_tag_00892([p]) == {"a": ["s1"]}
