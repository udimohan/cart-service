"""Tests for catalog_00301."""

import pytest

from cartservice.generated.catalog_00301 import (
    Product_00301,
    bucket_by_tag_00301,
    is_valid_sku_00301,
    price_with_tax_00301,
)


def test_price_with_tax_00301():
    assert price_with_tax_00301(1000, 500) == 1050


def test_price_with_tax_negative_00301():
    with pytest.raises(ValueError):
        price_with_tax_00301(1000, -1)


def test_is_valid_sku_00301():
    assert is_valid_sku_00301("abc123")
    assert not is_valid_sku_00301("")


def test_bucket_by_tag_00301():
    p = Product_00301("s1", 100, ["a"])
    assert bucket_by_tag_00301([p]) == {"a": ["s1"]}
