"""Tests for catalog_00610."""

import pytest

from cartservice.generated.catalog_00610 import (
    Product_00610,
    bucket_by_tag_00610,
    is_valid_sku_00610,
    price_with_tax_00610,
)


def test_price_with_tax_00610():
    assert price_with_tax_00610(1000, 500) == 1050


def test_price_with_tax_negative_00610():
    with pytest.raises(ValueError):
        price_with_tax_00610(1000, -1)


def test_is_valid_sku_00610():
    assert is_valid_sku_00610("abc123")
    assert not is_valid_sku_00610("")


def test_bucket_by_tag_00610():
    p = Product_00610("s1", 100, ["a"])
    assert bucket_by_tag_00610([p]) == {"a": ["s1"]}
