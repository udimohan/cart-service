"""Tests for catalog_00326."""

import pytest

from cartservice.generated.catalog_00326 import (
    Product_00326,
    bucket_by_tag_00326,
    is_valid_sku_00326,
    price_with_tax_00326,
)


def test_price_with_tax_00326():
    assert price_with_tax_00326(1000, 500) == 1050


def test_price_with_tax_negative_00326():
    with pytest.raises(ValueError):
        price_with_tax_00326(1000, -1)


def test_is_valid_sku_00326():
    assert is_valid_sku_00326("abc123")
    assert not is_valid_sku_00326("")


def test_bucket_by_tag_00326():
    p = Product_00326("s1", 100, ["a"])
    assert bucket_by_tag_00326([p]) == {"a": ["s1"]}
