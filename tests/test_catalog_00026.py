"""Tests for catalog_00026."""

import pytest

from cartservice.generated.catalog_00026 import (
    Product_00026,
    bucket_by_tag_00026,
    is_valid_sku_00026,
    price_with_tax_00026,
)


def test_price_with_tax_00026():
    assert price_with_tax_00026(1000, 500) == 1050


def test_price_with_tax_negative_00026():
    with pytest.raises(ValueError):
        price_with_tax_00026(1000, -1)


def test_is_valid_sku_00026():
    assert is_valid_sku_00026("abc123")
    assert not is_valid_sku_00026("")


def test_bucket_by_tag_00026():
    p = Product_00026("s1", 100, ["a"])
    assert bucket_by_tag_00026([p]) == {"a": ["s1"]}
