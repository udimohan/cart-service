"""Tests for catalog_00511."""

import pytest

from cartservice.generated.catalog_00511 import (
    Product_00511,
    bucket_by_tag_00511,
    is_valid_sku_00511,
    price_with_tax_00511,
)


def test_price_with_tax_00511():
    assert price_with_tax_00511(1000, 500) == 1050


def test_price_with_tax_negative_00511():
    with pytest.raises(ValueError):
        price_with_tax_00511(1000, -1)


def test_is_valid_sku_00511():
    assert is_valid_sku_00511("abc123")
    assert not is_valid_sku_00511("")


def test_bucket_by_tag_00511():
    p = Product_00511("s1", 100, ["a"])
    assert bucket_by_tag_00511([p]) == {"a": ["s1"]}
