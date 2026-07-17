"""Tests for catalog_00351."""

import pytest

from cartservice.generated.catalog_00351 import (
    Product_00351,
    bucket_by_tag_00351,
    is_valid_sku_00351,
    price_with_tax_00351,
)


def test_price_with_tax_00351():
    assert price_with_tax_00351(1000, 500) == 1050


def test_price_with_tax_negative_00351():
    with pytest.raises(ValueError):
        price_with_tax_00351(1000, -1)


def test_is_valid_sku_00351():
    assert is_valid_sku_00351("abc123")
    assert not is_valid_sku_00351("")


def test_bucket_by_tag_00351():
    p = Product_00351("s1", 100, ["a"])
    assert bucket_by_tag_00351([p]) == {"a": ["s1"]}
