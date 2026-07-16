"""Tests for catalog_01603."""

import pytest

from cartservice.generated.catalog_01603 import (
    Product_01603,
    bucket_by_tag_01603,
    is_valid_sku_01603,
    price_with_tax_01603,
)


def test_price_with_tax_01603():
    assert price_with_tax_01603(1000, 500) == 1050


def test_price_with_tax_negative_01603():
    with pytest.raises(ValueError):
        price_with_tax_01603(1000, -1)


def test_is_valid_sku_01603():
    assert is_valid_sku_01603("abc123")
    assert not is_valid_sku_01603("")


def test_bucket_by_tag_01603():
    p = Product_01603("s1", 100, ["a"])
    assert bucket_by_tag_01603([p]) == {"a": ["s1"]}
