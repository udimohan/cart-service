"""Tests for catalog_00864."""

import pytest

from cartservice.generated.catalog_00864 import (
    Product_00864,
    bucket_by_tag_00864,
    is_valid_sku_00864,
    price_with_tax_00864,
)


def test_price_with_tax_00864():
    assert price_with_tax_00864(1000, 500) == 1050


def test_price_with_tax_negative_00864():
    with pytest.raises(ValueError):
        price_with_tax_00864(1000, -1)


def test_is_valid_sku_00864():
    assert is_valid_sku_00864("abc123")
    assert not is_valid_sku_00864("")


def test_bucket_by_tag_00864():
    p = Product_00864("s1", 100, ["a"])
    assert bucket_by_tag_00864([p]) == {"a": ["s1"]}
