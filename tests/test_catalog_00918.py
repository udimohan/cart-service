"""Tests for catalog_00918."""

import pytest

from cartservice.generated.catalog_00918 import (
    Product_00918,
    bucket_by_tag_00918,
    is_valid_sku_00918,
    price_with_tax_00918,
)


def test_price_with_tax_00918():
    assert price_with_tax_00918(1000, 500) == 1050


def test_price_with_tax_negative_00918():
    with pytest.raises(ValueError):
        price_with_tax_00918(1000, -1)


def test_is_valid_sku_00918():
    assert is_valid_sku_00918("abc123")
    assert not is_valid_sku_00918("")


def test_bucket_by_tag_00918():
    p = Product_00918("s1", 100, ["a"])
    assert bucket_by_tag_00918([p]) == {"a": ["s1"]}
