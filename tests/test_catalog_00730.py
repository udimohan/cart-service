"""Tests for catalog_00730."""

import pytest

from cartservice.generated.catalog_00730 import (
    Product_00730,
    bucket_by_tag_00730,
    is_valid_sku_00730,
    price_with_tax_00730,
)


def test_price_with_tax_00730():
    assert price_with_tax_00730(1000, 500) == 1050


def test_price_with_tax_negative_00730():
    with pytest.raises(ValueError):
        price_with_tax_00730(1000, -1)


def test_is_valid_sku_00730():
    assert is_valid_sku_00730("abc123")
    assert not is_valid_sku_00730("")


def test_bucket_by_tag_00730():
    p = Product_00730("s1", 100, ["a"])
    assert bucket_by_tag_00730([p]) == {"a": ["s1"]}
