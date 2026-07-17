"""Tests for catalog_01125."""

import pytest

from cartservice.generated.catalog_01125 import (
    Product_01125,
    bucket_by_tag_01125,
    is_valid_sku_01125,
    price_with_tax_01125,
)


def test_price_with_tax_01125():
    assert price_with_tax_01125(1000, 500) == 1050


def test_price_with_tax_negative_01125():
    with pytest.raises(ValueError):
        price_with_tax_01125(1000, -1)


def test_is_valid_sku_01125():
    assert is_valid_sku_01125("abc123")
    assert not is_valid_sku_01125("")


def test_bucket_by_tag_01125():
    p = Product_01125("s1", 100, ["a"])
    assert bucket_by_tag_01125([p]) == {"a": ["s1"]}
