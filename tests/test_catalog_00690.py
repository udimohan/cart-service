"""Tests for catalog_00690."""

import pytest

from cartservice.generated.catalog_00690 import (
    Product_00690,
    bucket_by_tag_00690,
    is_valid_sku_00690,
    price_with_tax_00690,
)


def test_price_with_tax_00690():
    assert price_with_tax_00690(1000, 500) == 1050


def test_price_with_tax_negative_00690():
    with pytest.raises(ValueError):
        price_with_tax_00690(1000, -1)


def test_is_valid_sku_00690():
    assert is_valid_sku_00690("abc123")
    assert not is_valid_sku_00690("")


def test_bucket_by_tag_00690():
    p = Product_00690("s1", 100, ["a"])
    assert bucket_by_tag_00690([p]) == {"a": ["s1"]}
