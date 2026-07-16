"""Tests for catalog_01221."""

import pytest

from cartservice.generated.catalog_01221 import (
    Product_01221,
    bucket_by_tag_01221,
    is_valid_sku_01221,
    price_with_tax_01221,
)


def test_price_with_tax_01221():
    assert price_with_tax_01221(1000, 500) == 1050


def test_price_with_tax_negative_01221():
    with pytest.raises(ValueError):
        price_with_tax_01221(1000, -1)


def test_is_valid_sku_01221():
    assert is_valid_sku_01221("abc123")
    assert not is_valid_sku_01221("")


def test_bucket_by_tag_01221():
    p = Product_01221("s1", 100, ["a"])
    assert bucket_by_tag_01221([p]) == {"a": ["s1"]}
