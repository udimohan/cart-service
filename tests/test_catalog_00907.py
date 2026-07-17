"""Tests for catalog_00907."""

import pytest

from cartservice.generated.catalog_00907 import (
    Product_00907,
    bucket_by_tag_00907,
    is_valid_sku_00907,
    price_with_tax_00907,
)


def test_price_with_tax_00907():
    assert price_with_tax_00907(1000, 500) == 1050


def test_price_with_tax_negative_00907():
    with pytest.raises(ValueError):
        price_with_tax_00907(1000, -1)


def test_is_valid_sku_00907():
    assert is_valid_sku_00907("abc123")
    assert not is_valid_sku_00907("")


def test_bucket_by_tag_00907():
    p = Product_00907("s1", 100, ["a"])
    assert bucket_by_tag_00907([p]) == {"a": ["s1"]}
