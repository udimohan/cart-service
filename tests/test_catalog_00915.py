"""Tests for catalog_00915."""

import pytest

from cartservice.generated.catalog_00915 import (
    Product_00915,
    bucket_by_tag_00915,
    is_valid_sku_00915,
    price_with_tax_00915,
)


def test_price_with_tax_00915():
    assert price_with_tax_00915(1000, 500) == 1050


def test_price_with_tax_negative_00915():
    with pytest.raises(ValueError):
        price_with_tax_00915(1000, -1)


def test_is_valid_sku_00915():
    assert is_valid_sku_00915("abc123")
    assert not is_valid_sku_00915("")


def test_bucket_by_tag_00915():
    p = Product_00915("s1", 100, ["a"])
    assert bucket_by_tag_00915([p]) == {"a": ["s1"]}
