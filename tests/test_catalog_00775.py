"""Tests for catalog_00775."""

import pytest

from cartservice.generated.catalog_00775 import (
    Product_00775,
    bucket_by_tag_00775,
    is_valid_sku_00775,
    price_with_tax_00775,
)


def test_price_with_tax_00775():
    assert price_with_tax_00775(1000, 500) == 1050


def test_price_with_tax_negative_00775():
    with pytest.raises(ValueError):
        price_with_tax_00775(1000, -1)


def test_is_valid_sku_00775():
    assert is_valid_sku_00775("abc123")
    assert not is_valid_sku_00775("")


def test_bucket_by_tag_00775():
    p = Product_00775("s1", 100, ["a"])
    assert bucket_by_tag_00775([p]) == {"a": ["s1"]}
