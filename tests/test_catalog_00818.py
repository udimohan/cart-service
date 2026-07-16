"""Tests for catalog_00818."""

import pytest

from cartservice.generated.catalog_00818 import (
    Product_00818,
    bucket_by_tag_00818,
    is_valid_sku_00818,
    price_with_tax_00818,
)


def test_price_with_tax_00818():
    assert price_with_tax_00818(1000, 500) == 1050


def test_price_with_tax_negative_00818():
    with pytest.raises(ValueError):
        price_with_tax_00818(1000, -1)


def test_is_valid_sku_00818():
    assert is_valid_sku_00818("abc123")
    assert not is_valid_sku_00818("")


def test_bucket_by_tag_00818():
    p = Product_00818("s1", 100, ["a"])
    assert bucket_by_tag_00818([p]) == {"a": ["s1"]}
