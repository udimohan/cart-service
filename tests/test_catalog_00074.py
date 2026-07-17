"""Tests for catalog_00074."""

import pytest

from cartservice.generated.catalog_00074 import (
    Product_00074,
    bucket_by_tag_00074,
    is_valid_sku_00074,
    price_with_tax_00074,
)


def test_price_with_tax_00074():
    assert price_with_tax_00074(1000, 500) == 1050


def test_price_with_tax_negative_00074():
    with pytest.raises(ValueError):
        price_with_tax_00074(1000, -1)


def test_is_valid_sku_00074():
    assert is_valid_sku_00074("abc123")
    assert not is_valid_sku_00074("")


def test_bucket_by_tag_00074():
    p = Product_00074("s1", 100, ["a"])
    assert bucket_by_tag_00074([p]) == {"a": ["s1"]}
