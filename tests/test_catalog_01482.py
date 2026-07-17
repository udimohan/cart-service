"""Tests for catalog_01482."""

import pytest

from cartservice.generated.catalog_01482 import (
    Product_01482,
    bucket_by_tag_01482,
    is_valid_sku_01482,
    price_with_tax_01482,
)


def test_price_with_tax_01482():
    assert price_with_tax_01482(1000, 500) == 1050


def test_price_with_tax_negative_01482():
    with pytest.raises(ValueError):
        price_with_tax_01482(1000, -1)


def test_is_valid_sku_01482():
    assert is_valid_sku_01482("abc123")
    assert not is_valid_sku_01482("")


def test_bucket_by_tag_01482():
    p = Product_01482("s1", 100, ["a"])
    assert bucket_by_tag_01482([p]) == {"a": ["s1"]}
