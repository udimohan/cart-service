"""Tests for catalog_01671."""

import pytest

from cartservice.generated.catalog_01671 import (
    Product_01671,
    bucket_by_tag_01671,
    is_valid_sku_01671,
    price_with_tax_01671,
)


def test_price_with_tax_01671():
    assert price_with_tax_01671(1000, 500) == 1050


def test_price_with_tax_negative_01671():
    with pytest.raises(ValueError):
        price_with_tax_01671(1000, -1)


def test_is_valid_sku_01671():
    assert is_valid_sku_01671("abc123")
    assert not is_valid_sku_01671("")


def test_bucket_by_tag_01671():
    p = Product_01671("s1", 100, ["a"])
    assert bucket_by_tag_01671([p]) == {"a": ["s1"]}
