"""Tests for catalog_00220."""

import pytest

from cartservice.generated.catalog_00220 import (
    Product_00220,
    bucket_by_tag_00220,
    is_valid_sku_00220,
    price_with_tax_00220,
)


def test_price_with_tax_00220():
    assert price_with_tax_00220(1000, 500) == 1050


def test_price_with_tax_negative_00220():
    with pytest.raises(ValueError):
        price_with_tax_00220(1000, -1)


def test_is_valid_sku_00220():
    assert is_valid_sku_00220("abc123")
    assert not is_valid_sku_00220("")


def test_bucket_by_tag_00220():
    p = Product_00220("s1", 100, ["a"])
    assert bucket_by_tag_00220([p]) == {"a": ["s1"]}
