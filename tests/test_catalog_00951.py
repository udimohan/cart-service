"""Tests for catalog_00951."""

import pytest

from cartservice.generated.catalog_00951 import (
    Product_00951,
    bucket_by_tag_00951,
    is_valid_sku_00951,
    price_with_tax_00951,
)


def test_price_with_tax_00951():
    assert price_with_tax_00951(1000, 500) == 1050


def test_price_with_tax_negative_00951():
    with pytest.raises(ValueError):
        price_with_tax_00951(1000, -1)


def test_is_valid_sku_00951():
    assert is_valid_sku_00951("abc123")
    assert not is_valid_sku_00951("")


def test_bucket_by_tag_00951():
    p = Product_00951("s1", 100, ["a"])
    assert bucket_by_tag_00951([p]) == {"a": ["s1"]}
