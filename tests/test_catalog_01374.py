"""Tests for catalog_01374."""

import pytest

from cartservice.generated.catalog_01374 import (
    Product_01374,
    bucket_by_tag_01374,
    is_valid_sku_01374,
    price_with_tax_01374,
)


def test_price_with_tax_01374():
    assert price_with_tax_01374(1000, 500) == 1050


def test_price_with_tax_negative_01374():
    with pytest.raises(ValueError):
        price_with_tax_01374(1000, -1)


def test_is_valid_sku_01374():
    assert is_valid_sku_01374("abc123")
    assert not is_valid_sku_01374("")


def test_bucket_by_tag_01374():
    p = Product_01374("s1", 100, ["a"])
    assert bucket_by_tag_01374([p]) == {"a": ["s1"]}
