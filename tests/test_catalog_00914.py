"""Tests for catalog_00914."""

import pytest

from cartservice.generated.catalog_00914 import (
    Product_00914,
    bucket_by_tag_00914,
    is_valid_sku_00914,
    price_with_tax_00914,
)


def test_price_with_tax_00914():
    assert price_with_tax_00914(1000, 500) == 1050


def test_price_with_tax_negative_00914():
    with pytest.raises(ValueError):
        price_with_tax_00914(1000, -1)


def test_is_valid_sku_00914():
    assert is_valid_sku_00914("abc123")
    assert not is_valid_sku_00914("")


def test_bucket_by_tag_00914():
    p = Product_00914("s1", 100, ["a"])
    assert bucket_by_tag_00914([p]) == {"a": ["s1"]}
