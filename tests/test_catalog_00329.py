"""Tests for catalog_00329."""

import pytest

from cartservice.generated.catalog_00329 import (
    Product_00329,
    bucket_by_tag_00329,
    is_valid_sku_00329,
    price_with_tax_00329,
)


def test_price_with_tax_00329():
    assert price_with_tax_00329(1000, 500) == 1050


def test_price_with_tax_negative_00329():
    with pytest.raises(ValueError):
        price_with_tax_00329(1000, -1)


def test_is_valid_sku_00329():
    assert is_valid_sku_00329("abc123")
    assert not is_valid_sku_00329("")


def test_bucket_by_tag_00329():
    p = Product_00329("s1", 100, ["a"])
    assert bucket_by_tag_00329([p]) == {"a": ["s1"]}
