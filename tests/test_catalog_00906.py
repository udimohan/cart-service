"""Tests for catalog_00906."""

import pytest

from cartservice.generated.catalog_00906 import (
    Product_00906,
    bucket_by_tag_00906,
    is_valid_sku_00906,
    price_with_tax_00906,
)


def test_price_with_tax_00906():
    assert price_with_tax_00906(1000, 500) == 1050


def test_price_with_tax_negative_00906():
    with pytest.raises(ValueError):
        price_with_tax_00906(1000, -1)


def test_is_valid_sku_00906():
    assert is_valid_sku_00906("abc123")
    assert not is_valid_sku_00906("")


def test_bucket_by_tag_00906():
    p = Product_00906("s1", 100, ["a"])
    assert bucket_by_tag_00906([p]) == {"a": ["s1"]}
