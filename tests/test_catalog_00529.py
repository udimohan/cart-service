"""Tests for catalog_00529."""

import pytest

from cartservice.generated.catalog_00529 import (
    Product_00529,
    bucket_by_tag_00529,
    is_valid_sku_00529,
    price_with_tax_00529,
)


def test_price_with_tax_00529():
    assert price_with_tax_00529(1000, 500) == 1050


def test_price_with_tax_negative_00529():
    with pytest.raises(ValueError):
        price_with_tax_00529(1000, -1)


def test_is_valid_sku_00529():
    assert is_valid_sku_00529("abc123")
    assert not is_valid_sku_00529("")


def test_bucket_by_tag_00529():
    p = Product_00529("s1", 100, ["a"])
    assert bucket_by_tag_00529([p]) == {"a": ["s1"]}
