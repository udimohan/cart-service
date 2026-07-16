"""Tests for catalog_01152."""

import pytest

from cartservice.generated.catalog_01152 import (
    Product_01152,
    bucket_by_tag_01152,
    is_valid_sku_01152,
    price_with_tax_01152,
)


def test_price_with_tax_01152():
    assert price_with_tax_01152(1000, 500) == 1050


def test_price_with_tax_negative_01152():
    with pytest.raises(ValueError):
        price_with_tax_01152(1000, -1)


def test_is_valid_sku_01152():
    assert is_valid_sku_01152("abc123")
    assert not is_valid_sku_01152("")


def test_bucket_by_tag_01152():
    p = Product_01152("s1", 100, ["a"])
    assert bucket_by_tag_01152([p]) == {"a": ["s1"]}
