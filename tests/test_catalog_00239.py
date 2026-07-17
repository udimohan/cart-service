"""Tests for catalog_00239."""

import pytest

from cartservice.generated.catalog_00239 import (
    Product_00239,
    bucket_by_tag_00239,
    is_valid_sku_00239,
    price_with_tax_00239,
)


def test_price_with_tax_00239():
    assert price_with_tax_00239(1000, 500) == 1050


def test_price_with_tax_negative_00239():
    with pytest.raises(ValueError):
        price_with_tax_00239(1000, -1)


def test_is_valid_sku_00239():
    assert is_valid_sku_00239("abc123")
    assert not is_valid_sku_00239("")


def test_bucket_by_tag_00239():
    p = Product_00239("s1", 100, ["a"])
    assert bucket_by_tag_00239([p]) == {"a": ["s1"]}
