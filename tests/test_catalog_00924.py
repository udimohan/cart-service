"""Tests for catalog_00924."""

import pytest

from cartservice.generated.catalog_00924 import (
    Product_00924,
    bucket_by_tag_00924,
    is_valid_sku_00924,
    price_with_tax_00924,
)


def test_price_with_tax_00924():
    assert price_with_tax_00924(1000, 500) == 1050


def test_price_with_tax_negative_00924():
    with pytest.raises(ValueError):
        price_with_tax_00924(1000, -1)


def test_is_valid_sku_00924():
    assert is_valid_sku_00924("abc123")
    assert not is_valid_sku_00924("")


def test_bucket_by_tag_00924():
    p = Product_00924("s1", 100, ["a"])
    assert bucket_by_tag_00924([p]) == {"a": ["s1"]}
