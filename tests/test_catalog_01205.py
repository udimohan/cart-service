"""Tests for catalog_01205."""

import pytest

from cartservice.generated.catalog_01205 import (
    Product_01205,
    bucket_by_tag_01205,
    is_valid_sku_01205,
    price_with_tax_01205,
)


def test_price_with_tax_01205():
    assert price_with_tax_01205(1000, 500) == 1050


def test_price_with_tax_negative_01205():
    with pytest.raises(ValueError):
        price_with_tax_01205(1000, -1)


def test_is_valid_sku_01205():
    assert is_valid_sku_01205("abc123")
    assert not is_valid_sku_01205("")


def test_bucket_by_tag_01205():
    p = Product_01205("s1", 100, ["a"])
    assert bucket_by_tag_01205([p]) == {"a": ["s1"]}
