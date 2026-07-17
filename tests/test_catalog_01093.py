"""Tests for catalog_01093."""

import pytest

from cartservice.generated.catalog_01093 import (
    Product_01093,
    bucket_by_tag_01093,
    is_valid_sku_01093,
    price_with_tax_01093,
)


def test_price_with_tax_01093():
    assert price_with_tax_01093(1000, 500) == 1050


def test_price_with_tax_negative_01093():
    with pytest.raises(ValueError):
        price_with_tax_01093(1000, -1)


def test_is_valid_sku_01093():
    assert is_valid_sku_01093("abc123")
    assert not is_valid_sku_01093("")


def test_bucket_by_tag_01093():
    p = Product_01093("s1", 100, ["a"])
    assert bucket_by_tag_01093([p]) == {"a": ["s1"]}
