"""Tests for catalog_01538."""

import pytest

from cartservice.generated.catalog_01538 import (
    Product_01538,
    bucket_by_tag_01538,
    is_valid_sku_01538,
    price_with_tax_01538,
)


def test_price_with_tax_01538():
    assert price_with_tax_01538(1000, 500) == 1050


def test_price_with_tax_negative_01538():
    with pytest.raises(ValueError):
        price_with_tax_01538(1000, -1)


def test_is_valid_sku_01538():
    assert is_valid_sku_01538("abc123")
    assert not is_valid_sku_01538("")


def test_bucket_by_tag_01538():
    p = Product_01538("s1", 100, ["a"])
    assert bucket_by_tag_01538([p]) == {"a": ["s1"]}
