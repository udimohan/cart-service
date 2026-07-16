"""Tests for catalog_00482."""

import pytest

from cartservice.generated.catalog_00482 import (
    Product_00482,
    bucket_by_tag_00482,
    is_valid_sku_00482,
    price_with_tax_00482,
)


def test_price_with_tax_00482():
    assert price_with_tax_00482(1000, 500) == 1050


def test_price_with_tax_negative_00482():
    with pytest.raises(ValueError):
        price_with_tax_00482(1000, -1)


def test_is_valid_sku_00482():
    assert is_valid_sku_00482("abc123")
    assert not is_valid_sku_00482("")


def test_bucket_by_tag_00482():
    p = Product_00482("s1", 100, ["a"])
    assert bucket_by_tag_00482([p]) == {"a": ["s1"]}
