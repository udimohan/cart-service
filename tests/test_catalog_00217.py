"""Tests for catalog_00217."""

import pytest

from cartservice.generated.catalog_00217 import (
    Product_00217,
    bucket_by_tag_00217,
    is_valid_sku_00217,
    price_with_tax_00217,
)


def test_price_with_tax_00217():
    assert price_with_tax_00217(1000, 500) == 1050


def test_price_with_tax_negative_00217():
    with pytest.raises(ValueError):
        price_with_tax_00217(1000, -1)


def test_is_valid_sku_00217():
    assert is_valid_sku_00217("abc123")
    assert not is_valid_sku_00217("")


def test_bucket_by_tag_00217():
    p = Product_00217("s1", 100, ["a"])
    assert bucket_by_tag_00217([p]) == {"a": ["s1"]}
