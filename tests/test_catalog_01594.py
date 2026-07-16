"""Tests for catalog_01594."""

import pytest

from cartservice.generated.catalog_01594 import (
    Product_01594,
    bucket_by_tag_01594,
    is_valid_sku_01594,
    price_with_tax_01594,
)


def test_price_with_tax_01594():
    assert price_with_tax_01594(1000, 500) == 1050


def test_price_with_tax_negative_01594():
    with pytest.raises(ValueError):
        price_with_tax_01594(1000, -1)


def test_is_valid_sku_01594():
    assert is_valid_sku_01594("abc123")
    assert not is_valid_sku_01594("")


def test_bucket_by_tag_01594():
    p = Product_01594("s1", 100, ["a"])
    assert bucket_by_tag_01594([p]) == {"a": ["s1"]}
