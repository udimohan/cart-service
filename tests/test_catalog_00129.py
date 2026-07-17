"""Tests for catalog_00129."""

import pytest

from cartservice.generated.catalog_00129 import (
    Product_00129,
    bucket_by_tag_00129,
    is_valid_sku_00129,
    price_with_tax_00129,
)


def test_price_with_tax_00129():
    assert price_with_tax_00129(1000, 500) == 1050


def test_price_with_tax_negative_00129():
    with pytest.raises(ValueError):
        price_with_tax_00129(1000, -1)


def test_is_valid_sku_00129():
    assert is_valid_sku_00129("abc123")
    assert not is_valid_sku_00129("")


def test_bucket_by_tag_00129():
    p = Product_00129("s1", 100, ["a"])
    assert bucket_by_tag_00129([p]) == {"a": ["s1"]}
