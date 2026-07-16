"""Tests for catalog_00413."""

import pytest

from cartservice.generated.catalog_00413 import (
    Product_00413,
    bucket_by_tag_00413,
    is_valid_sku_00413,
    price_with_tax_00413,
)


def test_price_with_tax_00413():
    assert price_with_tax_00413(1000, 500) == 1050


def test_price_with_tax_negative_00413():
    with pytest.raises(ValueError):
        price_with_tax_00413(1000, -1)


def test_is_valid_sku_00413():
    assert is_valid_sku_00413("abc123")
    assert not is_valid_sku_00413("")


def test_bucket_by_tag_00413():
    p = Product_00413("s1", 100, ["a"])
    assert bucket_by_tag_00413([p]) == {"a": ["s1"]}
