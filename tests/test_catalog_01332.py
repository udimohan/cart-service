"""Tests for catalog_01332."""

import pytest

from cartservice.generated.catalog_01332 import (
    Product_01332,
    bucket_by_tag_01332,
    is_valid_sku_01332,
    price_with_tax_01332,
)


def test_price_with_tax_01332():
    assert price_with_tax_01332(1000, 500) == 1050


def test_price_with_tax_negative_01332():
    with pytest.raises(ValueError):
        price_with_tax_01332(1000, -1)


def test_is_valid_sku_01332():
    assert is_valid_sku_01332("abc123")
    assert not is_valid_sku_01332("")


def test_bucket_by_tag_01332():
    p = Product_01332("s1", 100, ["a"])
    assert bucket_by_tag_01332([p]) == {"a": ["s1"]}
