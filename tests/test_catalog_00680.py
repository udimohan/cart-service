"""Tests for catalog_00680."""

import pytest

from cartservice.generated.catalog_00680 import (
    Product_00680,
    bucket_by_tag_00680,
    is_valid_sku_00680,
    price_with_tax_00680,
)


def test_price_with_tax_00680():
    assert price_with_tax_00680(1000, 500) == 1050


def test_price_with_tax_negative_00680():
    with pytest.raises(ValueError):
        price_with_tax_00680(1000, -1)


def test_is_valid_sku_00680():
    assert is_valid_sku_00680("abc123")
    assert not is_valid_sku_00680("")


def test_bucket_by_tag_00680():
    p = Product_00680("s1", 100, ["a"])
    assert bucket_by_tag_00680([p]) == {"a": ["s1"]}
