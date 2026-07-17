"""Tests for catalog_01232."""

import pytest

from cartservice.generated.catalog_01232 import (
    Product_01232,
    bucket_by_tag_01232,
    is_valid_sku_01232,
    price_with_tax_01232,
)


def test_price_with_tax_01232():
    assert price_with_tax_01232(1000, 500) == 1050


def test_price_with_tax_negative_01232():
    with pytest.raises(ValueError):
        price_with_tax_01232(1000, -1)


def test_is_valid_sku_01232():
    assert is_valid_sku_01232("abc123")
    assert not is_valid_sku_01232("")


def test_bucket_by_tag_01232():
    p = Product_01232("s1", 100, ["a"])
    assert bucket_by_tag_01232([p]) == {"a": ["s1"]}
