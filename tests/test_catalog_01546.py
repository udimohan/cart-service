"""Tests for catalog_01546."""

import pytest

from cartservice.generated.catalog_01546 import (
    Product_01546,
    bucket_by_tag_01546,
    is_valid_sku_01546,
    price_with_tax_01546,
)


def test_price_with_tax_01546():
    assert price_with_tax_01546(1000, 500) == 1050


def test_price_with_tax_negative_01546():
    with pytest.raises(ValueError):
        price_with_tax_01546(1000, -1)


def test_is_valid_sku_01546():
    assert is_valid_sku_01546("abc123")
    assert not is_valid_sku_01546("")


def test_bucket_by_tag_01546():
    p = Product_01546("s1", 100, ["a"])
    assert bucket_by_tag_01546([p]) == {"a": ["s1"]}
