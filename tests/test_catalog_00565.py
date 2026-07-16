"""Tests for catalog_00565."""

import pytest

from cartservice.generated.catalog_00565 import (
    Product_00565,
    bucket_by_tag_00565,
    is_valid_sku_00565,
    price_with_tax_00565,
)


def test_price_with_tax_00565():
    assert price_with_tax_00565(1000, 500) == 1050


def test_price_with_tax_negative_00565():
    with pytest.raises(ValueError):
        price_with_tax_00565(1000, -1)


def test_is_valid_sku_00565():
    assert is_valid_sku_00565("abc123")
    assert not is_valid_sku_00565("")


def test_bucket_by_tag_00565():
    p = Product_00565("s1", 100, ["a"])
    assert bucket_by_tag_00565([p]) == {"a": ["s1"]}
