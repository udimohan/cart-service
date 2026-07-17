"""Tests for catalog_00579."""

import pytest

from cartservice.generated.catalog_00579 import (
    Product_00579,
    bucket_by_tag_00579,
    is_valid_sku_00579,
    price_with_tax_00579,
)


def test_price_with_tax_00579():
    assert price_with_tax_00579(1000, 500) == 1050


def test_price_with_tax_negative_00579():
    with pytest.raises(ValueError):
        price_with_tax_00579(1000, -1)


def test_is_valid_sku_00579():
    assert is_valid_sku_00579("abc123")
    assert not is_valid_sku_00579("")


def test_bucket_by_tag_00579():
    p = Product_00579("s1", 100, ["a"])
    assert bucket_by_tag_00579([p]) == {"a": ["s1"]}
