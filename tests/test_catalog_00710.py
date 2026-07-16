"""Tests for catalog_00710."""

import pytest

from cartservice.generated.catalog_00710 import (
    Product_00710,
    bucket_by_tag_00710,
    is_valid_sku_00710,
    price_with_tax_00710,
)


def test_price_with_tax_00710():
    assert price_with_tax_00710(1000, 500) == 1050


def test_price_with_tax_negative_00710():
    with pytest.raises(ValueError):
        price_with_tax_00710(1000, -1)


def test_is_valid_sku_00710():
    assert is_valid_sku_00710("abc123")
    assert not is_valid_sku_00710("")


def test_bucket_by_tag_00710():
    p = Product_00710("s1", 100, ["a"])
    assert bucket_by_tag_00710([p]) == {"a": ["s1"]}
