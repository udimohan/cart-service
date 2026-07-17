"""Tests for catalog_00031."""

import pytest

from cartservice.generated.catalog_00031 import (
    Product_00031,
    bucket_by_tag_00031,
    is_valid_sku_00031,
    price_with_tax_00031,
)


def test_price_with_tax_00031():
    assert price_with_tax_00031(1000, 500) == 1050


def test_price_with_tax_negative_00031():
    with pytest.raises(ValueError):
        price_with_tax_00031(1000, -1)


def test_is_valid_sku_00031():
    assert is_valid_sku_00031("abc123")
    assert not is_valid_sku_00031("")


def test_bucket_by_tag_00031():
    p = Product_00031("s1", 100, ["a"])
    assert bucket_by_tag_00031([p]) == {"a": ["s1"]}
