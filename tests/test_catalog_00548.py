"""Tests for catalog_00548."""

import pytest

from cartservice.generated.catalog_00548 import (
    Product_00548,
    bucket_by_tag_00548,
    is_valid_sku_00548,
    price_with_tax_00548,
)


def test_price_with_tax_00548():
    assert price_with_tax_00548(1000, 500) == 1050


def test_price_with_tax_negative_00548():
    with pytest.raises(ValueError):
        price_with_tax_00548(1000, -1)


def test_is_valid_sku_00548():
    assert is_valid_sku_00548("abc123")
    assert not is_valid_sku_00548("")


def test_bucket_by_tag_00548():
    p = Product_00548("s1", 100, ["a"])
    assert bucket_by_tag_00548([p]) == {"a": ["s1"]}
