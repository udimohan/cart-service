"""Tests for catalog_00377."""

import pytest

from cartservice.generated.catalog_00377 import (
    Product_00377,
    bucket_by_tag_00377,
    is_valid_sku_00377,
    price_with_tax_00377,
)


def test_price_with_tax_00377():
    assert price_with_tax_00377(1000, 500) == 1050


def test_price_with_tax_negative_00377():
    with pytest.raises(ValueError):
        price_with_tax_00377(1000, -1)


def test_is_valid_sku_00377():
    assert is_valid_sku_00377("abc123")
    assert not is_valid_sku_00377("")


def test_bucket_by_tag_00377():
    p = Product_00377("s1", 100, ["a"])
    assert bucket_by_tag_00377([p]) == {"a": ["s1"]}
