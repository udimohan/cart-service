"""Tests for catalog_00025."""

import pytest

from cartservice.generated.catalog_00025 import (
    Product_00025,
    bucket_by_tag_00025,
    is_valid_sku_00025,
    price_with_tax_00025,
)


def test_price_with_tax_00025():
    assert price_with_tax_00025(1000, 500) == 1050


def test_price_with_tax_negative_00025():
    with pytest.raises(ValueError):
        price_with_tax_00025(1000, -1)


def test_is_valid_sku_00025():
    assert is_valid_sku_00025("abc123")
    assert not is_valid_sku_00025("")


def test_bucket_by_tag_00025():
    p = Product_00025("s1", 100, ["a"])
    assert bucket_by_tag_00025([p]) == {"a": ["s1"]}
