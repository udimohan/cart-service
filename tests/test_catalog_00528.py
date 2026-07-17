"""Tests for catalog_00528."""

import pytest

from cartservice.generated.catalog_00528 import (
    Product_00528,
    bucket_by_tag_00528,
    is_valid_sku_00528,
    price_with_tax_00528,
)


def test_price_with_tax_00528():
    assert price_with_tax_00528(1000, 500) == 1050


def test_price_with_tax_negative_00528():
    with pytest.raises(ValueError):
        price_with_tax_00528(1000, -1)


def test_is_valid_sku_00528():
    assert is_valid_sku_00528("abc123")
    assert not is_valid_sku_00528("")


def test_bucket_by_tag_00528():
    p = Product_00528("s1", 100, ["a"])
    assert bucket_by_tag_00528([p]) == {"a": ["s1"]}
