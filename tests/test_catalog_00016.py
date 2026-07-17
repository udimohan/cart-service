"""Tests for catalog_00016."""

import pytest

from cartservice.generated.catalog_00016 import (
    Product_00016,
    bucket_by_tag_00016,
    is_valid_sku_00016,
    price_with_tax_00016,
)


def test_price_with_tax_00016():
    assert price_with_tax_00016(1000, 500) == 1050


def test_price_with_tax_negative_00016():
    with pytest.raises(ValueError):
        price_with_tax_00016(1000, -1)


def test_is_valid_sku_00016():
    assert is_valid_sku_00016("abc123")
    assert not is_valid_sku_00016("")


def test_bucket_by_tag_00016():
    p = Product_00016("s1", 100, ["a"])
    assert bucket_by_tag_00016([p]) == {"a": ["s1"]}
