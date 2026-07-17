"""Tests for catalog_00457."""

import pytest

from cartservice.generated.catalog_00457 import (
    Product_00457,
    bucket_by_tag_00457,
    is_valid_sku_00457,
    price_with_tax_00457,
)


def test_price_with_tax_00457():
    assert price_with_tax_00457(1000, 500) == 1050


def test_price_with_tax_negative_00457():
    with pytest.raises(ValueError):
        price_with_tax_00457(1000, -1)


def test_is_valid_sku_00457():
    assert is_valid_sku_00457("abc123")
    assert not is_valid_sku_00457("")


def test_bucket_by_tag_00457():
    p = Product_00457("s1", 100, ["a"])
    assert bucket_by_tag_00457([p]) == {"a": ["s1"]}
