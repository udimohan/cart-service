"""Tests for catalog_00431."""

import pytest

from cartservice.generated.catalog_00431 import (
    Product_00431,
    bucket_by_tag_00431,
    is_valid_sku_00431,
    price_with_tax_00431,
)


def test_price_with_tax_00431():
    assert price_with_tax_00431(1000, 500) == 1050


def test_price_with_tax_negative_00431():
    with pytest.raises(ValueError):
        price_with_tax_00431(1000, -1)


def test_is_valid_sku_00431():
    assert is_valid_sku_00431("abc123")
    assert not is_valid_sku_00431("")


def test_bucket_by_tag_00431():
    p = Product_00431("s1", 100, ["a"])
    assert bucket_by_tag_00431([p]) == {"a": ["s1"]}
