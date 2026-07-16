"""Tests for catalog_00285."""

import pytest

from cartservice.generated.catalog_00285 import (
    Product_00285,
    bucket_by_tag_00285,
    is_valid_sku_00285,
    price_with_tax_00285,
)


def test_price_with_tax_00285():
    assert price_with_tax_00285(1000, 500) == 1050


def test_price_with_tax_negative_00285():
    with pytest.raises(ValueError):
        price_with_tax_00285(1000, -1)


def test_is_valid_sku_00285():
    assert is_valid_sku_00285("abc123")
    assert not is_valid_sku_00285("")


def test_bucket_by_tag_00285():
    p = Product_00285("s1", 100, ["a"])
    assert bucket_by_tag_00285([p]) == {"a": ["s1"]}
