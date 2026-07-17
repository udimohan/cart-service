"""Tests for catalog_00185."""

import pytest

from cartservice.generated.catalog_00185 import (
    Product_00185,
    bucket_by_tag_00185,
    is_valid_sku_00185,
    price_with_tax_00185,
)


def test_price_with_tax_00185():
    assert price_with_tax_00185(1000, 500) == 1050


def test_price_with_tax_negative_00185():
    with pytest.raises(ValueError):
        price_with_tax_00185(1000, -1)


def test_is_valid_sku_00185():
    assert is_valid_sku_00185("abc123")
    assert not is_valid_sku_00185("")


def test_bucket_by_tag_00185():
    p = Product_00185("s1", 100, ["a"])
    assert bucket_by_tag_00185([p]) == {"a": ["s1"]}
