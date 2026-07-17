"""Tests for catalog_00100."""

import pytest

from cartservice.generated.catalog_00100 import (
    Product_00100,
    bucket_by_tag_00100,
    is_valid_sku_00100,
    price_with_tax_00100,
)


def test_price_with_tax_00100():
    assert price_with_tax_00100(1000, 500) == 1050


def test_price_with_tax_negative_00100():
    with pytest.raises(ValueError):
        price_with_tax_00100(1000, -1)


def test_is_valid_sku_00100():
    assert is_valid_sku_00100("abc123")
    assert not is_valid_sku_00100("")


def test_bucket_by_tag_00100():
    p = Product_00100("s1", 100, ["a"])
    assert bucket_by_tag_00100([p]) == {"a": ["s1"]}
