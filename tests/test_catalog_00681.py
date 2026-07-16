"""Tests for catalog_00681."""

import pytest

from cartservice.generated.catalog_00681 import (
    Product_00681,
    bucket_by_tag_00681,
    is_valid_sku_00681,
    price_with_tax_00681,
)


def test_price_with_tax_00681():
    assert price_with_tax_00681(1000, 500) == 1050


def test_price_with_tax_negative_00681():
    with pytest.raises(ValueError):
        price_with_tax_00681(1000, -1)


def test_is_valid_sku_00681():
    assert is_valid_sku_00681("abc123")
    assert not is_valid_sku_00681("")


def test_bucket_by_tag_00681():
    p = Product_00681("s1", 100, ["a"])
    assert bucket_by_tag_00681([p]) == {"a": ["s1"]}
