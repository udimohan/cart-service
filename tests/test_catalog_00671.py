"""Tests for catalog_00671."""

import pytest

from cartservice.generated.catalog_00671 import (
    Product_00671,
    bucket_by_tag_00671,
    is_valid_sku_00671,
    price_with_tax_00671,
)


def test_price_with_tax_00671():
    assert price_with_tax_00671(1000, 500) == 1050


def test_price_with_tax_negative_00671():
    with pytest.raises(ValueError):
        price_with_tax_00671(1000, -1)


def test_is_valid_sku_00671():
    assert is_valid_sku_00671("abc123")
    assert not is_valid_sku_00671("")


def test_bucket_by_tag_00671():
    p = Product_00671("s1", 100, ["a"])
    assert bucket_by_tag_00671([p]) == {"a": ["s1"]}
