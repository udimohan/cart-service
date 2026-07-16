"""Tests for catalog_01016."""

import pytest

from cartservice.generated.catalog_01016 import (
    Product_01016,
    bucket_by_tag_01016,
    is_valid_sku_01016,
    price_with_tax_01016,
)


def test_price_with_tax_01016():
    assert price_with_tax_01016(1000, 500) == 1050


def test_price_with_tax_negative_01016():
    with pytest.raises(ValueError):
        price_with_tax_01016(1000, -1)


def test_is_valid_sku_01016():
    assert is_valid_sku_01016("abc123")
    assert not is_valid_sku_01016("")


def test_bucket_by_tag_01016():
    p = Product_01016("s1", 100, ["a"])
    assert bucket_by_tag_01016([p]) == {"a": ["s1"]}
