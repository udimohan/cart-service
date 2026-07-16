"""Tests for catalog_00594."""

import pytest

from cartservice.generated.catalog_00594 import (
    Product_00594,
    bucket_by_tag_00594,
    is_valid_sku_00594,
    price_with_tax_00594,
)


def test_price_with_tax_00594():
    assert price_with_tax_00594(1000, 500) == 1050


def test_price_with_tax_negative_00594():
    with pytest.raises(ValueError):
        price_with_tax_00594(1000, -1)


def test_is_valid_sku_00594():
    assert is_valid_sku_00594("abc123")
    assert not is_valid_sku_00594("")


def test_bucket_by_tag_00594():
    p = Product_00594("s1", 100, ["a"])
    assert bucket_by_tag_00594([p]) == {"a": ["s1"]}
