"""Tests for catalog_01229."""

import pytest

from cartservice.generated.catalog_01229 import (
    Product_01229,
    bucket_by_tag_01229,
    is_valid_sku_01229,
    price_with_tax_01229,
)


def test_price_with_tax_01229():
    assert price_with_tax_01229(1000, 500) == 1050


def test_price_with_tax_negative_01229():
    with pytest.raises(ValueError):
        price_with_tax_01229(1000, -1)


def test_is_valid_sku_01229():
    assert is_valid_sku_01229("abc123")
    assert not is_valid_sku_01229("")


def test_bucket_by_tag_01229():
    p = Product_01229("s1", 100, ["a"])
    assert bucket_by_tag_01229([p]) == {"a": ["s1"]}
