"""Tests for catalog_00381."""

import pytest

from cartservice.generated.catalog_00381 import (
    Product_00381,
    bucket_by_tag_00381,
    is_valid_sku_00381,
    price_with_tax_00381,
)


def test_price_with_tax_00381():
    assert price_with_tax_00381(1000, 500) == 1050


def test_price_with_tax_negative_00381():
    with pytest.raises(ValueError):
        price_with_tax_00381(1000, -1)


def test_is_valid_sku_00381():
    assert is_valid_sku_00381("abc123")
    assert not is_valid_sku_00381("")


def test_bucket_by_tag_00381():
    p = Product_00381("s1", 100, ["a"])
    assert bucket_by_tag_00381([p]) == {"a": ["s1"]}
