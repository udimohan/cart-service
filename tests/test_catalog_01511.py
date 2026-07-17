"""Tests for catalog_01511."""

import pytest

from cartservice.generated.catalog_01511 import (
    Product_01511,
    bucket_by_tag_01511,
    is_valid_sku_01511,
    price_with_tax_01511,
)


def test_price_with_tax_01511():
    assert price_with_tax_01511(1000, 500) == 1050


def test_price_with_tax_negative_01511():
    with pytest.raises(ValueError):
        price_with_tax_01511(1000, -1)


def test_is_valid_sku_01511():
    assert is_valid_sku_01511("abc123")
    assert not is_valid_sku_01511("")


def test_bucket_by_tag_01511():
    p = Product_01511("s1", 100, ["a"])
    assert bucket_by_tag_01511([p]) == {"a": ["s1"]}
