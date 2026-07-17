"""Tests for catalog_00883."""

import pytest

from cartservice.generated.catalog_00883 import (
    Product_00883,
    bucket_by_tag_00883,
    is_valid_sku_00883,
    price_with_tax_00883,
)


def test_price_with_tax_00883():
    assert price_with_tax_00883(1000, 500) == 1050


def test_price_with_tax_negative_00883():
    with pytest.raises(ValueError):
        price_with_tax_00883(1000, -1)


def test_is_valid_sku_00883():
    assert is_valid_sku_00883("abc123")
    assert not is_valid_sku_00883("")


def test_bucket_by_tag_00883():
    p = Product_00883("s1", 100, ["a"])
    assert bucket_by_tag_00883([p]) == {"a": ["s1"]}
