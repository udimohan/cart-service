"""Tests for catalog_01148."""

import pytest

from cartservice.generated.catalog_01148 import (
    Product_01148,
    bucket_by_tag_01148,
    is_valid_sku_01148,
    price_with_tax_01148,
)


def test_price_with_tax_01148():
    assert price_with_tax_01148(1000, 500) == 1050


def test_price_with_tax_negative_01148():
    with pytest.raises(ValueError):
        price_with_tax_01148(1000, -1)


def test_is_valid_sku_01148():
    assert is_valid_sku_01148("abc123")
    assert not is_valid_sku_01148("")


def test_bucket_by_tag_01148():
    p = Product_01148("s1", 100, ["a"])
    assert bucket_by_tag_01148([p]) == {"a": ["s1"]}
