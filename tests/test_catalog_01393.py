"""Tests for catalog_01393."""

import pytest

from cartservice.generated.catalog_01393 import (
    Product_01393,
    bucket_by_tag_01393,
    is_valid_sku_01393,
    price_with_tax_01393,
)


def test_price_with_tax_01393():
    assert price_with_tax_01393(1000, 500) == 1050


def test_price_with_tax_negative_01393():
    with pytest.raises(ValueError):
        price_with_tax_01393(1000, -1)


def test_is_valid_sku_01393():
    assert is_valid_sku_01393("abc123")
    assert not is_valid_sku_01393("")


def test_bucket_by_tag_01393():
    p = Product_01393("s1", 100, ["a"])
    assert bucket_by_tag_01393([p]) == {"a": ["s1"]}
