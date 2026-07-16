"""Tests for catalog_00973."""

import pytest

from cartservice.generated.catalog_00973 import (
    Product_00973,
    bucket_by_tag_00973,
    is_valid_sku_00973,
    price_with_tax_00973,
)


def test_price_with_tax_00973():
    assert price_with_tax_00973(1000, 500) == 1050


def test_price_with_tax_negative_00973():
    with pytest.raises(ValueError):
        price_with_tax_00973(1000, -1)


def test_is_valid_sku_00973():
    assert is_valid_sku_00973("abc123")
    assert not is_valid_sku_00973("")


def test_bucket_by_tag_00973():
    p = Product_00973("s1", 100, ["a"])
    assert bucket_by_tag_00973([p]) == {"a": ["s1"]}
